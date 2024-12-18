batch_dir=/home/dyf/data_generate/doc-instruct/data/lima/response/
CUDA_VISIBLE_DEVICES=4,5 python /home/dyf/data_generate/doc-instruct/response_generate.py \
    --seed_tasks_path /home/dyf/data_generate/doc-instruct/data/lima/epoch/diff/diff_new_instruct_0_doc_round_0_Mistral-7B-Instruct-v0.3.jsonl \
    --model_id /data1/dyf/model/Mistral-7B-Instruct-v0.3 \
    --batch_length 0 \
    --batch_dir ${batch_dir}


# /data1/dyf/model/Llama-3.1-8B-Instruct
# /data1/dyf/model/Llama-3.1-Tulu-3-8B
# /data1/dyf/model/Mistral-7B-Instruct-v0.3