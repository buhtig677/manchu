import json
from pathlib import Path
from openai import OpenAI
from tqdm import tqdm
import time
import os

client = OpenAI(
    api_key="sk-UgOzUkp0isSDppPC3uMVztt4ZJmnDXUUJx0jll57XPkbHIVO",  # 在这里将 MOONSHOT_API_KEY 替换为你从 Kimi 开放平台申请的 API Key
    base_url="https://api.moonshot.cn/v1",
)

user_prompt = """
docs_1.txt是介绍一篇论文的网页，可能包含了论文的标题和关键词和摘要。
你需要将网页上的论文标题和摘要以及关键字抽取出来。
请使用如下 JSON 格式输出你的回复：
{
    "title": "标题",
    "abstract": "摘要",
    "keywords": "关键字"
}
注意，请将文字信息放置在 `text` 字段中，将摘要放在 `abstract` 字段中，将关键字放置在 `keywords` 字段中。
请记住，保证原文输出，不需要翻译成中文。并且只需要json格式数据，不需要额外信息。
"""
title = """What matters in the queer archive? Technologies of memory and Queering the Map"""
file_content = None
completion = client.chat.completions.create(
    model="moonshot-v1-128k",
    messages=[
        {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},  # <-- 将附带输出格式的 system prompt 提交给 Kimi
        {"role": "system", "content": file_content},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.3,
    response_format={"type": "json_object"},  # <-- 使用 response_format 参数指定输出格式为 json_object
)
# 由于我们设置了 JSON Mode，Kimi 大模型返回的 message.content 为序列化后的 JSON Object 字符串，
# 我们使用 json.loads 解析其内容，将其反序列化为 python 中的字典 dict。
print(completion.choices[0].message.content)


