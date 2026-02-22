#!/usr/bin/env bash
# setup.sh — Provision infrastructure and create the RAG corpus.
#
# Unlike the Bedrock demo where everything is Terraform-managed, Vertex AI
# RAG corpus creation and document import require the Python SDK because
# no Terraform resources exist for these operations.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TERRAFORM_DIR="$SCRIPT_DIR/../terraform"
DOCS_DIR="$SCRIPT_DIR/../../docs"

echo "=== Step 1: Terraform init & apply ==="
terraform -chdir="$TERRAFORM_DIR" init
terraform -chdir="$TERRAFORM_DIR" apply -auto-approve

# Read outputs
BUCKET_NAME=$(terraform -chdir="$TERRAFORM_DIR" output -raw gcs_bucket_name)
PROJECT_ID=$(terraform -chdir="$TERRAFORM_DIR" output -raw project_id)
REGION=$(terraform -chdir="$TERRAFORM_DIR" output -raw region)

echo ""
echo "=== Step 2: Upload FAQ documents to GCS ==="
echo "Bucket: gs://$BUCKET_NAME"
gsutil cp "$DOCS_DIR"/* "gs://$BUCKET_NAME/"
echo "Documents uploaded."

echo ""
echo "=== Step 3: Create RAG corpus (Python SDK — no Terraform resource) ==="
CORPUS_NAME=$(python3 -c "
from vertexai.preview import rag
import vertexai

vertexai.init(project='$PROJECT_ID', location='$REGION')
corpus = rag.create_corpus(display_name='novacrm-faq-corpus')
print(corpus.name)
")
echo "Corpus created: $CORPUS_NAME"

echo ""
echo "=== Step 4: Import documents into corpus (Python SDK) ==="
python3 -c "
from vertexai.preview import rag
import vertexai

vertexai.init(project='$PROJECT_ID', location='$REGION')
rag.import_files(
    '$CORPUS_NAME',
    ['gs://$BUCKET_NAME/'],
    chunk_size=512,
    chunk_overlap=100,
)
print('Documents imported successfully')
"

echo ""
echo "=========================================="
echo "Setup complete!"
echo ""
echo "Run the bot with:"
echo "  export GCP_PROJECT=$PROJECT_ID"
echo "  export GCP_LOCATION=$REGION"
echo "  export CORPUS_NAME=$CORPUS_NAME"
echo "  python3 app.py"
echo "=========================================="
