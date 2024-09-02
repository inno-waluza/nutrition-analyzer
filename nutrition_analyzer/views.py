from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
import json
from django.views.generic import TemplateView


class NutritionAnalyzerView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Load the model and tokenizer directly from Hugging Face
        model_name = "sgarbi/bert-fda-nutrition-ner"  # Replace with your actual model name on Hugging Face
        
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForTokenClassification.from_pretrained(model_name)
        except Exception as e:
            raise RuntimeError(f"Failed to load model or tokenizer from Hugging Face: {str(e)}")

    def post(self, request):
        try:
            # Ensure the request body is valid JSON
            text = request.data.get("recipe")
            if not text:
                return Response({"error": "No recipe provided."}, status=status.HTTP_400_BAD_REQUEST)

            # Tokenize the input
            inputs = self.tokenizer(text, return_tensors="pt")
            print(f"Tokenized input: {inputs}")

            # Pass the tokenized input to the model
            outputs = self.model(**inputs)
            print(f"Model outputs: {outputs}")

            # Get the predicted token classes
            predictions = torch.argmax(outputs.logits, dim=-1)
            print(f"Predictions: {predictions}")

            # Convert token IDs to labels
            labels = [self.model.config.id2label[label_id.item()] for label_id in predictions[0]]
            print(f"Labels: {labels}")

            # Convert token IDs to tokens
            tokens = self.tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
            print(f"Tokens: {tokens}")

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

            # Prepare the results in a user-friendly format
            result = []
            for token, label in combined_tokens:
                if label != "O" and token not in ["[CLS]", "[SEP]"]:
                    result.append({"ingredient": token, "major_nutrient": label.split('-')[1]})

            return Response({"analysis": result}, status=status.HTTP_200_OK)

        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON format."}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response({"message": "Use POST request to analyze a recipe."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

class AnalyzeInterface(TemplateView):
    template_name = 'analyze.html'

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

    