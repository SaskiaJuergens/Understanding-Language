import openai
import gradio
import json

openai.api_key = "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"

# Load initial frameslot.json
with open("frameslot.json", "r") as file:
    frameslot_data = json.load(file)

def initiate_chat(topic):
    return [
        {"role": "system", "content": f"you are a film critic with a select range of hobbies and interests. You enjoy talking to people. Make small talk. Let's chat about {topic}!"},
    ]

topic = "Alita"  # Change the topic to "Alita"
messages = initiate_chat(topic)

def refill_frameslot(data, user_input):
    # Check if the topic is Alita
    if topic.lower() == "alita":
        # fill the json for Alita
        user_input = gradio.Interface(fn=lambda x: x, inputs="text", outputs="text", title="Alita Information Prompt").launch()
        # Update frameslot_data with Alita information
        data["request_slots"][0]["movieKnowledge"] = ["yes"]  # You can modify this based on user input
        # Add more fields as needed

    return data

def CustomChatGPT(user_input):
    global frameslot_data
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})

    # Refill frameslot.json if the topic is Alita
    frameslot_data = refill_frameslot(frameslot_data, user_input)

    return ChatGPT_reply

# Save the updated frameslot_data to frameslot.json
with open("frameSlots.json", "w") as file:
    json.dump(frameslot_data, file, indent=2)

# Gradio Interface
demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Real Estate Pro")
demo.launch(share=True)
