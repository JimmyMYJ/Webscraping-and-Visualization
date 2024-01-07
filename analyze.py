from openai import OpenAI
client = OpenAI(api_key=(open("key.txt", "r").read()))
input_data = open("result.txt", "r").read()
def get_response(input_data):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "Compare the job posting and resume and provide improvements to the resume.", #Need another role for file upload
        },
        {
            "role": "user", 
            "content": input_data
        }
    ],
    max_tokens=150,
    )
    return response.choices[0].message.content