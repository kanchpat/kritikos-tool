terraform {
  required_version = ">= 1.5.0"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# --------------------------------------------------------------------------
# IMPORTANT: Vertex AI RAG Engine limitations with Terraform
#
# The following resources CANNOT be managed via Terraform and require the
# setup.sh script (which uses the Python vertexai SDK directly):
#
#   1. RAG Corpus creation  — no google_vertex_ai_rag_corpus resource exists
#   2. Document import      — no resource to import files into a corpus
#   3. Safety / grounding   — model-level config, not a Terraform resource
#
# Compare this with AWS Bedrock, where the Knowledge Base, data source,
# data sync, and guardrails are ALL managed declaratively via Terraform.
# --------------------------------------------------------------------------

# Enable required APIs
resource "google_project_service" "aiplatform" {
  service            = "aiplatform.googleapis.com"
  disable_on_destroy = false
}

resource "google_project_service" "storage" {
  service            = "storage.googleapis.com"
  disable_on_destroy = false
}

# GCS bucket to hold FAQ documents
resource "google_storage_bucket" "faq_docs" {
  name     = "${var.project_id}-${var.project_name}-docs"
  location = var.region

  uniform_bucket_level_access = true
  force_destroy               = true

  versioning {
    enabled = false
  }

  depends_on = [google_project_service.storage]
}

# Retrieve the project number for the Vertex AI service agent
data "google_project" "current" {
  project_id = var.project_id
}

# Grant the Vertex AI service agent read access to the GCS bucket
# so that RAG Engine can import documents from it.
resource "google_storage_bucket_iam_member" "vertex_ai_reader" {
  bucket = google_storage_bucket.faq_docs.name
  role   = "roles/storage.objectViewer"
  member = "serviceAccount:service-${data.google_project.current.number}@gcp-sa-aiplatform.iam.gserviceaccount.com"

  depends_on = [google_project_service.aiplatform]
}
