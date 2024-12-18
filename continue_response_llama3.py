# 这里会让模型对指令生成多个回答，并采用rejection sampling 和 preference-based sampling来筛选出一个最好的回答
import os
import json
import argparse
from transformers import AutoTokenizer
# os.environ["CUDA_VISIBLE_DEVICES"] = "4,5,6,7"
# model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")
import vllm
from importlib import import_module
import torch
import copy
from tqdm import tqdm
# rejection sampling
# 接下来，我们设定一些标准，比如：
# 回答必须与问题相关。
# 回答不能含糊或模棱两可。

# preference-based sampling
# 假设我们从过去的用户反馈中了解到用户更喜欢直接、确定性的回答，而不是模棱两可的回答。
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--batch_dir",
        type=str,
        # required=True,
        default="/home/dyf/data_generate/doc-instruct/data/lima/",
        help="The directory where the batch is stored.",
    )
    parser.add_argument(
        "--seed_tasks_path",
        type=str,
        # required=True,
        default="/home/dyf/data_generate/doc-instruct/data/lima/epoch/com/com_new_instruct_round_1.jsonl",
        help="The path to the human written data.",
    )
    parser.add_argument(
        "--model_id",
        type=str,
        default=None
    )
    parser.add_argument(
        "--batch_length",
        type=float,
        default=10,
        help="ins generated each round",
    )
    return parser.parse_args()

def output_log_jsonl(log_file, all_logs):
    with open(log_file, "w") as f:
        for log in all_logs:
            f.write(json.dumps(log) + "\n")

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


def response_generate_main(batch_dir, seed_tasks, model, sampling_params, chat_formatting_function, tokenizer, model_id, batch_length):
    model_id = model_id.split('/')[-1]
    all_logs = []
    response_path = "/home/dyf/data_generate/doc-instruct/data/lima/response/raw_response_Llama-3.1-8B-Instruct_0.jsonl"
    seed_tasks_2 = [json.loads(l) for l in open(response_path, "r")]
    # import copy
    # original_list = [[1, 2, 3], [4, 5, 6]]
    copied_list = copy.deepcopy(seed_tasks)
    for t in tqdm(copied_list):
        flag = False
        # instruction = t['conversations'][0]
        # prompt = persona_com_instruct_generate_rewrite.format(questioner=questioner, question=question)
        prompt = t['conversations'][0].strip() # answer_generate.format(instruction=instruction).strip()
        for task2 in seed_tasks_2:
            if prompt == task2['conversations'][0]:
                all_logs.append(task2)
                if len(all_logs) % 500 == 0 or len(all_logs) == 4000:
                    output_log_jsonl(os.path.join(batch_dir, f"raw_response_{model_id}_{batch_length}.jsonl"), all_logs) 
                flag = True
        if flag:
            if len(all_logs) >= 4000:
                break
            continue

        # conversation = [{"role": "user", "content": inputs}]
        # tools = [get_current_weather]

        # format and tokenize the tool use prompt 
        # inputs = tokenizer.apply_chat_template(
        #             conversation,
        #             add_generation_prompt=True,
        #             # return_dict=True,
        #             return_tensors="pt",
        # )

        # inputs = inputs.to('cuda')
        result = use_vllm([prompt], model, sampling_params, chat_formatting_function, tokenizer).strip()
        # outputs = model.generate(inputs, max_new_tokens=5000, do_sample=True, temperature=0.7, top_p=0.9) #现在貌似是gs，后面可能要改成sample
        # result = tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True)
        # try:
        #     answer = result.split('### Response:')[1]
        # except:
        #     continue
        # answer = result
        print(result)
        t['conversations'].append(result)
        all_logs.append(t)
        if len(all_logs) % 500 == 0 or len(all_logs) == 4000:
            output_log_jsonl(os.path.join(batch_dir, f"raw_response_{model_id}_{batch_length}.jsonl"), all_logs)
        if len(all_logs) >= 4000:
            break

# def response_generate_main(batch_dir, seed_tasks, chat_formatting_function, model, sampling_params):
#     # args = parse_args()
#     # seed_tasks = [json.loads(l) for l in open(args.seed_tasks_path, "r")]
#     # chat_formatting_function = dynamic_import_function("templates.create_prompt_with_huggingface_tokenizer_template")
#     # model = vllm.LLM(
#     #     model=model_id,
#     #     tokenizer=model_id,
#     #     tokenizer_mode="auto",
#     #     tensor_parallel_size=torch.cuda.device_count(),
#     #     tokenizer_revision=None, 
#     #     revision=None,
#     # )
    
#     # sampling_params = vllm.SamplingParams(
#     #     temperature=0.0,  # greedy decoding
#     #     max_tokens=5000,
#     #     # stop=args.additional_stop_sequence,
#     #     # --additional_stop_sequence',
#     #     # type=str,
#     #     # nargs="+",
#     #     # default=[],
#     # )
#     single_sample(batch_dir, seed_tasks, chat_formatting_function, model, sampling_params)

if __name__ == "__main__":
    args = parse_args()
    batch_dir = args.batch_dir
    batch_length = args.batch_length
    seed_tasks = [json.loads(l) for l in open(args.seed_tasks_path, "r")]
    model_id = args.model_id
    chat_formatting_function = dynamic_import_function("templates.create_prompt_with_huggingface_tokenizer_template")
    model = vllm.LLM(
        model=model_id,
        tokenizer=model_id,
        tokenizer_mode="auto",
        tensor_parallel_size=torch.cuda.device_count(),
        tokenizer_revision=None,
        revision=None,
    )
    
    sampling_params = vllm.SamplingParams(
        temperature=0.0,  # greedy decoding
        max_tokens=5000,
        # stop=args.additional_stop_sequence,
        # --additional_stop_sequence',
        # type=str,
        # nargs="+",
        # default=[],
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    response_generate_main(batch_dir, seed_tasks, model, sampling_params, chat_formatting_function, tokenizer, model_id, batch_length)
