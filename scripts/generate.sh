# batch_dir=/home/dyf/data_generate/persona-instruct/data/lima/epoch/com/

CUDA_VISIBLE_DEVICES=4,5 python /home/dyf/data_generate/doc-instruct/generate.py \
    --batch_dir /home/dyf/data_generate/doc-instruct/data/lima/response/ \
    --seed_tasks_path /home/dyf/data/doc/falcon.jsonl \
    --roundi 0 \
    --is_vllm \
    --model_id /data1/dyf/model/Llama-3.1-Tulu-3-8B \
    --batch_length 100000

# /data1/dyf/model/Llama-3.1-8B-Instruct
# /data1/dyf/model/Llama-3.1-Tulu-3-8B
# /data1/dyf/model/Mistral-7B-Instruct-v0.3