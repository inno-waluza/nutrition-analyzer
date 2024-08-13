from transformers import AutoTokenizer, AutoModelForTokenClassification

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("sgarbi/bert-fda-nutrition-ner")
model = AutoModelForTokenClassification.from_pretrained("sgarbi/bert-fda-nutrition-ner")

# Save the model and tokenizer locally
model.save_pretrained("./my_nutrition_model")
tokenizer.save_pretrained("./my_nutrition_tokenizer")
