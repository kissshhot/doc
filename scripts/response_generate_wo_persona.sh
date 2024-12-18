batch_dir=/home/dyf/data_generate/doc-instruct/data/lima/response/
CUDA_VISIBLE_DEVICES=0,1 python /home/dyf/data_generate/doc-instruct/response_generate.py \
    --seed_tasks_path /home/dyf/data_generate/doc-instruct/data/lima/epoch/com/com_new_instruct_4000_round_1_Llama-3.1-Tulu-3-8B_unscore.jsonl \
    --model_id /data1/dyf/model/Llama-3.1-Tulu-3-8B \
    --batch_length 4000 \
    --batch_dir ${batch_dir}


# /data1/dyf/model/Llama-3.1-8B-Instruct
# /data1/dyf/model/Llama-3.1-Tulu-3-8B
# /data1/dyf/model/Mistral-7B-Instruct-v0.3