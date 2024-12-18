from transformers import AutoTokenizer, AutoModel
import pdb
import torch
import os
import json
import re
import random
from tqdm import tqdm
from importlib import import_module
import argparse
import sys
from prompts.prompt_template_persona2 import doc_keypoint_prompt_self_n_test # , doc_keypoint_prompt_self_test, doc_diff_instruct, doc_keypoint_prompt, doc_keypoint_prompt_self, doc_keypoint_prompt_math, doc_keypoint_prompt_few_atr, doc_keypoint_prompt_self_1_shot, doc_keypoint_prompt_self_1_shot_n_question, doc_keypoint_prompt_self_n_question
# os.environ["CUDA_VISIBLE_DEVICES"] = "3"
# model_id = "/data1/dyf/model/Llama-3.1-8B-Instruct/"
# tokenizer = AutoTokenizer.from_pretrained(model_id)
tokenizer_embedding = AutoTokenizer.from_pretrained('BAAI/bge-small-en-v1.5')
model_embedding = AutoModel.from_pretrained('BAAI/bge-small-en-v1.5') # , device_map={"": "cuda"}
model_embedding.eval()
# model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

def output_log_jsonl(log_file, all_logs):
    with open(log_file, "w") as f:
        for log in all_logs:
            f.write(json.dumps(log) + "\n")


def embedding_filter(txt, sentence_embedding):
    # Tokenize sentences
    encoded_input = tokenizer_embedding(txt, padding=True, truncation=True, return_tensors='pt')
    # for s2p(short query to long passage) retrieval task, add an instruction to query (not add instruction for passages)
    # encoded_input = tokenizer([instruction + q for q in queries], padding=True, truncation=True, return_tensors='pt')

    # Compute token embeddings
    with torch.no_grad():
        model_output = model_embedding(**encoded_input)
        # Perform pooling. In this case, cls pooling.
        txt_embeddings = model_output[0][:, 0]
    # normalize embeddings
    txt_embeddings = torch.nn.functional.normalize(txt_embeddings, p=2, dim=1)
    if sentence_embedding == []:
        sentence_embedding = txt_embeddings
        return True, sentence_embedding
    score_list =[txt_embeddings[0] @ sentence_embedding[i] for i in range(0, len(sentence_embedding))]
    # sentence_embedding = torch.cat((sentence_embedding, txt_embeddings), dim=0)
    if any(x > 0.8 for x in score_list):
        print('embedding不符')
        return False, sentence_embedding
    else:
        print('embedding符合要求')
        sentence_embedding = torch.cat((sentence_embedding, txt_embeddings), dim=0)
        return True, sentence_embedding
    # print("Sentence embeddings:", sentence_embeddings)

def doc_filter(txt, doc):
    # Tokenize sentences
    encoded_input = tokenizer_embedding([txt,doc], padding=True, truncation=True, return_tensors='pt')
    # for s2p(short query to long passage) retrieval task, add an instruction to query (not add instruction for passages)
    # encoded_input = tokenizer([instruction + q for q in queries], padding=True, truncation=True, return_tensors='pt')
    with torch.no_grad():
        model_output = model_embedding(**encoded_input)
        # Perform pooling. In this case, cls pooling.
        sentence_embeddings = model_output[0][:, 0]
    # normalize embeddings
    sentence_embeddings = torch.nn.functional.normalize(sentence_embeddings, p=2, dim=1)
    score = sentence_embeddings[0] @ sentence_embeddings[1]
    if score > 0.7:
        return True
    else:
        return False


def dynamic_import_function(function_path):
    '''
    Dynamically import a function from a path string (e.g., "module.submodule.my_function")
    templates.create_prompt_with_huggingface_tokenizer_template
    '''
    module_path, function_name = function_path.rsplit(".", 1)
    module = import_module(module_path)
    function = getattr(module, function_name)
    return function

def create_prompt_with_huggingface_tokenizer_template(messages, tokenizer, add_bos=False):
    formatted_text = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
    if add_bos:
        formatted_text = tokenizer.bos_token + formatted_text
    return formatted_text

