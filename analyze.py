from openai import OpenAI
client = OpenAI(api_key=(open("key.txt", "r").read()))

def get_response(input_data):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {"role": "user", 
        "content": input_data}
    ],
    max_tokens=150,
    )
    return response

print(get_response("hi"))