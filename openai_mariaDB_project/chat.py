import openai
import config


OPENAI_KEY = config.KEY
openai.api_key = OPENAI_KEY

# 인공지능 모델 선택
MODEL = "gpt-3.5-turbo"

###################################################
# Chat GPT 함수
###################################################


def chat_message(msg):
    # msg = input("gpt에게 물어보세요..")

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "MIT대학 교수처럼 답변해줘"},
            {"role": "user", "content": msg},
            {"role": "assistant", "content": "과학 얘기 관련된 얘기만 해줘"}
        ],
        temperature=0,
    )
    # print(response)
    return (response['choices'][0].message.content)
