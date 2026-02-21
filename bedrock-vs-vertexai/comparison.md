# Amazon Bedrock vs Google Vertex AI — Feature Comparison

> Last updated: 2026-02-21

---

## 1. Deployment

| Feature | Amazon Bedrock | Google Vertex AI |
|---|---|---|
| **Serverless inference** | Yes — on-demand, no infra management | Yes — fully managed for partner & open models |
| **Provisioned throughput** | Model Units (MUs), tokens/min | Generative AI Scale Units (GSUs) |
| **Commitment terms** | No commitment, 1-month, 6-month | Monthly/weekly fixed-cost subscriptions |
| **Endpoints** | Runtime endpoints via provisioned model ARN | Regional endpoints (preferred) + global endpoint |
| **Custom model hosting** | Yes — via Provisioned Throughput | Yes — custom containers on Vertex Endpoints |
| **Private endpoints** | AWS PrivateLink VPC endpoints | Private Service Connect (PSC) |
| **Invocation APIs** | InvokeModel, Converse, ConverseStream | Predict, GenerateContent, StreamGenerateContent |
| **Regions** | 15+ AWS regions | 10+ GCP regions; PT in us-central1, us-east4 |

**Terraform:**
| Resource | Bedrock | Vertex AI |
|---|---|---|
| Provisioned throughput | `aws_bedrock_provisioned_model_throughput` | Manual (console/gcloud) |
| Endpoints | Managed (no resource needed) | `google_vertex_ai_endpoint` |
| Custom model import | `aws_bedrock_custom_model` | `google_vertex_ai_model` |

**Notes**: Both offer serverless + provisioned options. Bedrock has more flexible commitment terms (including no-commitment provisioned). Vertex AI's regional endpoint approach gives more control over data residency. Bedrock provisioned throughput is Terraform-manageable; Vertex AI PT currently requires console or gcloud CLI.

---

## 2. Model Catalog

| Feature | Amazon Bedrock | Google Vertex AI |
|---|---|---|
| **First-party models** | Amazon Nova (lite, pro, micro, premier) | Gemini (2.5 Pro, 2.5 Flash, 3 Pro) |
| **Anthropic Claude** | Claude 3.5 Sonnet, 3 Haiku, Opus (requires use-case submission) | Claude 3.5 Haiku, 3 Haiku (MaaS) |
| **Meta Llama** | Llama 3.3+ | Llama 4+ (via Model Garden) |
| **Mistral** | Full lineup | Available via Model Garden |
| **Cohere** | Command, Command R+ | Limited |
| **Other providers** | DeepSeek, AI21 Jamba, Qwen, OpenAI GPT-OSS | DeepSeek, Qwen, GLM-4.7 |
| **Model marketplace** | Bedrock Model Catalog | Model Garden (100+ models) |
| **Fine-tuning** | Select models (Titan, Llama, Cohere) | Gemini, open models (supervised tuning) |
| **Model access** | Most immediate; Anthropic requires submission | GA for most; some in preview |

**Terraform:**
| Resource | Bedrock | Vertex AI |
|---|---|---|
| Model access enablement | Manual (console one-time) | Manual (console/API) |
| Fine-tuned models | `aws_bedrock_custom_model` | `google_vertex_ai_model` |
| Model evaluation | Manual | `google_vertex_ai_model_evaluation` |

**Notes**: Bedrock has broader immediate model availability across providers. Vertex AI's strength is the Gemini family (especially 2.5 Pro with 1M token context) and the Model Garden with 100+ open models. Both require manual console steps for initial model access enablement — this can't be fully automated.

---

## 3. Observability

