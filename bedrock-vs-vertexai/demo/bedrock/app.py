"""Bedrock RAG FAQ Bot — interactive CLI using Knowledge Bases for RAG."""

import os
import sys
import json

import boto3
from botocore.exceptions import ClientError

REGION = os.environ.get("AWS_REGION", "us-east-1")
KNOWLEDGE_BASE_ID = os.environ.get("KNOWLEDGE_BASE_ID")
GUARDRAIL_ID = os.environ.get("GUARDRAIL_ID")
MODEL_ARN = (
    "arn:aws:bedrock:us-east-1::foundation-model/"
    "anthropic.claude-3-5-sonnet-20241022-v2:0"
)


def build_request(question: str, session_id: str | None) -> dict:
    """Build the retrieve_and_generate request payload."""
    config = {
        "type": "KNOWLEDGE_BASE",
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": KNOWLEDGE_BASE_ID,
            "modelArn": MODEL_ARN,
            "retrievalConfiguration": {
                "vectorSearchConfiguration": {"numberOfResults": 5}
            },
        },
    }
    request = {"input": {"text": question}, "retrieveAndGenerateConfiguration": config}
    if session_id:
        request["sessionId"] = session_id
    if GUARDRAIL_ID:
        config["knowledgeBaseConfiguration"]["guardrailConfiguration"] = {
            "guardrailId": GUARDRAIL_ID,
            "guardrailVersion": "DRAFT",
        }
    return request


def print_response(response: dict) -> None:
    """Print the generated answer and any source citations."""
    output = response.get("output", {})
    print(f"\n  Answer: {output.get('text', '(no answer)')}\n")

    citations = response.get("citations", [])
    if citations:
        print("  Sources:")
        seen = set()
        for citation in citations:
            for ref in citation.get("retrievedReferences", []):
                loc = ref.get("location", {}).get("s3Location", {}).get("uri", "")
                if loc and loc not in seen:
                    seen.add(loc)
                    print(f"    - {loc}")
        print()


def main() -> None:
    if not KNOWLEDGE_BASE_ID:
        print("Error: KNOWLEDGE_BASE_ID environment variable is required.")
        sys.exit(1)

    client = boto3.client("bedrock-agent-runtime", region_name=REGION)
    session_id = None

    print("NovaCRM FAQ Bot (Bedrock RAG)")
    print("Type 'quit' or 'exit' to stop.\n")

    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not question or question.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        try:
            resp = client.retrieve_and_generate(**build_request(question, session_id))
            session_id = resp.get("sessionId", session_id)
            print_response(resp)
        except ClientError as exc:
            print(f"\n  AWS Error: {exc.response['Error']['Message']}\n")
        except Exception as exc:
            print(f"\n  Error: {exc}\n")


if __name__ == "__main__":
    main()
