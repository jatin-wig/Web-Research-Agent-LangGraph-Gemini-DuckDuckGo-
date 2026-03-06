# Web Research Agent (LangGraph + Gemini + DuckDuckGo)

An AI-powered multi-agent research system that automatically explores the web, gathers information, analyzes sources, and produces a polished research article.

The system uses LangGraph orchestration with Gemini LLMs to simulate a structured research workflow similar to how human researchers work.

---
## Demo Video

[![Watch the video](https://img.youtube.com/vi/8jJkpOccrOU/hqdefault.jpg)](https://www.youtube.com/watch?v=8jJkpOccrOU)

---

## Users simply enter a topic, and the agent performs:

- Research planning

- Web search and data collection

- Content summarization

- Article synthesis

- Final refinement
  
The result is a publication-quality article generated from live web data

## Features

- Multi-agent AI architecture
- Automated research query generation 
- Live web search using DuckDuckGo 
- Web scraping and text extraction
- Document summarization 
- AI-generated structured articles
- Article refinement for clarity and quality 
- Simple Streamlit interface

---

## Tech Stack

| Category | Technologies |
| :--- | :--- |
| **Language** | Python |
| **AI & Frameworks** | LangGraph, LangChain, Google Gemini API |
| **Web Data** | DuckDuckGo Search, BeautifulSoup (Web Scraping) |
| **Frontend** | Streamlit |

---
 
# Setup Instructions

## 1) Clone the Repository
```bash

git clone https://github.com/jatin-wig/Web-Research-Agent-LangGraph-Gemini-DuckDuckGo-.git
```

## 2) Install Dependencies
```bash
pip install -r requirements.txt
```

## 3) Add Gemini API Key (Required)

Create a .env file in the project root directory:

GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

## Important:

Do not upload .env to GitHub

Keep your Gemini API key private

## 4) Run the App
```bash
streamlit run app.py
 ```
or 
```bash
python -m streamlit run app.py 
```

# Built by Jatin Wig
### GitHub: https://github.com/jatin-wig