def use_vllm(prompts, model, sampling_params, chat_formatting_function, tokenizer):
    
    # chat_formatting_function = dynamic_import_function("templates.create_prompt_with_huggingface_tokenizer_template")
    # model = vllm.LLM(
    #     model=model_id,
    #     tokenizer=model_id,
    #     tokenizer_mode="auto",
    #     tensor_parallel_size=torch.cuda.device_count(),
    #     tokenizer_revision=None, 
    #     revision=None,
    # )
    
    # sampling_params = vllm.SamplingParams(
    #     temperature=0.7,  # greedy decoding
    #     max_tokens=5000,
    #     # stop=args.additional_stop_sequence,
    #     # --additional_stop_sequence',
    #     # type=str,
    #     # nargs="+",
    #     # default=[],
    # )
    # apply chat formatting
    formatted_prompts = []
    for prompt in prompts:
        messages = [{"role": "user", "content": prompt}]
        formatted_prompt = chat_formatting_function(messages, tokenizer, add_bos=False)
        formatted_prompts.append(formatted_prompt)
    prompts = formatted_prompts
            
    outputs = model.generate(prompts, sampling_params)
    outputs = [it.outputs[0].text for it in outputs]
    return outputs[0]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--batch_dir",
        type=str,
        # required=True,
        default="/home/dyf/data_generate/doc-instruct/data/lima/epoch/diff/",
        help="The directory where the batch is stored.",
    )
    parser.add_argument(
        "--seed_tasks_path",
        type=str,
        # required=True,
        default="/home/dyf/data_generate/doc-instruct/data/lima/persona2/persona_add_lima_persona2_wo_vllm.jsonl",
        help="The path to the human written data.",
    )
    parser.add_argument(
        "--use_clf_seed_tasks_only",
        action="store_true",
        help="If specified, we will only use the classification seed tasks to prompt new instructions. This will lead to more classification instructions.",
    )
    parser.add_argument(
        "--batch_length",
        type=int,
        default=1000,
        help="ins generated each round",
    )
    parser.add_argument(
        "--roundi",
        type=int,
        default=0,
        help="round",
    )
    parser.add_argument(
        "--use_vllm",
        # required=True,
        action="store_true",
        # help="The path to the human written data.",
    )
    return parser.parse_args()

