output "gcs_bucket_name" {
  description = "GCS bucket containing FAQ documents"
  value       = google_storage_bucket.faq_docs.name
}

output "project_id" {
  description = "GCP project ID"
  value       = var.project_id
}

output "region" {
  description = "GCP region"
  value       = var.region
}
