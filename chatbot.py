from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from schemas import MentorResponse,QuestionClassification,Suggested
from langchain_core.runnables import RunnableParallel,RunnableBranch
from prompts import (
    PROGRAMMING_PROMPT,
    ML_AI_PROMPT,
    WEB_DEVELOPMENT_PROMPT,
    GENERAL_CS_PROMPT,
    SUGGESTION_PROMPT,
    CLASSIFICATION_PROMPT
)


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv()

output_parser=PydanticOutputParser(pydantic_object=MentorResponse)
classification_parser = PydanticOutputParser(pydantic_object=QuestionClassification)
suggestion_parser=PydanticOutputParser(pydantic_object=Suggested)
# ============================================================
# LANGCHAIN MODEL
# ============================================================

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
)

# ============================================================
# All CHAIN
# ============================================================
classification_chain=CLASSIFICATION_PROMPT | model | classification_parser
programming_chain = PROGRAMMING_PROMPT | model | output_parser

ml_ai_chain = ML_AI_PROMPT| model | output_parser

we_dev_chain= WEB_DEVELOPMENT_PROMPT | model

gen_cs_chain=GENERAL_CS_PROMPT | model | output_parser

suggetion_chain=SUGGESTION_PROMPT | model | suggestion_parser


# ============================================================
# Condition CHAIN  | RunnableBranch
# ============================================================
conditional_chain=RunnableBranch(
    (lambda x:x['question']=='Programming',programming_chain),
    (lambda x:x['question']=='ML & AI',programming_chain),
    (lambda x:x['question']=='Web Development',programming_chain),
    gen_cs_chain
)

# ============================================================
# Parallel CHAIN | RunnableParallel
# ============================================================
parallel_chain = RunnableParallel(
    {
        "Answer" : conditional_chain,
        "questions": suggetion_chain
    }
)



# classify = classification_chain.invoke({
#     "question": "What is LSTM?"
# })

# print(classify.topic)

# result=conditional_chain.invoke({"question":"What is LSTM?"})

# print(result.answer)

# question = suggetion_chain.invoke({
#     "question": "What is LSTM?",
#     "category": classify.topic
# })

# for i, q in enumerate(question.questions, start=1):
#     print(f"{i}. {q}")


# result=parallel_chain.invoke({"question":"What is LSTM?"})

# print(result['Answer'])
# print(result['questions'])



def run_chatbot(user_question: str):
    result = parallel_chain.invoke({
        "question": user_question
    })

    answer = result["Answer"]
    suggestions = result["questions"]

    return {
        "answer": answer,
        "suggested_questions": suggestions.questions
    }