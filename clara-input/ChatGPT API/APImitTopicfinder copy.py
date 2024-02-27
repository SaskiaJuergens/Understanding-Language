import openai
import gradio

openai.api_key = "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"

def initiate_chat(topic):
    return [
        {"role": "system", "content": f"you are a film critic with a select range of hobbies and interests. You enjoy talking to people. Make small talk. Let's chat about {topic}!"},
    ]

topic = "forest"
messages = initiate_chat(topic)

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Real Estate Pro")

demo.launch(share=True)
