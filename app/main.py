from fastapi import FastAPI, HTTPException

from app.schemas import ChatRequest, ChatResponse

from app.guardrails import (
    validate_input,
    contains_pii,
    validate_output
)

from app.policy_engine import validate_policy

from app.groq_client import generate_response

app = FastAPI(
    title="LLM Guardrails Gateway",
    version="1.0.0"
)

@app.get("/")
def home():

    return {
        "message": "LLM Guardrails Gateway Running"
    }

@app.post("/chat", response_model=ChatResponse)

def chat(request: ChatRequest):

    message = request.message

    valid, reason = validate_input(message)

    if not valid:

        raise HTTPException(
            status_code=400,
            detail=reason
        )

    if contains_pii(message):

        raise HTTPException(
            status_code=400,
            detail="PII detected in input"
        )

    response = generate_response(message)

    if not validate_output(response):

        response = "Unsafe output blocked"

    if not validate_policy(response):

        response = "Policy violation detected"

    return {
        "response": response,
        "status": "success"
    }