import streamlit as st

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage
)
from chatbot import run_chatbot

load_dotenv()


#================================
# Header
#================================
st.header("Programming Mentor Chatbot")


#================================
# Create the chat history only once
#================================


if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(
            content="""
You are an expert Programming Mentor and AI Learning Assistant.

Your primary goal is to help students LEARN:
- Programming
- Machine Learning and AI
- Web Development
- General Computer Science

Explain concepts clearly, provide practical examples,
help students debug their code, and encourage them
to understand the solution rather than simply copy it.
"""
        )
    ]


#================================
# Display previous messages
#================================


for message in st.session_state.chat_history:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)


# Sidebar
with st.sidebar:
    st.subheader("Programming Mentor Chatbot")
    st.subheader("Topics:")
    st.markdown("""
    - Programming
    - ML and AI
    - Web Development
    - General Computer Science

  """)

    st.divider()

    st.subheader("Chat History")
    messages=[
        message
        for message in st.session_state.chat_history
        if isinstance(message,(HumanMessage,AIMessage)) 
         
    ]
    if not messages:
        st.caption("No Conversation Yet")
    else:
        for message in st.session_state.chat_history:
            if isinstance(message,HumanMessage):
                with st.chat_message("User"):
                   st.write(message.content)
            
            if isinstance(message,AIMessage):
                with st.chat_message("assistant"):    
                   st.write(message.content)


    if st.button("Clear Chat",use_container_width=True):
        st.session_state.chat_history=[
             SystemMessage(
                         content="""
             You are an expert Programming Mentor and AI Learning Assistant.
             
             Your primary goal is to help students LEARN:
             - Programming
             - Machine Learning and AI
             - Web Development
             - General Computer Science
             
             Explain concepts clearly, provide practical examples,
             help students debug their code, and encourage them
             to understand the solution rather than simply copy it.
             """
                     )
        ]
        st.rerun()

#================================            
#Take User input
#================================


user_input=st.chat_input("Type Your Question")

if user_input:
    if user_input.strip().lower()=="exit":
        st.stop()


    #================================
    #Store the user message
    #================================
    st.session_state.chat_history.append(HumanMessage(content=user_input))



    #================================
    #disply the user message
    #================================
    with st.chat_message("user"):
        st.write(user_input)


    #================================
    #Model Input
    #================================
    
    result=run_chatbot(user_input)
    answer=result['answer']
    suggested_questions = result.get(
                    "suggested_questions",
                    []
                )

    #================================
    #Chat History Text
    #================================
    
    history_text=answer.answer
    st.session_state.chat_history.append(AIMessage(content=history_text))



    with st.chat_message("assistant"):
        
        # answer=result['answer']
        #================================
        #Answer
        #================================

        st.markdown("###  Answer")
        st.markdown(answer.answer)

        #================================
        #Summary
        #================================

        st.markdown("###  Summary")
        st.markdown(answer.summary)

        #================================
        #key Points
        #================================

        if answer.key_points:
            st.markdown("### Key Points")
            for index,point in enumerate(answer.key_points,start=1):
                st.markdown(f"{index}.  {point}")


        #================================
        #Keywords
        #================================

        st.markdown("### Keywords")

        if answer.keywords:
            st.write(",".join(answer.keywords))
        else:
            st.write("No Keywords available")
        
        
        #================================
        # CODE
        #================================
        
        if answer.code:
        
                st.markdown("###  Code")
                st.code(answer.code)
        
        
        #================================
        # EXAMPLE
        #================================
        
        if answer.example:
        
            st.markdown("###  Example")
            st.write(answer.example)
        
        
        
        #================================
        # SUGGESTED QUESTIONS
        #================================
        
        if suggested_questions:
            st.markdown("###  Suggested Questions")
            for index, suggestion in enumerate(suggested_questions,start=1):
                st.markdown(f"{index}. {suggestion}")
        
        
        #================================
        # CATEGORY + CONFIDENCE
        #================================
        
        st.caption(
                f"Category: {answer.category} | "
                f"Confidence: {answer.confidence:.0%}"
            )