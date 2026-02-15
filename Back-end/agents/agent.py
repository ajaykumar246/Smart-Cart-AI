
import os
from dotenv import load_dotenv
from typing import TypedDict, List, Dict, Literal
from pydantic import BaseModel, Field

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END


load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3
)

class TripContext(BaseModel):
    destination: str
    climate: Literal["cold", "hot", "moderate", "rainy"]
    duration: int
    trip_type: str
    intensity: str
    budget: int

class CategoryPlan(BaseModel):
    categories: List[str]


class BudgetSplit(BaseModel):
    allocation: Dict[str, int]


class AdjustmentIntent(BaseModel):
    action: Literal["remove", "replace", "reduce"]
    target: str
    value: str