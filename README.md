# Medical Symptom Analyzer

A Streamlit-based application that analyzes medical symptoms and suggests potential treatments using AI-powered analysis.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hardikdeshmukh999/medical-symptom-analyzer.git
cd medical-symptom-analyzer
```

2. Create a virtual environment (recommended):
```bash
python -m venv .venv
```

3. Activate the virtual environment:
- On Windows:
```bash
.venv\Scripts\activate
```
- On macOS/Linux:
```bash
source .venv/bin/activate
```

4. Install the required packages:
```bash
pip install -r requirements.txt
```

## Requirements

The application requires the following Python packages:
- streamlit
- openai
- faiss-cpu
- numpy
- pickle (built-in)

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Enter your OpenAI API key in the sidebar
4. Describe your symptoms in the text area
5. Click "Analyze Symptoms" to get AI-powered analysis and recommendations

## Features

- AI-powered symptom analysis
- Treatment recommendations
- Dosage guidance
- User-friendly interface
- Real-time analysis

## Note

This application requires an OpenAI API key to function. You can obtain one from the [OpenAI website](https://platform.openai.com/).

## Disclaimer

This application is for informational purposes only and should not be used as a substitute for professional medical advice. Always consult with a healthcare professional for proper medical diagnosis and treatment. 