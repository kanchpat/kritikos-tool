# Claude Code vs Gemini CLI — Feature Comparison

> Last updated: 2026-02-21

## Scorecard

| # | Category | Claude Code | Gemini CLI | Winner |
|---|---|---|---|---|
| 1 | Setup & Configuration | 7 | 9 | Gemini CLI |
| 2 | Supported Models & Providers | 8 | 8 | Tie |
| 3 | Code Editing | 7 | 9 | Gemini CLI |
| 4 | Context Management | 7 | 9 | Gemini CLI |
| 5 | Tool / MCP Support | 9 | 8 | Claude Code |
| 6 | IDE Integrations | 9 | 7 | Claude Code |
| 7 | Agentic Capabilities | 9 | 8 | Claude Code |
| 8 | Skills / Custom Commands | 7 | 9 | Gemini CLI |
| 9 | Extensibility | 6 | 9 | Gemini CLI |
| 10 | Pricing / Token Usage | 6 | 9 | Gemini CLI |
| 11 | Platform Support | 7 | 9 | Gemini CLI |
| 12 | Open Source | 8 | 8 | Tie |
| | **Total** | **90** | **102** | |

---

## 1. Setup & Configuration — Claude Code: 7 | Gemini CLI: 9 :white_check_mark:

| Feature | Claude Code | Gemini CLI |
|---|---|---|
| **Install** | `npm install -g @anthropic-ai/claude-code` | `npm install -g @google/gemini-cli` |
| **Runtime** | Node.js 18+ | Node.js 20+ |
| **Project context file** | `CLAUDE.md` | `GEMINI.md` |
| **Settings file** | `~/.claude/settings.json` | `~/.gemini/settings.json` |
| **Project settings** | `.claude/settings.json` | `.gemini/settings.json` |
| **System settings** | — | `/etc/gemini-cli/settings.json` |
| **Settings format** | JSON | JSON |
| **Settings hierarchy** | User → Project | System → User → Project → CLI args |
| **.env support** | Via tools / manual | Auto-loads `.env` (walks up directories) |
| **Auth** | Anthropic API key or OAuth | Google OAuth, API key, or Vertex AI |

**Notes**: Gemini CLI has a deeper settings hierarchy (4 levels vs 2). Both tools support nested context files at any directory level for scoped instructions — CLAUDE.md and GEMINI.md can be placed in subdirectories for component-specific context. Gemini CLI also supports a global `~/.gemini/GEMINI.md` and automatically discovers context files when tools access new directories (up to 200 dirs, configurable).

---

## 2. Supported Models & Providers — Claude Code: 8 | Gemini CLI: 8 (Tie)

| Feature | Claude Code | Gemini CLI |
|---|---|---|
| **Default model** | Claude Sonnet 4.5 | Gemini 2.5 Flash |
| **Top-tier model** | Claude Opus 4.6 | Gemini 3 Pro |
| **Fast model** | Claude Haiku 4.5 | Gemini 3 Flash |
| **Model switching** | `/model` command, `--model` flag | `--model` flag |
| **Third-party providers** | Amazon Bedrock, Google Vertex AI (for Claude models) | Vertex AI |
| **Model-agnostic** | Claude models only | Gemini models only |
| **Output token limit** | 64K (Opus/Sonnet) | 64K (2.5 Pro/Flash) |

**Notes**: Both are locked to their respective model families. Claude Code can route through Bedrock or Vertex but still uses Claude models. Gemini CLI is Gemini-only. Neither is truly model-agnostic for the core agent.

---

## 3. Code Editing — Claude Code: 7 | Gemini CLI: 9 :white_check_mark:

| Feature | Claude Code | Gemini CLI |
|---|---|---|
| **Edit mechanism** | Exact string match + replace | Text replacement with multi-stage correction |
| **Multi-file edits** | Yes — parallel tool calls | Yes |
| **Diff view** | Terminal diff output | Terminal diff + VS Code native diffs |
| **Undo** | No built-in undo (use git) | `/undo` command restores pre-edit state |
| **Back** | — | `/back` navigates conversation history |
| **File creation** | Write tool | WriteFile tool |
| **File reading** | Read tool | ReadFile tool |
| **Search (content)** | Grep tool (ripgrep-based) | Grep-like search |
| **Search (files)** | Glob tool | FindFiles (glob) |

**Notes**: Gemini CLI's `/undo` is a notable UX advantage — it restores files to their state before the last tool execution without needing git. Claude Code's edit tool requires exact string matching which is more precise but can fail if the match isn't unique. Gemini CLI's replace tool has a built-in retry mechanism that iteratively refines patterns.

---

## 4. Context Management — Claude Code: 7 | Gemini CLI: 9 :white_check_mark:

