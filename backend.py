from fastapi import FastAPI
import pandas as pd
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

# Load environment variables from .env file
load_dotenv()

# Load Titanic Dataset
df = pd.read_csv("titanic.csv")

# Load API Key securely
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Initialize FastAPI
app = FastAPI()

# Initialize LangChain with Gemini
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=api_key)

# Function to generate insights from the dataset
def get_titanic_insight(question):
    prompt = PromptTemplate.from_template(
        "You are an expert Titanic dataset analyst. Answer the user's question based on the dataset:\n\n{question}"
    )
    response = llm.invoke(prompt.format(question=question))
    return response.content  # Ensure we return text content properly

# Function to generate visualizations
def generate_visualization(query):
    query = query.lower()
    plt.figure(figsize=(8, 5))

    # Age visualization
    if any(phrase in query for phrase in ["histogram of age", "age histogram", "distribution of age", "passenger ages"]):
        sns.histplot(df["Age"].fillna(df["Age"].median()), bins=20, kde=True)
        plt.title("Distribution of Passenger Ages")
        
    # Embarkation port visualization
    elif any(phrase in query for phrase in ["embark", "port", "embarked from"]):
        sns.countplot(x=df["Embarked"].fillna("Unknown"))
        plt.title("Passengers per Embarkation Port")
        
    # Fare visualization
    elif any(phrase in query for phrase in ["fare", "ticket price", "ticket cost", "average fare"]):
        sns.histplot(df["Fare"], bins=30, kde=True)
        plt.title("Distribution of Ticket Fares")
        
    # Gender distribution
    elif any(phrase in query for phrase in ["gender", "male", "female", "sex"]):
        sns.countplot(x=df["Sex"])
        plt.title("Gender Distribution of Passengers")
        
    # Survival visualization
    elif any(phrase in query for phrase in ["survival", "survived", "died"]):
        sns.countplot(x=df["Survived"])
        plt.title("Survival Count")
        plt.xticks([0, 1], ["Did not survive", "Survived"])
        
    else:
        return None

    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format="png")
    plt.close()
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode("utf-8")
    return img_base64

# API Endpoint for text-based queries
@app.get("/query/")
async def query(question: str):
    response = get_titanic_insight(question)
    return {"response": response}

# API Endpoint for visualizations
@app.get("/visualize/")
async def visualize(query: str):
    img_base64 = generate_visualization(query)
    return {"image": img_base64} if img_base64 else {"error": "No visualization available"}
