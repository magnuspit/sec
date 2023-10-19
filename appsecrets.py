import openai
#from dotenv import load_dotenv

#load_dotenv()

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful sports assistant."},
        {"role": "user", "content": "what is the football team that won more Champion leagues?"}
    ]
)

result = ''
for choice in response.choices:
    result += choice['message']['content']

print(result)
