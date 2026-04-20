# Hermes Agent

A fork of [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) — an agentic AI assistant powered by Hermes models with tool-calling capabilities.

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
└── utils/             # Utility functions
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/my-feature`)
3. Commit your changes
4. Open a Pull Request

Please use the [issue templates](.github/ISSUE_TEMPLATE/) for bug reports and feature requests.

## License

MIT License — see [LICENSE](LICENSE) for details.

## Acknowledgements

- [NousResearch](https://nousresearch.com/) for the original hermes-agent and Hermes model family
- The open-source LLM community
