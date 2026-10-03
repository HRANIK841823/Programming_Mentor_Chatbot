from typing import List, Literal, Optional
from pydantic import BaseModel, Field



# ============================================================
# Some Suggested Question
# ============================================================
class Suggested(BaseModel):
    questions: List[str] = Field(description="3 to 5 useful follow-up questions related to the student's question.")


# ============================================================
# QUESTION CLASSIFICATION
# ============================================================

class QuestionClassification(BaseModel):
    topic: Literal["Programming", "ML & AI","Web Development","General CS"] = Field(description="The topic of the student's question.")

# ============================================================
# FINAL MENTOR RESPONSE
# ============================================================

class MentorResponse(BaseModel):
    answer: str = Field(
        description="The main mentor answer. Give a clear, accurate explanation. within 2-3 lines beginner friendly"
    )

    summary: str = Field(
        description="A short 1-2 sentence summary of the answer."
    )

    keywords: List[str] = Field(
        description="Important technical keywords related to the question."
    )

    category: Literal[
        "Programming",
        "ML & AI",
        "Web Development",
        "General CS"
    ] = Field(
        description="The category that best matches the user's question."
    )

    key_points: List[str] = Field(
        default_factory=list,
        description="Important points. Use when the topic benefits from bullet points."
    )

    code: Optional[str] = Field(
        default=None,
        description="Code example only when code is useful or requested. Otherwise null."
    )

    example: Optional[str] = Field(
        default=None,
        description="A practical example when useful. Otherwise null."
    )

    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="Confidence that the selected category is correct."
    )



