import openai
import gradio

openai.api_key = "####"

messages = [{"role": "system", "content": "You are a cinamavisitor that makes publicity for the next movie called the Alita"}]


#saving the chat and append it to message -> send it it gbt 
def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    #safe reply
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")

demo.launch(share=True)