def UCB_sample_record(seed_tasks, batch_length, roundi, is_vllm, model, sampling_params, chat_formatting_function, tokenizer, model_id): #记录次数，并加入UCB评分进行采样
    # all_logs = [json.loads(l) for l in open("/home/dyf/data_generate/doc-instruct/data/start_tasks.jsonl", "r")]
    model_id = model_id.split('/')[-1]
    all_logs = []
    lima_tasks = [json.loads(l) for l in open("/home/dyf/data_generate/doc-instruct/data/lima_train.jsonl", "r")]
    test_log = []
    question_embedding = []
    raw_logs = []
    # attributions = ['subtopic', 'resource', 'scene', 'skill', 'audience', 'perspective', 'writer']
    # formats = ['Yes/No Question', 'Choice Question', 'WH Question', ]
    if is_vllm == True:
        for idx in tqdm(range(len(seed_tasks))): #len(seed_tasks)'
            if idx <= 836:
                continue
            task = random.sample(lima_tasks, 1)
            # sl_attributions = attributions # random.sample(attributions, 5)
            doc = seed_tasks[idx]['doc']
            # if len(doc) >=1000:
            #     doc = doc[0:1000]
            # doc_keypoint_prompt_math doc_keypoint_prompt_few_atr
            prompt = doc_keypoint_prompt_self_n_test.format(doc=doc, lima_question1=task[0]['conversations'][0])
            # prompt = doc_diff_instruct.format(doc1=task[0]['doc'], doc2=task[1]['doc'], doc3=task[2]['doc'], question1=task[0]['conversations'][0], question2=task[1]['conversations'][0], question3=task[2]['conversations'][0], doc=doc)
            # prompt = persona_diff_instruct_generate_simple.format(questioner1=task[0]['questioner'], questioner2=task[1]['questioner'], questioner3=task[2]['questioner'], question1=task[0]['conversations'][0], question2=task[1]['conversations'][0], question3=task[2]['conversations'][0])
            et = False
            while True:
                result = use_vllm([prompt], model, sampling_params, chat_formatting_function, tokenizer)
                # print(result) Ensure that the new questions are aligned with the selected attribute values, and that the new questions are independent of each other.
                try:
                    if '### New Questions:' in result:
                        text_question = result.split('### New Questions:')[1].strip('"').strip()
                        sl_attributions = result.split('### Attributes:')[1].split('### New Questions:')[0].strip('"').strip()
                    # else:
                    #     question = result.strip('"').strip()
                    break
                except:
                    et = True
                    break
            if et:
                continue
            print(prompt)
            print(result)
            # 使用正则表达式匹配每个问题的描述部分
            try:
                pattern = r'\d+\.\s*\*\*.*?\*\*:\s*(.*?)(?=\n\d+|\Z)'

                # 查找所有匹配的问题描述
                questions = re.findall(pattern, text_question, re.DOTALL)
                if len(questions) == 0:
                    # 使用换行符分割文本
                    questions = text_question.split('\n')
                    # 去除每个问题前的编号
                    questions = [q.split('. ', 1)[1] for q in questions if q[0].isdigit()]
            except:
                continue
            for question in questions:
                t = {}
                t['doc'] = doc
                t['sl_attributions'] = sl_attributions
                # t['lima'] = task[0]['conversations'][0]
                t['conversations'] = []
                t['conversations'].append(question)
                raw_logs.append(t)
                if len(raw_logs) % 500 == 0:
                    output_log_jsonl(os.path.join('/home/dyf/data_generate/doc-instruct/data/lima/raw_data/', f"diff_raw_instruct_{batch_length}_doc_round_{roundi}_{model_id}.jsonl"), raw_logs)
                if doc_filter(question, doc):
                    continue
                f1, _ = embedding_filter(question, question_embedding)
                if f1: # filter_output(documents, question) and filter_output(questioner_doc, questioner) and f1 and f2: # and filter_output(respondent_doc, respondent): # and quality_score_vllm(question, model, sampling_params, chat_formatting_function):
                    _, question_embedding = embedding_filter(question, question_embedding)
                    # documents.append(question)
                    # questioner_doc.append(questioner)
                    # respondent_doc.append(respondent)
                    print(question)
                    all_logs.append(t)
                    if len(all_logs) % 500 == 0:
                        output_log_jsonl(os.path.join('/home/dyf/data_generate/doc-instruct/data/lima/epoch/diff/', f"diff_new_instruct_{batch_length}_doc_round_{roundi}_{model_id}.jsonl"), all_logs)
                else:
                    test_ = {}
                    test_['id'] = idx
                    test_['result'] = [f1]
                    test_log.append(test_)
                    output_log_jsonl(os.path.join("/home/dyf/data_generate/doc-instruct/data/lima/wrong/", f"bool_log_round_{roundi}_{model_id}.jsonl"), test_log)
                    continue
                if len(all_logs) >= 1000:
                    output_log_jsonl(os.path.join('/home/dyf/data_generate/doc-instruct/data/lima/raw_data/', f"diff_raw_instruct_{batch_length}_doc_round_{roundi}_{model_id}.jsonl"), raw_logs)
                    output_log_jsonl(os.path.join('/home/dyf/data_generate/doc-instruct/data/lima/epoch/diff/', f"diff_new_instruct_{batch_length}_doc_round_{roundi}_{model_id}.jsonl"), all_logs)
                    sys.exit(0)
    # all_logs = seed_tasks + all_logs
    return all_logs


def main_diff(roundi, seed_tasks, is_vllm, batch_length, model, sampling_params, chat_formatting_function, tokenizer, model_id):
    # args = parse_args()
    # if args.use_clf_seed_tasks_only:
    #     seed_tasks = [t for t in seed_tasks if t["is_classification"]]
    # if roundi == 0:
    #     for t in seed_tasks:
    #         t['select_time'] = 1
    # print(args)
    # print(args.use_vllm)
    # os.makedirs(args.batch_dir, exist_ok=True)
    return UCB_sample_record(seed_tasks, batch_length, roundi, is_vllm, model, sampling_params, chat_formatting_function, tokenizer, model_id)

# if __name__ == "__main__":
#     args = parse_args()
#     seed_tasks = [json.loads(l) for l in open(args.seed_tasks_path, "r")]
#     if args.use_clf_seed_tasks_only:
#         seed_tasks = [t for t in seed_tasks if t["is_classification"]]
#     if args.roundi == 0:
#         for t in seed_tasks:
#             t['select_time'] = 1
#     os.makedirs(args.batch_dir, exist_ok=True)

#     do_random_sample_ucb = True
#     if do_random_sample_ucb == True:
#         UCB_sample_record(seed_tasks, args.batch_length)