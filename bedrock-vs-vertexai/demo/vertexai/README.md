# Vertex AI RAG FAQ Bot

Interactive CLI FAQ bot powered by Vertex AI RAG Engine and Gemini 2.0 Flash.

## Prerequisites

- **Google Cloud SDK** (`gcloud`) installed and configured
- **Terraform** >= 1.5
- **Python** >= 3.9 with `pip`
- A GCP project with billing enabled

## What Terraform manages vs. what it doesn't

| Resource | Managed by |
|---|---|
| GCS bucket for documents | Terraform |
| API enablement (aiplatform, storage) | Terraform |
| IAM for Vertex AI service agent | Terraform |
| **RAG corpus creation** | **setup.sh (Python SDK)** |
| **Document import into corpus** | **setup.sh (Python SDK)** |
| **Safety / grounding filters** | **Model-level config in app.py** |

**Key difference from Bedrock:** In the Bedrock demo, the Knowledge Base, data
source, sync job, and guardrails are ALL managed declaratively via Terraform.
With Vertex AI, the RAG corpus and document import have no Terraform resources
and require imperative scripts using the Python SDK.

## Setup

### Step 1: Authenticate

```bash
gcloud auth login
gcloud auth application-default login
```

### Step 2: Configure Terraform

```bash
cd terraform
cp terraform.tfvars.example terraform.tfvars
# Edit terraform.tfvars with your project ID
```

### Step 3: Run setup script

```bash
pip install -r requirements.txt
chmod +x scripts/setup.sh
./scripts/setup.sh
```

This will:
1. Run `terraform apply` to create the GCS bucket and enable APIs
2. Upload FAQ docs to GCS
3. Create a RAG corpus (Python SDK — no Terraform resource exists)
4. Import documents into the corpus (Python SDK)

### Step 4: Run the bot

```bash
export GCP_PROJECT=your-project-id
export GCP_LOCATION=us-central1
export CORPUS_NAME=projects/.../locations/.../ragCorpora/...
python3 app.py
```

## Updating documents

After editing files in `../docs/`, re-sync with:

```bash
export CORPUS_NAME=projects/.../locations/.../ragCorpora/...
./scripts/sync-docs.sh
```
