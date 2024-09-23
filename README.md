# Text Classification App with Hugging Face LLM
This is a simple web application that allows users to input text and receive classification probabilities from a pre-trained Large Language Model (LLM) loaded via Hugging Face. The app consists of a Flask API for processing the text and returning model predictions, and an HTML frontend that displays the results using a dynamic bar graph.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project_structure)
- [Configuration](#configuration)
- [Technologies Used](#technologies)
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
