# Hermes Agent

A fork of [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) — an agentic AI assistant powered by Hermes models with tool-calling capabilities.

> **Personal fork** — I'm using this for local experimentation with Ollama. My typical setup uses `hermes3` via Ollama on port 11434.

## Features

- 🤖 **Hermes Model Integration** — Optimized for NousResearch Hermes model family
- 🛠️ **Tool Calling** — Structured function/tool calling via JSON schema
- 🔌 **OpenAI-Compatible API** — Drop-in replacement for OpenAI API clients
- 🐳 **Docker Support** — Containerized deployment ready
- ⚙️ **Flexible Configuration** — Extensive environment-based configuration

## Quick Start

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip
- An OpenAI-compatible LLM backend (e.g., [vLLM](https://github.com/vllm-project/vllm), [Ollama](https://ollama.com/), LM Studio)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-org/hermes-agent.git
cd hermes-agent

# Copy and configure environment
cp .env.example .env
# Edit .env with your settings

# Install dependencies (using uv)
uv sync

# Or using pip
pip install -r requirements.txt
```

### Configuration

All configuration is done via environment variables. See [`.env.example`](.env.example) for the full list of options.

Key variables:

| Variable | Description | Default |
|---|---|---|
| `OPENAI_API_BASE` | Base URL for your LLM backend | `http://localhost:8000/v1` |
| `OPENAI_API_KEY` | API key (use `none` for local backends) | `none` |
| `MODEL_NAME` | Model identifier to use | `NousResearch/Hermes-3-Llama-3.1-8B` |
| `MAX_TOKENS` | Maximum tokens per response | `4096` |
| `TEMPERATURE` | Sampling temperature | `0.7` |

#### Ollama Setup

If you're running Ollama locally, set these in your `.env`:

```
OPENAI_API_BASE=http://localhost:11434/v1
OPENAI_API_KEY=none
MODEL_NAME=hermes3
TEMPERATURE=0.5
MAX_TOKENS=8192
```

> **Note:** I find `TEMPERATURE=0.5` gives more consistent tool-calling behavior with `hermes3` on Ollama compared to the default `0.7`. Your mileage may vary.

> **Note:** Bumped `MAX_TOKENS` to `8192` for Ollama — the default `4096` was occasionally cutting off longer tool responses mid-output.

> **Note:** If Ollama returns connection errors on startup, make sure the Ollama service is actually running (`ollama serve`) before launching the agent. Took me an embarrassingly long time to figure that one out.

> **Note:** On macOS, Ollama sometimes goes to sleep after inactivity and the first request will time out. Running `ollama run hermes3` in a separate terminal to warm it up before starting the agent helps.

### Running

```bash
# With uv
uv run python -m hermes_agent

# Or directly
python -m hermes_agent
```

### Docker

```bash
# Build the image
docker build -t hermes-agent .

# Run with environment file
docker run --env-file .env -p 8080:8080 hermes-agent
```

## Architecture

```
hermes_agent/
├── __main__.py        # Entry point
├── agent.py           # Core agent loop
├── tools/             # Tool definitions and implementations
├── prompts/           # System prompts and templates
└── util
```
