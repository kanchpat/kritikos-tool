#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TF_DIR="$SCRIPT_DIR/../terraform"
DOCS_DIR="$SCRIPT_DIR/../../docs"

echo "=============================================="
echo "  Bedrock RAG FAQ Bot — Setup"
echo "=============================================="
echo ""
echo "PREREQUISITE: Enable model access in the AWS Bedrock console."
echo "  1. Open https://console.aws.amazon.com/bedrock/home#/modelaccess"
echo "  2. Click 'Manage model access'"
echo "  3. Enable:"
echo "     - Anthropic > Claude 3.5 Sonnet v2"
echo "     - Amazon > Titan Text Embeddings V2"
echo "  4. Click 'Save changes' and wait for access to be granted."
echo ""
read -rp "Press Enter once model access is enabled to continue..."

# --- Terraform ---
echo ""
echo ">> Running Terraform..."
cd "$TF_DIR"
terraform init
terraform apply

# --- Upload docs to S3 ---
BUCKET_NAME=$(terraform output -raw s3_bucket_name)
KB_ID=$(terraform output -raw knowledge_base_id)
GUARDRAIL_ID=$(terraform output -raw guardrail_id)
DATA_SOURCE_ID=$(aws bedrock-agent list-data-sources \
  --knowledge-base-id "$KB_ID" \
  --query 'dataSourceSummaries[0].dataSourceId' \
  --output text)

echo ""
echo ">> Uploading docs to s3://$BUCKET_NAME/ ..."
if [ -d "$DOCS_DIR" ]; then
  aws s3 sync "$DOCS_DIR" "s3://$BUCKET_NAME/" --delete
else
  echo "WARNING: Docs directory not found at $DOCS_DIR"
  echo "         Upload your FAQ documents to s3://$BUCKET_NAME/ manually."
fi

# --- Trigger ingestion ---
echo ""
echo ">> Starting Knowledge Base ingestion job..."
aws bedrock-agent start-ingestion-job \
  --knowledge-base-id "$KB_ID" \
  --data-source-id "$DATA_SOURCE_ID"

echo ""
echo "=============================================="
echo "  Setup complete!"
echo "=============================================="
echo ""
echo "Run the FAQ bot with:"
echo ""
echo "  export KNOWLEDGE_BASE_ID=$KB_ID"
echo "  export GUARDRAIL_ID=$GUARDRAIL_ID"
echo "  python app.py"
echo ""
