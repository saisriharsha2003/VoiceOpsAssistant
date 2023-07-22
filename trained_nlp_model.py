import torch
from transformers import BertTokenizer, BertForSequenceClassification
import yaml

# Load the pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)

# Load intents from the YAML file
def load_intents_from_yaml(yaml_file):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
        intents = list(data['nlu'])
    return intents

# Replace 'training_data.yml' with the path to your YAML file
yaml_file = "training_data.yml"
intents = load_intents_from_yaml(yaml_file)

# Load the pre-trained model and set the number of labels
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=len(intents))

# Define the user input
user_input = "Hi, how are you?"

# Tokenize the user input and prepare it for the model
inputs = tokenizer(user_input, return_tensors="pt", padding=True, truncation=True)
outputs = model(**inputs)

# Get the predicted intent label
intent_idx = torch.argmax(outputs.logits, dim=1).item()
predicted_intent = intents[intent_idx]

print("Predicted Intent:", predicted_intent)
