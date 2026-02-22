variable "region" {
  description = "AWS region for all resources"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Project name used for resource naming"
  type        = string
  default     = "novacrm-faq"
}

variable "environment" {
  description = "Deployment environment (e.g. demo, staging, prod)"
  type        = string
  default     = "demo"
}
