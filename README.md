# Recipe Analyzer

## Overview

The Recipe Analyzer is a web application designed to analyze recipes and extract nutritional information using BERT for Named Entity Recognition (NER). Instead of traditional food recommendation systems, this application uses advanced NLP techniques to identify ingredients and their associated nutrients.

## Features

- **Recipe Analysis**: Users can input a recipe description, and the application will process it to extract nutritional details.
- **Nutritional Information Extraction**: Utilizes a BERT-based model (`sgarbi/bert-fda-nutrition-ner`) from Hugging Face to identify and classify ingredients and nutrients.

## Technologies Used

- **Backend**: Django with Django REST Framework (DRF)
- **NER Model**: BERT-based model (`sgarbi/bert-fda-nutrition-ner`) from Hugging Face Transformers library
- **Frontend**: HTML, CSS, and JavaScript

## Installation

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/recipe-analyzer.git
    cd recipe-analyzer
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Django development server:**

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

5. **Navigate to `http://127.0.0.1:8000/api/analyzer/` in your web browser to use the application.**

## Usage

- **Access the Application**

  Open your browser and navigate to [http://127.0.0.1:8000/api/analyzer/](http://127.0.0.1:8000/api/analyzer/).

- **Analyze a Recipe**

  - Enter a recipe description (e.g., "2 mangoes, 1 tablespoon of salt, 1 cup of water").
  - Click the "Analyze Recipe" button to see the nutritional analysis.

- **API Endpoint**

  - **POST** `/api/analyze/`: Analyzes the provided recipe and returns nutritional information.
  - **GET** `/api/analyze/`: Returns a message indicating that only POST requests are supported.

## API Documentation

### POST `/api/analyze/`

**Request Body**:
```json
{
  "recipe": "string"  // The recipe description to be analyzed
} 
```
**Response**:
```json
{
  "analysis": [
    {
      "ingredient": "string",    // Extracted ingredient
      "major_nutrient": "string" // Nutrient associated with the ingredient
    }
  ]
}
```
## License

This project is licensed under the MIT License - see the LICENSE file for details.

