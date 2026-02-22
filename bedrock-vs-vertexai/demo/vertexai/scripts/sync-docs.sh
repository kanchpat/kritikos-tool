#!/usr/bin/env bash
# sync-docs.sh — Re-sync FAQ documents to GCS and re-import into RAG corpus.
#
# Use this after updating files in ../../docs/. Requires CORPUS_NAME env var
# (printed by setup.sh during initial provisioning).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TERRAFORM_DIR="$SCRIPT_DIR/../terraform"
DOCS_DIR="$SCRIPT_DIR/../../docs"

if [ -z "${CORPUS_NAME:-}" ]; then
    echo "Error: CORPUS_NAME environment variable is required."
    echo "  Format: projects/{project}/locations/{location}/ragCorpora/{id}"
    echo "  (printed by setup.sh during initial setup)"
    exit 1
fi

# Read outputs from Terraform state
BUCKET_NAME=$(terraform -chdir="$TERRAFORM_DIR" output -raw gcs_bucket_name)
PROJECT_ID=$(terraform -chdir="$TERRAFORM_DIR" output -raw project_id)
REGION=$(terraform -chdir="$TERRAFORM_DIR" output -raw region)

echo "=== Syncing documents to GCS ==="
echo "Bucket: gs://$BUCKET_NAME"
gsutil -m rsync "$DOCS_DIR" "gs://$BUCKET_NAME/"
echo "Documents synced."

echo ""
echo "=== Re-importing documents into RAG corpus ==="
echo "Corpus: $CORPUS_NAME"
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
print('Documents re-imported successfully')
"

echo ""
echo "Done. Documents are now up to date in the RAG corpus."
