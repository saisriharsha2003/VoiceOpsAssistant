import yaml
from fuzzywuzzy import fuzz

def calculate_similarity(input_text, examples):
    return max(fuzz.ratio(input_text.lower(), example.lower()) for example in examples)

def finding_intents(user_input):
    with open("C:\\Users\\ranke\\Harsha\\Projects\\harsha-desktop-virtual-assisstant\\ML Model\\intents.yaml", "r") as yaml_file:
        intents_data = yaml.safe_load(yaml_file)
    best_intent = None
    max_similarity = 0
    for intent_data in intents_data["intents"]:
        intent_examples = intent_data["examples"].strip().split("\n")
        similarity = calculate_similarity(user_input, intent_examples)
        if similarity > max_similarity:
            max_similarity = similarity
            best_intent = intent_data["intent"]
    return best_intent