import json

def output_log_jsonl(log_file, all_logs):
    with open(log_file, "w") as f:
        for log in all_logs:
            f.write(json.dumps(log) + "\n")

# 打开JSON文件
with open('/home/dyf/data_generate/doc-instruct/data/lima/epoch/diff/0.8_4000_Llama-3.1-Tulu-3-8B.json', 'r', encoding='utf-8') as file:
    # 加载JSON数据
    data = json.load(file)
all_log = []
for t in data:
    tmp = {}
    tmp['conversations'] = []
    tmp['conversations'].append(t['conversations'][0]['content'])
    all_log.append(tmp)
output_log_jsonl("/home/dyf/data_generate/doc-instruct/data/lima/epoch/diff/0.8_4000_Llama-3.1-Tulu-3-8B.jsonl", all_log)

# 现在data变量包含了JSON文件中的数据
# print(data)