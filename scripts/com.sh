CUDA_VISIBLE_DEVICES=6,7 python /home/dyf/data_generate/doc-instruct/complexity.py \
    --seed_tasks_path /home/dyf/data_generate/doc-instruct/data/lima/epoch/com/com_new_instruct_4000_round_2_Llama-3.1-Tulu-3-8B.jsonl \
    --batch_length 4000 \
    --model_id /data1/dyf/model/Llama-3.1-Tulu-3-8B \
    --roundi 2