| Feature | Amazon Bedrock | Google Vertex AI |
|---|---|---|
| **Monitoring** | CloudWatch Metrics | Cloud Monitoring (auto-collected) |
| **Logging** | CloudWatch Logs or S3 | Cloud Logging |
| **Tracing** | AWS X-Ray, OTEL via ADOT | Cloud Trace, OpenTelemetry |
| **Model invocation logging** | Full request/response to CloudWatch/S3 | Via Cloud Logging |
| **Agent dashboards** | AgentCore real-time dashboards | Agent Engine metrics |
| **Model monitoring** | — | Vertex AI Model Monitoring (drift, quality) |
| **Custom metrics** | CloudWatch custom metrics | Cloud Monitoring custom metrics |
| **Alerts** | CloudWatch Alarms | Cloud Monitoring alerting policies |
| **3rd party integrations** | Elastic, Langfuse, OpenObserve | Datadog, Elastic (via Cloud Monitoring) |

**Terraform:**
| Resource | Bedrock | Vertex AI |
|---|---|---|
| Logging config | `aws_bedrock_model_invocation_logging_configuration` | Manual (console/gcloud) |
| Monitoring alarms | `aws_cloudwatch_metric_alarm` | `google_monitoring_alert_policy` |
| Dashboards | `aws_cloudwatch_dashboard` | `google_monitoring_dashboard` |
| Model monitoring | — | `google_vertex_ai_model_monitoring_job` (partial) |

**Notes**: Both leverage their respective cloud monitoring stacks. Bedrock's model invocation logging is Terraform-configurable, which is a deployment advantage. Vertex AI adds model-level monitoring for drift detection and quality tracking, which Bedrock lacks. Both support OpenTelemetry for custom instrumentation.

---

## 4. Agents & Orchestration

| Feature | Amazon Bedrock | Google Vertex AI |
|---|---|---|
| **Agent service** | Bedrock Agents + AgentCore (managed deployment) | Agent Builder + Agent Engine (runtime) |
| **Agent framework** | Framework-agnostic (LangGraph, CrewAI, custom) | Agent Development Kit (ADK) — open source |
| **Orchestration** | ReAct (default) or custom Lambda orchestrator | Workflow agents (Sequential, Parallel, Loop) + LLM-driven routing |
| **Tool use** | Native FM tool use | Pre-built tools, MCP, LangChain/LlamaIndex tools |
| **Multi-agent** | Supervisor coordination pattern | Sub-agent delegation |
| **Visual design** | — | Agent Designer (low-code canvas, exports to ADK) |
| **Deployment** | AgentCore (managed scaling, security) | Agent Engine (managed runtime) |
| **Language support** | Python, JavaScript | Python, Java, Go |
| **Custom orchestration** | Lambda-based custom strategies | Custom agent classes in ADK |

**Terraform:**
| Resource | Bedrock | Vertex AI |
|---|---|---|
| Agent definition | `aws_bedrock_agent` | Manual (ADK code + deploy) |
| Agent alias | `aws_bedrock_agent_alias` | — |
| Action groups | `aws_bedrock_agent_action_group` | — |
| Agent Engine deployment | — | Manual (`gcloud` / ADK CLI) |

**Notes**: Bedrock Agents have stronger Terraform support — the full agent lifecycle (create, alias, action groups) can be IaC-managed. Vertex AI's ADK is code-first and open source, but deployment to Agent Engine is currently a manual/CLI process. Vertex AI's Agent Designer provides a visual design experience that Bedrock lacks. Bedrock's Lambda-based custom orchestration gives deep control for complex workflows.

---

## 5. RAG / Knowledge Bases

| Feature | Amazon Bedrock | Google Vertex AI |
|---|---|---|
| **Service** | Knowledge Bases for Amazon Bedrock | Vertex AI RAG Engine |
| **Workflow** | Auto: fetch → chunk → embed → store | Corpus-based: ingest → index → retrieve |
| **Data sources** | S3, Confluence, Salesforce, SharePoint, Web Crawler | Cloud Storage, Drive, URLs |
| **Vector stores** | OpenSearch Serverless, Aurora PostgreSQL, Pinecone, Redis, MongoDB, Neptune | RagManagedDb (default), Vertex Vector Search, Pinecone, Weaviate |
| **Multimodal RAG** | GA — text, images, audio, video | Text + images |
| **APIs** | RetrieveAndGenerate, Retrieve (retrieval-only) | RAG Engine API (corpus-based) |
| **Structured data** | Yes — structured data retrieval | Limited |
| **S3/GCS vector storage** | S3 Vectors (cost-optimized) | — |
| **Chunking strategies** | Fixed-size, semantic, hierarchical | Fixed-size, semantic |

