# 🤖 AI Learning Mentor Chatbot

An AI-powered learning mentor chatbot built with LangChain and Streamlit.

The chatbot helps students with:

- Programming
- Machine Learning & AI
- Web Development
- General Computer Science

The project demonstrates the use of:

- PromptTemplate
- Pydantic Structured Output
- RunnableBranch
- RunnableParallel
- Streamlit
- ChatGroq

---

# Project Objective

The objective of this project is to build a beginner-friendly AI mentor
that can identify the topic and type of a student's question, route the
question to the appropriate mentor using RunnableBranch, and generate
multiple outputs simultaneously using RunnableParallel.

The final response is validated using Pydantic Structured Output and
displayed through a Streamlit chat interface.

---

# Features

## 1. Topic Classification

The chatbot identifies questions as one of:

- Programming
- ML & AI
- Web Development
- General CS

## 2. Question Type Classification

The chatbot also identifies the student's requirement:

- Concept
- Code
- Debug
- Explanation

## 3. Programming Mentor

Provides help with Python and general programming concepts.

## 4. ML & AI Mentor

Provides help with:

- Machine Learning
- Deep Learning
- CNN
- RNN
- LSTM
- NLP
- Generative AI

## 5. Web Development Mentor

Provides help with:

- HTML
- CSS
- JavaScript
- React
- FastAPI
- APIs
- Authentication
- Databases

## 6. General CS Mentor

Provides help with:

- Data Structures
- Algorithms
- Operating Systems
- Computer Networks
- DBMS
- OOP
- Computer Science fundamentals

## 7. Beginner-Friendly Answers

The chatbot is designed for learners and explains concepts using
simple language and examples.

---

# LangChain Architecture

The application follows this workflow:

User Question
      |
      v
Pydantic Question Classification
      |
      v
RunnableBranch
      |
      +---- Programming Mentor
      |
      +---- ML & AI Mentor
      |
      +---- Web Development Mentor
      |
      +---- General CS Mentor
      |
      v
RunnableParallel
      |
      +---- Main Answer
      |
      +---- Summary
      |
      +---- Keywords
      |
      +---- Some Suggested Question
      |
      v
Pydantic MentorResponse
      |
      v
Streamlit Chat Interface

---

# RunnableBranch Implementation

RunnableBranch is used to route the question to different mentor
pipelines according to the detected topic.

Example:

```python
mentor_branch = RunnableBranch(

    (
        lambda x: x["topic"] == "Programming",
        programming_chain
    ),

    (
        lambda x: x["topic"] == "ML & AI",
        ml_ai_chain
    ),

    (
        lambda x: x["topic"] == "Web Development",
        web_development_chain
    ),

    general_cs_chain
)
```