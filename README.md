# Kritikos Tool 🛠️

> **kritikos** (*Greek*: κριτικός) – relating to judging; fit for judging; able to discern.

`Kritikos Tool` is an open-source evaluation suite designed to benchmark, compare, and analyze the capabilities of modern AI-powered tools. The tools can vary based on the use case. 

This repository provides developers with a transparent, reproducible framework to understand which AI tools excel at specific tasks, from low-level bug fixes to large-scale codebase refactoring.

---

## 🔎 Benchmarking Framework

We evaluate tools based on their performance across several critical dimensions:

To name a few

- **Context Window Management**: How effectively the tool handles large codebases (200K vs 1M+ tokens).
- **Edit Reliability**: The accuracy of the tool's rewrite logic (Exact string matching vs. multi-stage pattern correction).
- **Agentic Capabilities**: The ability to plan, execute, and verify multi-step tasks autonomously.
- **Workflow Integration**: Support for git, IDEs, and developer-specific commands (`/commit`, `/undo`, etc.).
- **Extensibility**: Support for Model Context Protocol (MCP) and custom tool/command systems.

---

## 📊 Comparison Reports

We maintain detailed side-by-side reports for different toolsets:

- **[Claude Code vs. Gemini CLI](./comparisons/claude-vs-gemini/comparison.md)**: A deep dive into the two current leading AI coding CLI tools.

### Video Demos

| Demo | Description | Video |
|---|---|---|
| Bug Fix Challenge | Both tools fix 3 bugs in an Express.js API | [Watch on YouTube](<!-- TODO: add link -->) |
| Multi-File Refactor | Refactoring duplicated auth code in a Flask app | [Watch on YouTube](<!-- TODO: add link -->) |
| Greenfield Feature | Adding features + tests to a TODO API | [Watch on YouTube](<!-- TODO: add link -->) |
| Codebase Q&A | Explaining an auth flow in a React + Express app | [Watch on YouTube](<!-- TODO: add link -->) |

---

## 🛠️ How to Use

1.  **Clone the Repo**
    ```bash
    git clone https://github.com/kanchpat/kritikos-tool.git
    cd kritikos-tool
    ```

2.  **Select a Test Case**
    Navigate to a sub-folder in `tests/`.

3.  **Run Your Tool**
    Initialize your AI agent (e.g., `claude` or `gemini`) and ask it to solve the challenge described in that folder's `README.md`.

4.  **Compare Results**
    Evaluate the tool's approach against our criteria and existing reports.

---

## 🚀 Contributing

This is a living project. We welcome:
- New **Test Cases** (different stacks or harder problems).
- New **Tool Comparisons** (Bedrock, Vertex AI, Azure Foundry, etc.).
- Bug reports on existing test apps.

---

*Last Updated: February 2026*
