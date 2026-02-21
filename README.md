# Kritikos Tool 🛠️

> **kritikos** (*Greek*: κριτικός) – relating to judging; fit for judging; able to discern.

`Kritikos Tool` is an open-source evaluation suite designed to benchmark, compare, and analyze the capabilities of modern AI-powered coding CLI tools. This repository currently focuses on a side-by-side comparison between **Claude Code** and **Gemini CLI**.

The goal of this project is to provide developers with a transparent, reproducible way to understand which tools excel at specific tasks, from simple bug fixes to complex codebase refactors.

---

## 📊 Feature Comparison At-a-Glance

| Dimension | Claude Code Strength | Gemini CLI Strength |
|---|---|---|
| **Context Size** | 200K tokens | **1M tokens (5x larger)** |
| **Pricing** | API Costs / Pro Plan | **1,000 req/day FREE** |
| **IDE Support** | JetBrains + VS Code | Native VS Code Diffs |
| **Platform** | macOS, Linux, WSL2 | **Native Windows Support** |
| **Workflow** | Built-in `/commit`, `/review-pr` | Useful `/undo`, `/back` navigation |
| **Extensibility** | MCP Servers | Extension Registry + CLI |
| **Edit Logic** | Exact String Matching | Auto-retry Pattern Matching |

For a deep dive into the 12+ categories of comparison, see our [Full Comparison Document](./comparison.md).

---

## 🧪 The Benchmarking Suite

We test tools against real-world scenarios in the `tests/` directory:

| Test Case | Description | Tech Stack |
|---|---|---|
| **[Bug Fix](./tests/bugfix-app)** | Identification and resolution of logical and syntax errors. | Express.js |
| **[Multi-File Refactor](./tests/refactor-app)** | Abstracting duplication into decorators and externalizing config. | Flask (Python) |
| **[Greenfield Feature](./tests/todo-api)** | Adding new models, endpoints, and unit tests from scratch. | Node.js |
| **[Codebase Q&A](./tests/complex-app)** | Generating end-to-end architectural explanations. | React + Express |

---

## 🚀 Useful Applications & Findings

### What works best?
*   **For Large Codebases:** **Gemini CLI**'s 1M token window allows it to "see" entire monolithic structures that trip up smaller context windows.
*   **For Precise Workflow:** **Claude Code**'s integration with Git (`/commit`) and its structured "Plan Mode" make it feel more like a surgical instrument for professional developers.
*   **For Rapid Experimentation:** **Gemini CLI**'s `/undo` command is a game-changer, allowing you to roll back AI-generated changes instantly without cluttering your git history.
*   **For Windows Developers:** **Gemini CLI** provides a first-class native experience, whereas Claude Code currently requires WSL2.

### Recommendations
- **Use Claude Code** if you are on macOS/Linux, use JetBrains IDEs, and want a highly opinionated, "agentic" workflow that handles your commits and PR reviews.
- **Use Gemini CLI** if you need a huge context window, prefer native VS Code diffing, want a generous free tier, or are developing natively on Windows.

---

## 🎥 Video Walkthrough
We've prepared a side-by-side comparison script for a video demonstration of these tools in action. Check out the [Script here](./script.md).

---

## 🛠️ Getting Started

1.  **Clone the Repo**
    ```bash
    git clone https://github.com/kanchana/kritikos-tool.git
    cd kritikos-tool
    ```

2.  **Run the Tests**
    Navigate to any directory in `tests/` and use your preferred CLI tool to solve the challenges described in the local `README.md` files.

3.  **Contribute**
    Find a new tool or an interesting test case? Open a PR!

---

*Last Updated: February 2026*