| Feature | Claude Code | Gemini CLI |
|---|---|---|
| **Context window** | 200K tokens | 1M tokens |
| **Compression** | Auto-compresses older messages | Summary replacement at 60% usage |
| **Ignore file** | `.claudeignore` | `.geminiignore` |
| **Codebase indexing** | On-demand exploration | On-demand exploration |
| **Memory persistence** | Auto-memory directory (`~/.claude/projects/`) | Via GEMINI.md |
| **Clear context** | `/clear` | `/clear` |
| **Summarize** | Automatic | `/summarize` manual command |
| **File includes** | Read tool | `@` includes for specific files |

**Notes**: Gemini CLI's 1M token context window is 5x larger, allowing it to hold significantly more codebase context in a single session. Claude Code compensates with auto-memory that persists across sessions and aggressive smart compression. Gemini CLI's `/summarize` gives explicit control over when to compress.

---

## 5. Tool / MCP Support — Claude Code: 9 :white_check_mark: | Gemini CLI: 8

| Feature | Claude Code | Gemini CLI |
|---|---|---|
| **Built-in tools** | Read, Write, Edit, Glob, Grep, Bash, WebSearch, WebFetch | ReadFile, WriteFile, Replace, FindFiles, ListDir, Shell, GoogleSearch |
| **MCP support** | Yes — full MCP client | Yes — full MCP client |
| **MCP config location** | `~/.claude/settings.json` or project settings | `~/.gemini/settings.json` or project settings |
| **Custom tools** | Via MCP servers | Via MCP servers |
| **Tool permissions** | Granular allow/deny per tool | Permission prompts, `--yolo` for auto-approve |
| **Notebook support** | Yes (NotebookEdit tool) | — |

**Notes**: Both have robust MCP support for extending with custom tools. Claude Code has a more granular permission model with configurable allow/deny rules. Gemini CLI's `--yolo` mode is an all-or-nothing auto-approve. Claude Code includes dedicated notebook editing support.

---

## 6. IDE Integrations — Claude Code: 9 :white_check_mark: | Gemini CLI: 7

| Feature | Claude Code | Gemini CLI |
|---|---|---|
| **VS Code** | Yes — official extension | Yes — official Companion extension |
| **JetBrains** | Yes — official plugin | No |
| **Other IDEs** | Any terminal-based editor | Antigravity, Open VSX-compatible forks |
| **Diff viewing** | In-terminal | Native VS Code side-by-side diffs |
| **Selected text access** | Via IDE extension | Via VS Code Companion |
| **Workspace awareness** | Via IDE extension | Via VS Code Companion |

**Notes**: Claude Code has broader IDE support (JetBrains + VS Code). Gemini CLI's VS Code integration offers native in-editor diff viewing with the ability to modify diffs before accepting — a strong editing UX. Neither supports Vim/Neovim natively beyond terminal usage.

---

## 7. Agentic Capabilities — Claude Code: 9 :white_check_mark: | Gemini CLI: 8

| Feature | Claude Code | Gemini CLI |
|---|---|---|
| **Autonomous mode** | Yes — handles multi-step tasks | Yes — multi-step with tool chaining |
| **Sub-agents** | Task tool spawns specialized sub-agents | `/agents:run` launches separate CLI instances |
| **Agent types** | Built-in: Bash, Explore, Plan, general-purpose | Custom via extensions |
| **Planning mode** | Yes — dedicated plan mode with approval | Multi-step planning in conversation |
| **Parallel execution** | Parallel tool calls + background agents | Sub-agents run independently |
| **Auto-approve mode** | Configurable per-tool permissions | `--yolo` flag |

**Notes**: Claude Code has a more structured agent system with built-in specialized agent types (Explore, Plan, Bash). Gemini CLI's sub-agents are full CLI instances with their own context, which provides better isolation but more overhead. Claude Code's plan mode with explicit user approval is a unique workflow feature.

---

## 8. Skills / Custom Commands — Claude Code: 7 | Gemini CLI: 9 :white_check_mark:

| Feature | Claude Code | Gemini CLI |
|---|---|---|
| **Slash commands** | `/help`, `/clear`, `/model`, `/compact`, `/cost`, etc. | `/tools`, `/summarize`, `/copy`, `/undo`, `/back`, `/clear`, `/stats`, `/mcp` |
| **Custom commands** | Skills system (user-invocable skills) | Custom slash commands via `.toml` files |
| **Command definition** | Skill definitions in settings/extensions | TOML files in `.gemini/commands/` |
| **Namespacing** | Skill names | Directory-based (e.g., `git/commit.toml` → `/git:commit`) |
| **Command locations** | Project or global | User (`~/.gemini/commands/`), Project (`.gemini/commands/`), MCP prompts, Extensions |
| **Hot reload** | — | Yes — reload without CLI restart |
| **Notable built-in** | `/commit`, `/review-pr`, `/init` | `/copy`, `/undo`, `/back`, `/stats` |

**Notes**: Gemini CLI's TOML-based custom command system with directory namespacing is more structured and discoverable. Claude Code's skill system is tied to its extension/settings model. Gemini CLI's `/undo` and `/back` are unique navigation commands. Claude Code's `/commit` and `/review-pr` are unique developer workflow commands.