**Terraform:**
| Resource | Bedrock | Vertex AI |
|---|---|---|
| Knowledge base | `aws_bedrock_knowledge_base` | Manual (API/console) |
| Data source | `aws_bedrock_data_source` | Manual (API/console) |
| Vector store (managed) | `aws_opensearchserverless_collection` | `google_vertex_ai_feature_online_store` (partial) |

**Notes**: Bedrock has significantly better Terraform coverage for RAG — knowledge bases and data sources are fully IaC-manageable. Bedrock also leads in multimodal RAG (audio/video) and enterprise data connectors (Confluence, SharePoint, Salesforce). Vertex AI's RagManagedDb requires zero provisioning but lacks IaC support. Both support third-party vector stores.

---

## 6. Guardrails & Safety

| Feature | Amazon Bedrock | Google Vertex AI |
|---|---|---|
| **Service** | Bedrock Guardrails | Safety Filters + Model Armor |
| **Content filtering** | 6 categories: Hate, Insults, Sexual, Violence, Misconduct, Prompt Attack | Configurable categories: Dangerous Content, Harassment, Hate Speech |
| **PII detection** | Predefined entities (SSN, email, phone, etc.) + custom regex | Auto-block for PII (non-configurable) |
| **PII actions** | BLOCK, ANONYMIZE, NONE | Block only |
| **Prompt injection** | Built-in detection | Integrated safeguards |
| **Hallucination detection** | Yes — factual grounding checks | Via grounding with Google Search |
| **Topic blocking** | Yes — deny specific topics | — |
| **Custom policies** | 6 safeguard policies in single resource | Configurable thresholds per harm category |
| **Safety scores** | — | 0-1 likelihood scores per category |

**Terraform:**
| Resource | Bedrock | Vertex AI |
|---|---|---|
| Guardrail definition | `aws_bedrock_guardrail` | Manual (console/API) |
| Guardrail version | `aws_bedrock_guardrail_version` | — |
| Safety filters | Part of guardrail resource | Per-request API parameter |
| CloudFormation | `AWS::Bedrock::Guardrail` | — |

**Notes**: Bedrock Guardrails are a standout for IaC — the entire guardrail (content filters, PII rules, topic blocking, word filters) is a single Terraform resource. Vertex AI safety filters are configured per-request or in the console, with no Terraform resource. Bedrock also offers more granular PII handling (anonymize vs block) and topic-level controls. Vertex AI's Model Armor is newer and adds brand safety alignment.

---

## 7. 3rd Party Integrations

| Feature | Amazon Bedrock | Google Vertex AI |
|---|---|---|
| **Python SDK** | `boto3` (Bedrock client) | `google-cloud-aiplatform`, `google-genai` |
| **JavaScript SDK** | `@aws-sdk/client-bedrock-runtime` | `@google-cloud/vertexai` |
| **LangChain** | `langchain-aws` (ChatBedrockConverse) | `langchain-google-vertexai` (migrating to `langchain-google-genai`) |
| **LlamaIndex** | `llama-index-llms-bedrock` | `llama-index-llms-vertex` |
| **OpenAI compatibility** | — | Yes — OpenAI-compatible endpoint for Gemini |
| **MCP support** | Via agents (tool use) | Full MCP client/server in ADK |
| **Framework-agnostic** | Yes — Strands, CrewAI, LangGraph | Yes — CrewAI, LangGraph, ADK |
| **Observability partners** | Langfuse, Elastic, OpenObserve | Datadog, Elastic |

