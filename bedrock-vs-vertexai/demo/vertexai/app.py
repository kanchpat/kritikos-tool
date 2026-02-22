"""Vertex AI RAG FAQ Bot — interactive CLI using RAG Engine."""

import os
import sys

import vertexai
from vertexai.preview import rag
from vertexai.preview.generative_models import GenerativeModel, Tool


GCP_PROJECT = os.environ.get("GCP_PROJECT")
GCP_LOCATION = os.environ.get("GCP_LOCATION", "us-central1")
CORPUS_NAME = os.environ.get("CORPUS_NAME")

MODEL_ID = "gemini-2.0-flash"


def create_rag_tool(corpus_name: str) -> Tool:
    """Create a retrieval tool backed by the RAG corpus."""
    rag_resource = rag.RagResource(rag_corpus=corpus_name)
    rag_retrieval_tool = Tool.from_retrieval(
        retrieval=rag.Retrieval(
            source=rag.VertexRagStore(
                rag_resources=[rag_resource],
                similarity_top_k=5,
                vector_distance_threshold=0.5,
            ),
        )
    )
    return rag_retrieval_tool


def main() -> None:
    if not GCP_PROJECT:
        print("Error: GCP_PROJECT environment variable is required.")
        sys.exit(1)
    if not CORPUS_NAME:
        print("Error: CORPUS_NAME environment variable is required.")
        print("  Format: projects/{project}/locations/{location}/ragCorpora/{id}")
        sys.exit(1)

    # Initialize Vertex AI SDK
    vertexai.init(project=GCP_PROJECT, location=GCP_LOCATION)

    # Build RAG retrieval tool and model
    rag_tool = create_rag_tool(CORPUS_NAME)
    model = GenerativeModel(
        model_name=MODEL_ID,
        tools=[rag_tool],
        system_instruction=(
            "You are the NovaCRM FAQ assistant. Answer questions using only "
            "the retrieved context from the knowledge base. If the context does "
            "not contain the answer, say you don't know. Be concise and helpful."
        ),
    )

    print("NovaCRM FAQ Bot (Vertex AI RAG)")
    print("Type 'quit' or 'exit' to stop.\n")

    chat = model.start_chat()

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
            response = chat.send_message(question)
            answer = response.text if response.text else "(no answer)"
            print(f"\n  Answer: {answer}\n")

            # Print grounding sources if available
            if response.candidates and response.candidates[0].grounding_metadata:
                metadata = response.candidates[0].grounding_metadata
                chunks = getattr(metadata, "grounding_chunks", [])
                if chunks:
                    print("  Sources:")
                    for chunk in chunks:
                        source = getattr(chunk, "retrieved_context", None)
                        if source and getattr(source, "uri", None):
                            print(f"    - {source.uri}")
                    print()
        except Exception as exc:
            print(f"\n  Error: {exc}\n")


if __name__ == "__main__":
    main()
