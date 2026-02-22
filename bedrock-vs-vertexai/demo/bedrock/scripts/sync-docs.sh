#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TF_DIR="$SCRIPT_DIR/../terraform"
DOCS_DIR="$SCRIPT_DIR/../../docs"

cd "$TF_DIR"

BUCKET_NAME=$(terraform output -raw s3_bucket_name)
KB_ID=$(terraform output -raw knowledge_base_id)
DATA_SOURCE_ID=$(aws bedrock-agent list-data-sources \
  --knowledge-base-id "$KB_ID" \
  --query 'dataSourceSummaries[0].dataSourceId' \
  --output text)

echo ">> Syncing docs to s3://$BUCKET_NAME/ ..."
aws s3 sync "$DOCS_DIR" "s3://$BUCKET_NAME/" --delete

echo ">> Starting ingestion job..."
INGESTION_JOB=$(aws bedrock-agent start-ingestion-job \
  --knowledge-base-id "$KB_ID" \
  --data-source-id "$DATA_SOURCE_ID" \
  --output json)

JOB_ID=$(echo "$INGESTION_JOB" | python3 -c "import sys,json; print(json.load(sys.stdin)['ingestionJob']['ingestionJobId'])")
echo ">> Ingestion job started: $JOB_ID"
echo ">> Check status with:"
echo "   aws bedrock-agent get-ingestion-job --knowledge-base-id $KB_ID --data-source-id $DATA_SOURCE_ID --ingestion-job-id $JOB_ID"
