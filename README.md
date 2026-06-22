# AI Memory Assistant

## Overview

AI Memory Assistant is a personal memory-enabled chatbot built using LangChain, FAISS, Hugging Face Embeddings, and Groq LLMs.

Unlike traditional chatbots, this assistant can remember important information shared by users, retrieve relevant memories using semantic search, and generate personalized responses.

The project demonstrates concepts such as:

* AI Agents
* Long-Term Memory
* Vector Databases
* Embeddings
* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)

---

## Architecture

```text
User
 │
 ▼
Memory Agent
 │
 ├── Memory Retrieval
 │         │
 │         ▼
 │      FAISS Vector Store
 │
 ├── Memory Storage
 │         │
 │         ▼
 │      FAISS Vector Store
 │
 ▼
Prompt Builder
 │
 ▼
Groq LLM (Llama 3.1)
 │
 ▼
Response
```

---

## Workflow

### Step 1: User Input

The user enters a message.

Example:

```text
My name is Rahul
```

### Step 2: Memory Retrieval

The query is converted into embeddings and compared against stored memories using FAISS.

### Step 3: Prompt Construction

Relevant memories are added to the prompt along with the user's current message.

Example:

```text
Relevant Memories:
My name is Rahul

Current User Message:
What is my name?
```

### Step 4: LLM Response Generation

The prompt is sent to the Groq-hosted Llama 3.1 model.

The model generates a contextual response.

Example:

```text
Your name is Rahul.
```

### Step 5: Memory Storage

Important user information such as:

* Name
* Interests
* Preferences
* Goals
* Skills

is automatically stored for future retrieval.

---

## Technologies Used

* Python
* LangChain
* Groq API
* Llama 3.1 8B Instant
* FAISS Vector Database
* Hugging Face Embeddings
* Sentence Transformers
* dotenv

---

## Project Structure

```text
AI-Memory-Assistant/
│
├── app.py
├── agent.py
├── memory_store.py
├── tools.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Memory-Assistant.git
cd AI-Memory-Assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get a free API key from Groq Console.

---

## Running the Project

Start the application:

```bash
python app.py
```

Example:

```text
You: My name is Rahul

Assistant: Nice to meet you Rahul.

You: What is my name?

Assistant: Your name is Rahul.
```

---

## Key Concepts Demonstrated

### AI Agent

The Memory Agent coordinates memory retrieval, memory storage, prompt generation, and response generation.

### Embeddings

Text is converted into vector representations using Hugging Face sentence-transformer models.

### Vector Database

FAISS stores embeddings and performs similarity search.

### Retrieval-Augmented Generation (RAG)

Relevant memories are retrieved from FAISS and injected into the prompt before sending it to the LLM.

### Semantic Search

The assistant can find related memories even when exact keywords do not match.

---

## Future Improvements

* Streamlit Web Interface
* Multi-user Memory Support
* Memory Categorization
* Memory Importance Scoring
* Conversation History Tracking
* Database Integration (MongoDB/PostgreSQL)

---

## Author

Developed as a mini project to demonstrate AI Agents, Memory Systems, Vector Databases, and Retrieval-Augmented Generation using LangChain.
