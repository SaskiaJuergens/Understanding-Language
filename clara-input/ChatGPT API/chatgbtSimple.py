import openai

openai.api_key = "####"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "please imitate a chat between customer and person who makes publicity for the movie called Alita"}])
print(completion.choices[0].message.content)