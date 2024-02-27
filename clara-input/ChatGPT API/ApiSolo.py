import openai
import gradio
import json

openai.api_key = "Ihr_API-Schlüssel_hier_einfügen"

# Laden Sie die ursprüngliche frameslot.json
with open("frameSlots.json", "r") as file:
    frameslot_data = json.load(file)

def initiate_chat():
    return [
        {"role": "system", "content": "Sie sind ein Filmkritiker mit einer Auswahl an Hobbys und Interessen. Sie unterhalten sich gerne. Lassen Sie uns Smalltalk machen.Führen Sie das gespräch freundlich in Richtung dem Film Alita. Gern verknüft mit Inhalten des Films"},
    ]

messages = initiate_chat()

def refill_frameslot(data, user_input):
    # Überprüfen Sie, ob der Chat in Richtung Alita geht
    if "alita" in user_input.lower():
        # Aktualisieren Sie frameslot_data mit Alita-Informationen
        data["request_slots"][0]["movieKnowledge"] = ["ja"]  # Sie können dies entsprechend der Benutzereingabe anpassen
        # Fügen Sie bei Bedarf weitere Felder hinzu

    return data

def CustomChatGPT(user_input):
    global frameslot_data
    messages.append({"role": "user", "content": user_input})
    
    # Fügen Sie eine Anfrage für Smalltalk über Alita hinzu
    if "smalltalk" in user_input.lower():
        messages.append({"role": "assistant", "content": "Haben Sie den Film Alita: Battle Angel gesehen? Er ist ziemlich faszinierend!"})
    else:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        ChatGPT_reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": ChatGPT_reply})

        # Refill frameslot.json, wenn der Chat in Richtung Alita geht
        frameslot_data = refill_frameslot(frameslot_data, user_input)

    return ChatGPT_reply

# Gradio-Schnittstelle starten
demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Chat mit Alita")
demo.launch(share=True)

