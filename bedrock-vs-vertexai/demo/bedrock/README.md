# Bedrock RAG FAQ Bot

A Python CLI FAQ bot that uses Amazon Bedrock Knowledge Bases for retrieval-augmented generation (RAG). FAQ documents are stored in S3, embedded into an OpenSearch Serverless vector store, and queried via Bedrock's `retrieve_and_generate` API with Claude 3.5 Sonnet as the generation model.

## Prerequisites

- **AWS CLI** configured with credentials (`aws configure`)
- **Terraform** >= 1.5
- **Python** >= 3.9
- An AWS account with access to the Bedrock service in `us-east-1`

## Setup

### Step 1 — Enable model access (manual)

Bedrock foundation models require explicit opt-in. Open the AWS console:

<https://console.aws.amazon.com/bedrock/home#/modelaccess>

1. Click **Manage model access**.
2. Enable **Anthropic > Claude 3.5 Sonnet v2** and **Amazon > Titan Text Embeddings V2**.
3. Click **Save changes** and wait for access status to show "Granted".

### Step 2 — Provision infrastructure and load documents

```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the setup script (Terraform + S3 upload + ingestion)
bash scripts/setup.sh
```

The setup script will:
- Run `terraform init` and `terraform apply` to create all AWS resources.
- Upload FAQ documents from `../../docs/` to the S3 bucket.
- Trigger a Knowledge Base ingestion job to index the documents.

### Step 3 — Run the FAQ bot

```bash
export KNOWLEDGE_BASE_ID=<knowledge_base_id from setup output>
export GUARDRAIL_ID=<guardrail_id from setup output>   # optional
python app.py
```

Type your questions at the prompt. The bot will retrieve relevant document chunks and generate an answer with source citations.

### Syncing updated documents

After adding or editing files in `../../docs/`, re-sync and re-index:

```bash
bash scripts/sync-docs.sh
```

## What Terraform manages

| Resource | Purpose |
|---|---|
| S3 bucket (versioned) | Stores FAQ source documents |
| OpenSearch Serverless collection | Vector store for document embeddings |
| OpenSearch access/encryption/network policies | Secures the collection |
| IAM role + policy | Grants Bedrock KB access to S3, OpenSearch, and models |
| Bedrock Knowledge Base | RAG orchestration |
| Bedrock Data Source | Connects the KB to the S3 bucket |
| Bedrock Guardrail | Content filtering, PII anonymization, topic blocking |

## What is manual

- Enabling foundation model access in the Bedrock console (Step 1).
- The OpenSearch vector index is created automatically by Bedrock during the first ingestion job.

## Cleanup

```bash
cd terraform
terraform destroy
```
