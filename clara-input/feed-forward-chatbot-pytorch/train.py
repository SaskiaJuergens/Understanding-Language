import json
from nltk_utils import tokenize, stem, bag_of_words
import numpy as np

# Corrected import statement
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader


with open('intents.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = [] # tags and words

#tokenization
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

#stemming
ignore_words = ['?',',','.','!']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags = sorted(set(tags))

print(tags)

#create bag of words

X_train = []
Y_train = []
for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag) #bag of words
    label = tags.index(tag) #labels in numbers
    Y_train.append(label) # append the label / crossentropyloss

X_train = np.array(X_train)
Y_train = np.array(Y_train)

#create new dataset
#pytorch with batch chading
class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = Y_train
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    def __len__(self):
        return self.n_samples
    
#hyperparameters
batch_size = 8


dataset = ChatDataset()
train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle= True, num_workers=1)