---

## 9. Extensibility — Claude Code: 6 | Gemini CLI: 9 :white_check_mark:

| Feature | Claude Code | Gemini CLI |
|---|---|---|
| **Hooks system** | Yes — shell commands on tool events | Yes — BeforeTool, AfterTool, lifecycle events |
| **Hook events** | Tool-specific (PreToolUse, PostToolUse, etc.) | 10+ events: BeforeTool, AfterTool, SessionStart, PreCompress, BeforeModel, etc. |
| **Extensions** | MCP servers + settings | Full extension system (prompts, MCP, commands, hooks, sub-agents, skills) |
| **Extension registry** | — | geminicli.com/extensions/ |
| **Extension install** | Manual MCP config | `gemini extensions install <url>` |
| **Plugin system** | — | npm-based plugins with dependency injection |

**Notes**: Gemini CLI has a significantly more mature extension ecosystem with a registry, install CLI, and packaged extensions that bundle multiple capabilities. Claude Code's extensibility is primarily through MCP servers and hooks — functional but less packaged. Gemini CLI's hook system covers more lifecycle events (10+ vs ~4).

---

## 10. Pricing / Token Usage — Claude Code: 6 | Gemini CLI: 9 :white_check_mark:

| Feature | Claude Code | Gemini CLI |
|---|---|---|
| **Free tier** | Limited (with Anthropic account) | 60 req/min, 1,000 req/day (Google account) |
| **Subscription** | Claude Pro/Team/Enterprise ($20+/mo) | Google AI Ultra subscription |
| **API pricing** | Pay-per-token (varies by model) | Pay-per-token (varies by model) |
| **Token caching** | Prompt caching (automatic) | Built-in token caching |
| **Cost tracking** | `/cost` command | `/stats` command |
| **Usage limits** | Varies by plan | Varies by auth method |

**Notes**: Gemini CLI's free tier is notably generous — 1,000 requests/day with a Google account and no credit card. Claude Code requires a paid plan or API key for meaningful usage. Both offer pay-per-token API access for developers.

---

## 11. Platform Support — Claude Code: 7 | Gemini CLI: 9 :white_check_mark:

| Feature | Claude Code | Gemini CLI |
|---|---|---|
| **macOS** | Yes | Yes (10.15+) |
| **Linux** | Yes | Yes (Ubuntu 18.04+) |
| **Windows** | WSL2 required | Native Windows support |
| **Shell support** | Bash, Zsh | Bash, Zsh, PowerShell |
| **Min Node.js** | 18+ | 20+ |
| **Min RAM** | — | 512MB |
| **Min disk** | — | 100MB |
| **Cloud pre-installed** | — | Google Cloud Shell, Cloud Workstations |

**Notes**: Gemini CLI has native Windows support, which is a significant advantage for Windows developers. Claude Code requires WSL2 on Windows. Gemini CLI is pre-installed on Google Cloud environments.

---

## 12. Open Source — Claude Code: 8 | Gemini CLI: 8 (Tie)

| Feature | Claude Code | Gemini CLI |
|---|---|---|
| **License** | Apache 2.0 | Apache 2.0 |
| **Repository** | github.com/anthropics/claude-code | github.com/google-gemini/gemini-cli |
| **Language** | TypeScript | TypeScript |
| **Community** | GitHub Issues | GitHub Issues |

**Notes**: Both are open source under the same Apache 2.0 license. Both are built with TypeScript/Node.js.

---

## Quick Reference Summary

**Final Score: Claude Code 90 vs Gemini CLI 102**

| Category | Claude Code | Gemini CLI | Winner |
|---|---|---|---|
| Setup & Configuration | 7 | 9 | :white_check_mark: Gemini CLI |
| Models & Providers | 8 | 8 | Tie |
| Code Editing | 7 | 9 | :white_check_mark: Gemini CLI |
| Context Management | 7 | 9 | :white_check_mark: Gemini CLI |
| Tool / MCP Support | 9 | 8 | :white_check_mark: Claude Code |
| IDE Integrations | 9 | 7 | :white_check_mark: Claude Code |
| Agentic Capabilities | 9 | 8 | :white_check_mark: Claude Code |
| Skills / Custom Commands | 7 | 9 | :white_check_mark: Gemini CLI |
| Extensibility | 6 | 9 | :white_check_mark: Gemini CLI |
| Pricing / Token Usage | 6 | 9 | :white_check_mark: Gemini CLI |
| Platform Support | 7 | 9 | :white_check_mark: Gemini CLI |
| Open Source | 8 | 8 | Tie |
| **Total** | **90** | **102** | |

**Claude Code wins**: Tool/MCP Support, IDE Integrations, Agentic Capabilities (3 categories)
**Gemini CLI wins**: Setup, Code Editing, Context, Skills, Extensibility, Pricing, Platform (7 categories)
**Tie**: Models & Providers, Open Source (2 categories)
