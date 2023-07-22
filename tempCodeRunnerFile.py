import random
import spacy
import yaml
with open("C:\\Users\\ranke\\Harsha\\Projects\\Desktop Assistant\\intents.yaml") as file:
    training_data = yaml.safe_load(file)
nlp = spacy.blank("en")

textcat=nlp.add_pipe('textcat', last=True)
labels = list(training_data.keys())
for label in labels:
    textcat.add_label(label)
train_data = []
for label, examples in training_data.items():
    for example in examples:
        train_data.append((example, {"cats": {label: 1}}))
optimizer = nlp.begin_training()
for epoch in range(20):
    random.shuffle(train_data)
    losses = {}
    for text, annotations in train_data:
        nlp.update([text], [annotations], sgd=optimizer, losses=losses)
    print(f"Epoch: {epoch+1}, Loss: {losses['textcat']}")
nlp.to_disk("C:\\Users\\ranke\\Harsha\Projects\\Desktop Assistant\\trained_model")
