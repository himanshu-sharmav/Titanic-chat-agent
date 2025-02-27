# Titanic Dataset Chatbot

## Overview

The Titanic Dataset Chatbot is a web application that allows users to ask questions about the Titanic dataset and receive both text-based answers and visual insights. The application is built using FastAPI for the backend and Streamlit for the frontend, leveraging Google Generative AI (Gemini) for natural language processing.

## Features

- Ask questions in natural language about the Titanic dataset.
- Get clear text responses based on the dataset.
- Visualize data with helpful charts and graphs.
- User-friendly interface built with Streamlit.

## Technical Stack

- **Backend**: FastAPI
- **Agent Framework**: LangChain with Google Generative AI (Gemini)
- **Frontend**: Streamlit
- **Data Visualization**: Matplotlib and Seaborn

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/himanshu-sharmav/titanic-chatbot.git
   cd titanic-chatbot
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables. Create a `.env` file in the root directory and add your Google API key:

   ```
   GOOGLE_API_KEY=your_actual_google_api_key_here
   ```

## Usage

1. Start the FastAPI backend:

   ```bash
   uvicorn backend:app --reload
   ```

2. Start the Streamlit frontend:

   ```bash
   streamlit run app.py
   ```

3. Open your web browser and go to `http://localhost:8501` to interact with the chatbot.

## Example Questions

- "What percentage of passengers were male on the Titanic?"
- "Show me a histogram of passenger ages."
- "What was the average ticket fare?"
- "How many passengers embarked from each port?"

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
