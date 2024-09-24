# Text Classification App with Hugging Face LLM
This is a simple web application that allows users to input text and receive classification probabilities from a pre-trained Large Language Model (LLM) loaded via Hugging Face. The app consists of a Flask API for processing the text and returning model predictions, and an HTML frontend that displays the results using a dynamic bar graph.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Technologies Used](#technologies-used)
- [License](#license)

## Features
- Load any Hugging Face LLM model defined in a configuration file.
- Submit text from the frontend and receive class probabilities in real-time.
- Dynamic bar chart to visualize classification probabilities.
- Clean and responsive UI powered by Bootstrap and Chart.js.

## Installation
1. Clone the Repository:

```bash
git clone (https://github.com/GutoL/LLM_deployment.git)
cd LLM_deployment-main
```
2. Set up a Virtual Environment (Optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install dependencies
   
```bash
pip install -r requirements.txt
```

4. Prepare the Configuration:

  - Ensure you have a `predictor.config` file in the root of the project. This file should define the Hugging Face model to load in JSON format. Example `predictor.config`:

```json
{
  "model_name": "cardiffnlp/twitter-roberta-base-sentiment-latest"
}
```

## Usage
1. Run the Flask API:
```bash
python app.py
```

2. Access the Web App:

- Open your browser and navigate to `http://localhost:5000`.
- Input text into the form and click "Submit Text."
- The app will display the classification probabilities for the input text in a bar graph.

### Example Workflow:
1. User inputs a sentence such as "The movie was fantastic!"
2. the input is sent to the API, which loads the tokenizer and model based on the configuration.
3. The API returns a JSON response containing class probabilities (e.g., positive: 0.97, neutral: 0.02, negative: 0.01).
4. The frontend visualizes these probabilities as a bar chart.

## Project Structure
```graphql
LLM_deployment-main/
│
├── text_analysis.py               # Flask API that serves predictions
├── predictor.config      # Configuration file defining the Hugging Face model
├── requirements.txt      # Python dependencies
├── static/
│   ├── style.css         # Custom CSS for the frontend
│   └── script.js         # JavaScript to handle form submission and graph rendering
├── templates/
│   └── index.html        # Frontend HTML file
└── README.md             # This README file
```
## Configuration
The model to be loaded by the API is specified in the predictor.config file as JSON. It should include the Hugging Face model name as shown below:

```json
{
  "model_name": "cardiffnlp/twitter-roberta-base-sentiment-latest"
}
```
The API reads this configuration to load the appropriate tokenizer and model during runtime.

## Technologies Used

- Flask: Backend framework to serve the API.
- Hugging Face Transformers: For loading pre-trained language models.
- flask_classful: To structure the API into classes.
- Bootstrap: Frontend framework for responsive design.
- Chart.js: JavaScript library to visualize model output as a bar graph.
- jQuery: Simplifies DOM manipulation and AJAX requests.

## License
This project is licensed under the Apache License 2.0 License. See the `LICENSE` file for details.
