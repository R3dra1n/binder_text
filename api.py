from openai import OpenAI
from pydantic import BaseModel
import json
import os

content=input("输入妳的广告:")

# OpenAI.api_key = os.getenv("OPENAI_API_KEY")
# print(os.getenv("OPENAI_API_KEY"))
client = OpenAI()
# 对话生成
# completion = client.chat.completions.create(
#     model="gpt-4o",
#
#     messages=[
#         {"role": "system", "content": "将以下文本进行分句，每个句子自然流畅，按句意完整地切分. reponse in JSON format"},
#         {"role": "user", "content": "我相信每个品牌都有独特的品牌定位和表达，也一定会有契合自身发展特点的营销方式，我认为适合自己的就是最好的。 "}
#     ],
#     response_format= { 'type': 'json_object' }
# )
#
# print(completion.choices[0].message.content)

# 生成图像
# response = client.images.generate(
#     prompt="A cute baby sea otter",
#     n=2,
#     size="1024x1024"
# )
#
# print(response.data[0].url)



# JSON结构化输出
# response = client.chat.completions.create(
#     model="gpt-4o-2024-08-06",
#     messages=[
#         {
#             "role": "system",
#             "content": "You extract email addresses into JSON data."
#         },
#         {
#             "role": "user",
#             "content": "Feeling stuck? Send a message to help@company.com. Or jason_hsu@gmail.com is also work."
#         }
#     ],
#     response_format={
#         "type": "json_schema",
#         "json_schema": {
#             "name": "email_schema",
#             "schema": {
#                 "type": "object",
#                 "properties": {
#                     "email": {
#                         "description": "The email address that appears in the input. could be more than one",
#                         "type": "string"
#                     },
#                     "additionalProperties": True
#                 }
#             }
#         }
#     }
# )

# print(response.choices[0].message.content);


# 流媒体输出
# stream = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role": "user", "content": "Say this is a test"}],
#     stream=True,
# )
# for chunk in stream:
#     if chunk.choices[0].delta.content is not None:
#         print(chunk.choices[0].delta.content, end="")
#

#结构化输出JSON
# from pydantic import BaseModel
# from openai import OpenAI

# class Step(BaseModel):
#     explanation: str
#     output: str

# class MathReasoning(BaseModel):
#     steps: list[Step]
#     final_answer: str

# completion = client.beta.chat.completions.parse(
#     model="gpt-4o-2024-08-06",
#     messages=[
#         {"role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step."},
#         {"role": "user", "content": "how can I solve 8x + 7 = -23"}
#     ],
#     response_format=MathReasoning,
# )

# math_reasoning = completion.choices[0].message.parsed
# print(math_reasoning)



class Sentence(BaseModel):
    
    number: int
    sentence: str
    


class Sentences(BaseModel):
    output: list[Sentence]


completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "将以下文本进行分句，每个句子自然流畅，按句意完整地切分. reponse in JSON format"},
        {"role": "user", "content": f"{content}"}
    ],
    response_format=Sentences,

    # response_format={
    #     "type": "json_schema",
    #     "json_schema": {
    #         "name": "sentences_schema",
    #         "schema": {
    #             "type": "object",
    #             "properties": {
    #                 "sentence": {
    #                     "description": "The sentence that appears in the input",
    #                     "type": "string"
    #                 },
    #                 "additionalProperties": False
    #             }
    #         }
    #     }
    # }



)

math_reasoning = completion.choices[0].message.parsed
output=math_reasoning.model_dump_json()
output_json= json.loads(output)

print(len(output_json.get("output")))
for i in range(len(output_json.get("output"))):

    print(output_json.get("output")[i])