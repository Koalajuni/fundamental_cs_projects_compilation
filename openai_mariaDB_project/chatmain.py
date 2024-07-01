from chat import chat_message
from dbadd import ChatGPTadd


while True:
    msg = input("질문:")
    rst = chat_message(msg)
    # db에 저장
    ChatGPTadd(msg, rst)
    print("답변:", rst)