**Terraform:**
| Resource | Bedrock | Vertex AI |
|---|---|---|
| SDK/integration setup | N/A (code-level) | N/A (code-level) |

**Notes**: Both have strong framework support. Vertex AI's OpenAI-compatible endpoint is notable — existing OpenAI code can switch to Gemini with a URL change. LangChain integration is mature on both sides but Vertex AI is consolidating from multiple packages to `langchain-google-genai`. SDK/integration setup is code-level for both — nothing to Terraform here.

---

## 8. IaC / Terraform — Comprehensive Reference

### Bedrock Terraform Resources (`hashicorp/aws` provider)

| Resource | Purpose | Status |
|---|---|---|
| `aws_bedrock_custom_model` | Import/create custom models | GA |
| `aws_bedrock_provisioned_model_throughput` | Provisioned throughput | GA |
| `aws_bedrock_model_invocation_logging_configuration` | Enable invocation logging | GA |
| `aws_bedrock_guardrail` | Create guardrails with all policies | GA |
| `aws_bedrock_guardrail_version` | Version guardrails | GA |
| `aws_bedrock_agent` | Define agents | GA |
| `aws_bedrock_agent_alias` | Agent versioning | GA |
| `aws_bedrock_agent_action_group` | Agent tools/actions | GA |
| `aws_bedrock_agent_knowledge_base_association` | Link agent to KB | GA |
| `aws_bedrock_knowledge_base` | Create knowledge bases | GA |
| `aws_bedrock_data_source` | Knowledge base data sources | GA |

**Official module**: `aws-ia/bedrock/aws` (Terraform Registry)
**CloudFormation**: `AWS::Bedrock::*` resources available

### Vertex AI Terraform Resources (`hashicorp/google` provider)

| Resource | Purpose | Status |
|---|---|---|
| `google_vertex_ai_endpoint` | Create/manage endpoints | GA |
| `google_vertex_ai_model` | Register models | GA |
| `google_vertex_ai_dataset` | Manage datasets | GA |
| `google_vertex_ai_featurestore` | Feature store | GA |
| `google_vertex_ai_feature_online_store` | Online feature serving | GA |
| `google_vertex_ai_index` | Vector search index | GA |
| `google_vertex_ai_index_endpoint` | Vector search endpoint | GA |
| `google_vertex_ai_tensorboard` | Experiment tracking | GA |

**Official module**: `GoogleCloudPlatform/vertex-ai/google` (published Jan 2026)
**Submodules**: agent-engine, feature-online-store, model-armor-floorsetting, workbench

### What Requires Manual Setup

| Capability | Bedrock | Vertex AI |
|---|---|---|
| **Model access enablement** | Console (one-time per model) | Console (one-time per model) |
| **Provisioned throughput** | Terraform | Console / gcloud CLI |
| **Guardrails** | Terraform | Console / API per-request |
| **Knowledge bases** | Terraform | Console / API |
| **Agents** | Terraform | Code (ADK) + manual deploy |
| **Agent deployment** | Terraform (via agent alias) | gcloud / ADK CLI |
| **Invocation logging** | Terraform | Console / gcloud |
| **Safety filters** | Terraform (part of guardrails) | API parameter per-request |
| **Fine-tuning jobs** | Manual (console/API) | Manual (console/API) |
| **Model evaluation** | Manual | Manual |

**Notes**: Bedrock has significantly deeper Terraform coverage — agents, guardrails, knowledge bases, and logging are all fully IaC-manageable. Vertex AI's Terraform support focuses on infrastructure (endpoints, indexes, feature stores) but generative AI features (guardrails, RAG, agents) largely require console or API setup. The Jan 2026 Vertex AI Terraform module update adds agent-engine and model-armor submodules, but these are still maturing. For teams that need full GitOps pipelines, Bedrock is more automation-ready today.

---

## 9. Pricing

