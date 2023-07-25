from fuzzywuzzy import fuzz
import yaml

# Load the YAML file containing intents
with open("C:\\Users\\ranke\\Harsha\\Projects\\Desktop Assistant\\intents.yaml", "r") as yaml_file:
    intents_data = yaml.safe_load(yaml_file)

# Process user input
user_input = "Hey, what time is it?"


# Function to calculate similarity between user input and example phrases
def calculate_similarity(input_text, examples):
    return max(fuzz.ratio(input_text.lower(), example.lower()) for example in examples)


# Find the best matching intent based on similarity
best_intent = None
max_similarity = 0

for intent_data in intents_data["intents"]:
    intent_examples = intent_data["examples"].strip().split("\n")
    similarity = calculate_similarity(user_input, intent_examples)
    if similarity > max_similarity:
        max_similarity = similarity
        best_intent = intent_data["intent"]

# Implement If-Else logic based on the extracted intent
if best_intent == "greet":
    print("Hello! How can I assist you?")
elif best_intent == "search_chrome":
    print("Opening Chrome and searching...")
elif best_intent == "send_whatsapp":
    print("Sending a message on WhatsApp...")
# Add more elif blocks for other intents
elif best_intent is not None:
    print("Executing the action for intent:", best_intent)
else:
    print("I'm sorry, I didn't understand that.")
