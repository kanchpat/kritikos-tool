# RAG FAQ Bot — Bedrock vs Vertex AI

A side-by-side deployment of the same FAQ bot on Amazon Bedrock and Google Vertex AI, demonstrating the real-world differences in infrastructure-as-code coverage, tooling, and developer experience.

Both bots answer questions about a fictional SaaS product (NovaCRM) using retrieval-augmented generation over the same set of FAQ documents.

## Architecture

```
User question
    │
    ▼
┌──────────┐     ┌──────────────┐     ┌──────────────┐
│  CLI App  │────▶│ Vector Search │────▶│  LLM Answer  │
└──────────┘     │ (retrieve)    │     │ (generate)   │
                 └──────────────┘     └──────────────┘
```

| Component | Bedrock | Vertex AI |
|---|---|---|
| Vector store | OpenSearch Serverless | RAG Engine (managed) |
| Embedding model | Titan Text Embeddings V2 | Gecko (auto, via RAG Engine) |
| Generation model | Claude 3.5 Sonnet v2 | Gemini 2.0 Flash |
| Guardrails | Bedrock Guardrails (content + PII + topics) | Safety settings (model-level) |
| RAG orchestration | Knowledge Bases `retrieve_and_generate` | RAG Engine retrieval tool + Gemini |

## IaC Coverage Comparison

This is the key takeaway: **Bedrock's GenAI features are fully Terraform-managed; Vertex AI's are not.**

| Resource | Bedrock | Vertex AI |
|---|---|---|
| Object storage (S3 / GCS) | Terraform | Terraform |
| API enablement | N/A (always on) | Terraform |
| IAM roles / bindings | Terraform | Terraform |
| Vector store | Terraform (OpenSearch Serverless) | N/A (managed by RAG Engine) |
| Knowledge base / RAG corpus | Terraform (`aws_bedrockagent_knowledge_base`) | **Shell script** (Python SDK) |
| Data source / doc import | Terraform (`aws_bedrockagent_data_source`) | **Shell script** (Python SDK) |
| Guardrails / safety | Terraform (`aws_bedrock_guardrail`) | **Code** (model-level config) |
| Ingestion sync | AWS CLI (`start-ingestion-job`) | **Shell script** (Python SDK) |

### By the numbers

| Metric | Bedrock | Vertex AI |
|---|---|---|
| Terraform lines | ~340 | ~70 |
| Shell script lines | ~65 | ~67 |
| Terraform resource count | 10 | 4 |
| Manual / imperative steps | 1 (enable model access) | 3 (corpus, import, safety) |

## Shared FAQ Documents

Both platforms ingest the same three markdown files from `docs/`:

- `product-faq.md` — What NovaCRM is, features, integrations, API
- `pricing-faq.md` — Plans, pricing, trials, refunds
- `support-faq.md` — Password reset, 2FA, bug reporting, SLA

## Quick Start

### Bedrock

```bash
cd bedrock
pip install -r requirements.txt
bash scripts/setup.sh        # Terraform + S3 upload + ingestion
export KNOWLEDGE_BASE_ID=... # from setup output
python app.py
```

### Vertex AI

```bash
cd vertexai
pip install -r requirements.txt
bash scripts/setup.sh        # Terraform + GCS upload + corpus + import
export GCP_PROJECT=...       # your project ID
export CORPUS_NAME=...       # from setup output
python3 app.py
```

See each subdirectory's README for full setup instructions.

## Cleanup

```bash
# Bedrock
cd bedrock/terraform && terraform destroy

# Vertex AI
cd vertexai/terraform && terraform destroy
# Note: RAG corpus must be deleted separately via gcloud or the console
```
