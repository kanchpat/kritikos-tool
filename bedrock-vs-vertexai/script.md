# Video Script — Amazon Bedrock vs Google Vertex AI

## Setup
- Two browser windows side-by-side: AWS Console (left), GCP Console (right)
- Same AWS and GCP accounts with equivalent permissions
- Screen recording at 1080p or higher

---

## Segment 1: Introduction (1-2 min)
- Brief intro: "Comparing the two leading cloud AI platforms for enterprise GenAI"
- Show each console landing page (Bedrock, Vertex AI)
- Mention both are fully managed, multi-model platforms

---

## Segment 2: Model Catalog (2-3 min)

**What to show**:
- Bedrock Model Catalog — available models, one-click access, Anthropic use-case submission flow
- Vertex AI Model Garden — model browsing, Gemini models, open model selection

**Talking points**:
- Bedrock has more providers immediately available
- Vertex AI has Gemini family advantage + 100+ open models in Model Garden
- Both require manual console steps for initial model access

---

## Segment 3: Deploy & Invoke (3-4 min)

**What to show**:
- Bedrock: On-demand invocation via playground, provisioned throughput setup
- Vertex AI: Vertex AI Studio playground, endpoint creation

**Talking points**:
- Serverless is default on both — no infra to manage
- Bedrock PT is Terraform-manageable; Vertex AI PT requires console/gcloud
- Show the API call difference (InvokeModel vs GenerateContent)

---

## Segment 4: RAG / Knowledge Bases (4-5 min)

**What to show**:
- Bedrock: Create Knowledge Base → select S3 data source → choose vector store → test retrieval
- Vertex AI: Create RAG corpus → upload documents → test retrieval

**Talking points**:
- Bedrock has more data source connectors (Confluence, SharePoint, Salesforce)
- Bedrock KB is fully Terraform-manageable; Vertex RAG Engine is not
- Bedrock supports multimodal RAG (images, audio, video)
- Vertex AI's RagManagedDb needs zero provisioning

---

## Segment 5: Guardrails & Safety (3-4 min)

**What to show**:
- Bedrock: Create Guardrail → configure content filters, PII rules, topic blocking → test
- Vertex AI: Configure safety filters in API request / console

**Talking points**:
- Bedrock guardrails = single Terraform resource with 6 policy types
- Vertex AI safety filters are per-request API parameters (no Terraform resource)
- Bedrock PII handling: block vs anonymize
- Highlight: "This is where IaC differences are most visible"

---

## Segment 6: Agents (3-4 min)

**What to show**:
- Bedrock: Create Agent → define action groups → test in console
- Vertex AI: Show ADK code → Agent Designer visual canvas

**Talking points**:
- Bedrock agents are fully Terraform-managed (agent, alias, action groups)
- Vertex AI ADK is code-first, open source, but deployment is manual
- Vertex AI Agent Designer is unique — visual drag-and-drop that exports to code
- Multi-agent patterns on both sides

---

## Segment 7: Terraform / IaC Demo (4-5 min)

**What to show**:
- Side-by-side Terraform files:
  - Bedrock: agent + guardrail + knowledge base in ~50 lines of HCL
  - Vertex AI: endpoint + index in HCL, then manual steps for guardrails/agents
- Show `terraform plan` output for both
- Highlight what's missing on Vertex AI side

**Talking points**:
- "This is the key differentiator for DevOps teams"
- Bedrock: full GenAI stack is IaC-ready
- Vertex AI: infrastructure is IaC-ready, but GenAI features need console/API
- Show the IaC reference table from comparison.md

---

## Segment 8: Enterprise Security (2-3 min)

**What to show**:
- Bedrock: PrivateLink VPC endpoint setup
- Vertex AI: VPC Service Controls perimeter

**Talking points**:
- Both support private connectivity (no public internet)
- Both support CMEK encryption
- Bedrock has GovCloud; Vertex AI has confidential computing
- Both VPC setups are Terraform-manageable

---

## Segment 9: Wrap-Up (1-2 min)

- Summary table on screen (Quick Reference from comparison.md)
- "Choose Bedrock if: full IaC automation, GovCloud, broad model selection"
- "Choose Vertex AI if: Gemini models, visual agent design, confidential computing"
- Link to full comparison doc

---

## Total Estimated Runtime: 25-35 min

## Tips for Recording
- Use split-screen with clear labels (AWS / GCP)
- Keep console zoom at 100-125% for readability
- Pre-create resources where setup takes time (e.g., vector stores)
- Have Terraform files ready to show, not type live
- Blur any account IDs, keys, or sensitive info
