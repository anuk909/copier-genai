# Copier GenAI

Copier template for production-ready Generative AI projects.

## Features

- 🤖 **Multiple LLM Providers**: OpenAI, Claude, Ollama, vLLM support
- 📚 **RAG Ready**: Optional vector databases (ChromaDB, Qdrant, Pinecone, Weaviate)
- 🏗️ **Clean Architecture**: Modular structure with core, inference, processing, and RAG modules
- ⚡ **Modern Python**: uv for dependency management, Ruff for formatting/linting
- 🐳 **Docker Support**: Optional containerization with docker-compose
- 🧪 **Testing Built-in**: pytest with unit and integration test structure
- 📝 **AI Agent Ready**: Includes AGENTS.md guide for AI coding assistants
- 🔐 **Git Integration**: Auto-fills author info from git config
- ⚙️ **YAML Configuration**: Clean separation of config from code

## Requirements

To use this Copier template, you will need:

- **Git** v2+
- **Python** 3.11+
- **Copier** with extensions

### Install Copier

```bash
# With uv (recommended)
uv tool install copier --with copier-templates-extensions

# Or with pipx
pipx install copier
pipx inject copier copier-templates-extensions
```

### Interactive Setup

Copier will ask you questions to customize your project:

- **Project name**: Your GenAI project name
- **LLM Provider**: Choose from OpenAI, Claude, Ollama, or vLLM
- **RAG Support**: Enable/disable retrieval augmented generation
- **Vector Database**: Select ChromaDB, Qdrant, Pinecone, or Weaviate
- **Docker**: Include Docker configuration
- **Python Version**: Choose 3.11, 3.12, or 3.13
- **License**: MIT, Apache-2.0, BSD-3-Clause, or None

## Template Structure

The generated project will have this structure:

```
your-project/
├── config/
│   ├── model_config.yaml      # LLM and RAG configuration
│   └── logging_config.yaml    # Logging setup
├── data/
│   ├── cache/                 # Response cache
│   ├── embeddings/            # Embedding storage
│   └── vectordb/              # Vector database files
├── src/
│   ├── core/                  # LLM abstraction layer
│   │   ├── base_llm.py        # Base interface
```

## Quick Setup and Usage

Make sure all the requirements are met, then:

```bash
copier copy --trust "https://github.com/anuk909/copier-genai.git" my-genai-project
```

Or even shorter:

```bash
copier copy --trust "gh:anuk909/copier-genai" my-genai-project
```

Or from a local clone:

```bash
copier copy --trust /path/to/copier-genai my-genai-project
```

### After Generation

```bash
cd my-genai-project
bash scripts/setup_env.sh  # Install dependencies
cp .env.example .env       # Configure API keys
uv run pytest              # Run tests
```

## What You Get

```
your-project/
├── src/
│   ├── core/              # LLM client implementations
│   ├── rag/               # Vector DB & embeddings (optional)
│   ├── prompts/           # Prompt templates
│   ├── processing/        # Text processing utilities
│   └── inference/         # Inference engine
├── tests/                 # Unit & integration tests
├── config/                # YAML configuration files
├── scripts/               # Setup & utility scripts
├── docker-compose.yml     # Docker setup (optional)
└── AGENTS.md              # Guide for AI coding assistants
```

## Template Options

When you run the template, you'll be prompted for:

- **Project name** and description
- **LLM provider**: OpenAI, Claude, Ollama, or vLLM
- **RAG support**: Include vector database integration
- **Vector DB**: ChromaDB, Qdrant, Pinecone, or Weaviate
- **Docker**: Include Docker configuration
- **Python version**: 3.11, 3.12, or 3.13
- **License**: MIT, Apache-2.0, BSD, GPL, and more

The template automatically:

- Pulls your name and email from `git config`
- Sets copyright year to current year
- Generates repository URLs for GitHub, GitLab, or Bitbucket
- Creates an AI agent guide (AGENTS.md) for your project

## Credits

Inspired by [Prashant Rathi's](https://medium.com/@PrashantRathhttps://medium.com/@PrashantRath) approach to production-ready GenAI architecture.
And [copier-uv](https://github.com/pawamoy/copier-uv) - General Python projects with uv

## License

MIT - See [LICENSE](LICENSE) for details.

---

Built with ❤️ for the GenAI community
