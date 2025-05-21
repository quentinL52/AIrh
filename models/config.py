import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Dict, List, Any, Tuple, Optional, Type
from crewai import LLM
#########################################################################################################
# formatage du json
def format_cv(document):
    def format_section(title, data, indent=0):
        prefix = "  " * indent
        lines = [f"{title}:"]
        if isinstance(data, dict):
            for k, v in data.items():
                if isinstance(v, (dict, list)):
                    lines.append(f"{prefix}- {k.capitalize()}:")
                    lines.extend(format_section("", v, indent + 1))
                else:
                    lines.append(f"{prefix}- {k.capitalize()}: {v}")
        elif isinstance(data, list):
            for i, item in enumerate(data):
                lines.append(f"{prefix}- Élément {i + 1}:")
                lines.extend(format_section("", item, indent + 1))
        else:
            lines.append(f"{prefix}- {data}")
        return lines
    sections = []
    for section_name, content in document.items():
        title = section_name.replace("_", " ").capitalize()
        sections.extend(format_section(title, content))
        sections.append("") 
    return "\n".join(sections)


def read_system_prompt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
#########################################################################################################        
# modéles 
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
model_groq = "llama-3.1-8b-instant" #"llama-3.3-70b-versatile"
def chat_groq() :
  llm = ChatGroq(model=model_groq) 
  return llm

GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
model_google = "gemini-2.0-flash"
def chat_gemini():
    llm = ChatGoogleGenerativeAI(model=model_google)
    return llm

def agents_model():
    gemini_llm = LLM(
        model=f"gemini/{model_google}",
        api=GEMINI_API_KEY,
        température=0)
    return gemini_llm 
    
        

      
        