| Feature | Amazon Bedrock | Google Vertex AI |
|---|---|---|
| **On-demand** | Pay-per-token (published rates) | Pay-per-token (published rates) |
| **Example: Claude 3.5 Sonnet** | $3.00/1M input, $15.00/1M output | Similar (MaaS pricing) |
| **Example: Llama 3** | $0.22/1M input, $0.22/1M output | Varies by region |
| **Provisioned throughput** | Hourly billing per MU (commitment discounts) | Fixed monthly/weekly per GSU |
| **Batch processing** | 50% discount vs on-demand | Available for select models |
| **Cost tracking** | AWS Cost Explorer, `/cost` tags | GCP Billing, Budget alerts |
| **Pricing transparency** | Published per-model rates | Requires pricing calculator for PT |
| **Free tier** | Limited free trial credits | $300 GCP free credits (new accounts) |

**Notes**: Bedrock is more transparent — per-model token rates are published directly. Vertex AI provisioned throughput pricing requires the pricing calculator. Both offer commitment discounts for provisioned capacity. Bedrock's 50% batch discount is significant for bulk workloads.

---

## 10. Enterprise & Security

| Feature | Amazon Bedrock | Google Vertex AI |
|---|---|---|
| **Private connectivity** | AWS PrivateLink (VPC interface endpoints) | Private Service Connect (PSC) |
| **Encryption at rest** | AWS KMS (customer-managed keys) | CMEK (customer-managed encryption keys) |
| **Encryption in transit** | TLS 1.2+ | TLS 1.2+ |
| **IAM** | AWS IAM policies + VPC endpoint policies | GCP IAM roles + VPC Service Controls |
| **Network isolation** | VPC endpoints, no public IP needed | VPC Service Controls perimeter (blocks all public) |
| **Compliance** | HIPAA, SOC 2, PCI DSS, FedRAMP | HIPAA (announced 2026 for Agent Engine), SOC 2, ISO |
| **Data residency** | Data stays in originating AWS Region | Data stays in selected GCP region |
| **Data privacy** | Customer data not used for training; not shared with providers | Customer data not used for training |
| **Confidential computing** | — | Yes — hardware-based ephemeral keys, TEE |
| **Audit logging** | CloudTrail | Cloud Audit Logs |
| **GovCloud** | Yes (AWS GovCloud regions) | — |

**Terraform:**
| Resource | Bedrock | Vertex AI |
|---|---|---|
| VPC endpoint | `aws_vpc_endpoint` (service: bedrock-runtime) | `google_compute_service_attachment` + PSC |
| KMS keys | `aws_kms_key` | `google_kms_crypto_key` |
| IAM policies | `aws_iam_policy` | `google_project_iam_binding` |
| Audit logging | `aws_cloudtrail` | `google_project_iam_audit_config` |

**Notes**: Both are enterprise-grade with private connectivity, CMEK, and compliance certifications. Bedrock has a longer compliance track record and GovCloud support for federal workloads. Vertex AI brings unique confidential computing with hardware-based TEEs for sensitive workloads. VPC-level security is fully Terraform-manageable on both platforms.

---

## Quick Reference Summary

| Dimension | Bedrock Strength | Vertex AI Strength |
|---|---|---|
| **Deployment** | Flexible commitment terms | Unified PT experience |
| **Model catalog** | Broader provider selection | Gemini family + Model Garden |
| **Observability** | Agent dashboards | Model drift monitoring |
| **Agents** | Full Terraform lifecycle | ADK open source + visual designer |
| **RAG** | Multimodal (audio/video) + enterprise connectors | Zero-config RagManagedDb |
| **Guardrails** | Fully Terraform-managed | Flexible per-request thresholds |
| **3rd party** | Mature LangChain | OpenAI-compatible endpoint |
| **Terraform/IaC** | Deep coverage (agents, KB, guardrails) | Infrastructure-focused, GenAI catching up |
| **Pricing** | Transparent published rates, 50% batch | Flexible PT subscriptions |
| **Enterprise** | GovCloud, mature compliance | Confidential computing |
