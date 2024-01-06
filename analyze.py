import openai
openai.api_key = open("key.txt", "r").read().strip('\n')
output = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo"
    messages = [
        {
            "role": "user",
            "content": #Input Data
        }
    ]
)