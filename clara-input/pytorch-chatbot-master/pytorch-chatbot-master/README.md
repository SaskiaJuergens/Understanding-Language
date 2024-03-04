# Implementation of a Contextual Chatbot in PyTorch.  
Simple chatbot implementation with PyTorch. 

- The implementation should be easy to follow for beginners and provide a basic understanding of chatbots.
- The implementation is straightforward with a Feed Forward Neural net with 2 hidden layers.
- Customization for your own use case is super easy. Just modify `intents.json` with possible patterns and responses and re-run the training (see below for more info).

The approach is inspired by this article and ported to PyTorch: [https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077](https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077).

## Watch the Tutorial
[![Alt text](https://img.youtube.com/vi/RpWeNzfSUHw/hqdefault.jpg)](https://www.youtube.com/watch?v=RpWeNzfSUHw&list=PLqnslRFeH2UrFW4AUgn-eY37qOAWQpJyg)

## Installation

### Create an environment
Whatever you prefer (e.g. `conda` or `venv`)
```console
mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

### Activate it
Mac / Linux:
```console
. venv/bin/activate
```
Windows:
```console
venv\Scripts\activate
```
### Install PyTorch and dependencies

For Installation of PyTorch see [official website](https://pytorch.org/).

You also need `nltk`:
 ```console
pip install nltk
 ```

If you get an error during the first run, you also need to install `nltk.tokenize.punkt`:
Run this once in your terminal:
 ```console
$ python
>>> import nltk
>>> nltk.download('punkt')
```

## Usage
Run
```console
python train.py
```
This will dump `data.pth` file. And then run
```console
python chat.py
```
## API Key Setup:

The OpenAI API key is required to run this code. Please replace the placeholder "###" with your actual OpenAI API key.
Type of Request:

The code initiates a conversation with a predefined system message, setting the user as a film critic with specific hobbies and interests. The goal is to guide the conversation toward the movie "Alita" after a few interactions.
ChatGPT Request Function:

The CustomChatGPT function handles user inputs, sends the entire conversation to the OpenAI GPT-3.5 Turbo model, and returns the model's reply. The conversation history is maintained in the messages variable.

## Gradio Interface:

The Gradio interface (RobotTalkZone) is set up to take user input as text and display the model's response in real-time. It provides an interactive platform for users to engage with the ChatGPT model.
How to Run
Ensure you have the required dependencies installed. You can install them using:

Copy code
pip install openai gradio
Replace the OpenAI API key placeholder in the code with your actual API key.

Run the code. The Gradio interface will launch, allowing you to interact with the ChatGPT model.

## Additional Information
The code utilizes the GPT-3.5 Turbo model from OpenAI for natural language understanding and generation.
The gradio library is used to create a user-friendly interface for interacting with the ChatGPT model.
Feel free to experiment with different user inputs and explore the capabilities of RobotTalkZone Concept 02!
