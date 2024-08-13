from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

# Load the model and tokenizer from the local directory
tokenizer = AutoTokenizer.from_pretrained("./my_nutrition_tokenizer")
model = AutoModelForTokenClassification.from_pretrained("./my_nutrition_model")

# Now you can use the model as before

# Input text
#text = "2 mangoes, 1 tablespoon of salt, 1 cup of water"
text = input("enter recipe: ")
# Tokenize the input
inputs = tokenizer(text, return_tensors="pt")

# Pass the tokenized input to the model
outputs = model(**inputs)

# Get the predicted token classes
predictions = torch.argmax(outputs.logits, dim=-1)

# Convert token IDs to labels
labels = [model.config.id2label[label_id.item()] for label_id in predictions[0]]

# Convert token IDs to tokens
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

# Initialize variables for combining tokens
combined_tokens = []
current_token = ""
current_label = labels[0]

# Combine subwords and their labels
for token, label in zip(tokens, labels):
    if token.startswith("##"):
        current_token += token[2:]  # Append the subword to the current token
    else:
        if current_token:
            combined_tokens.append((current_token, current_label))
        current_token = token
        current_label = label

# Add the final token
if current_token:
    combined_tokens.append((current_token, current_label))

# Display the results in a user-friendly format
print("Extracted Ingredients and Labels:")
for token, label in combined_tokens:
    if label != "O" and token not in ["[CLS]", "[SEP]"]:  # Skip special tokens
        print(f"Ingredient: {token}, Major Nutrient: {label.split('-')[1]}")
