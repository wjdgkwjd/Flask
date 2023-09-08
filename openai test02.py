import openai
openai.api_key = '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'

# {"role": "system", "content": "You are a helpful assistant."},
# {"role": "user", "content": "Who won the world series in 2020?"},
#{"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
# {"role": "user", "content": "Where was it played?"}

messages = []
messages.append({"role": "system", "content": "너는 제주과학고등학교 학생이다."})
messages.append({"role": "system", "content": "너의 이름은 제돌이다."})
while True:
    question = input("me: ")
    if  question =="": break

    messages.append({"role": "user", "content": question})

    aiObj = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= messages
    )
    response=aiObj['choices'][0]['message']['content']#AI 답변 내용
    print(aiObj)

    print(f"AI: {response}")