# AI Agents Guide

This document provides guidance for AI coding assistants working with this Copier template for GenAI projects.

## Project Overview

This is a Copier template that generates production-ready GenAI projects with:

- Multiple LLM provider support (OpenAI, Claude, Ollama)
- RAG (Retrieval-Augmented Generation) capabilities
- Vector embeddings and storage
- Modular architecture with core, inference, processing, and RAG modules
- Comprehensive testing setup
- Docker support

## Template Structure

### Core Components

- **`copier.yml`**: Template configuration with user prompts and project metadata
- **`template/`**: Contains all Jinja2 templates that generate the target project
  - Files with `.jinja` extension are templates that will be rendered
  - Files without `.jinja` are copied as-is

### Generated Project Structure

The template generates projects with:

- **`src/core/`**: LLM client implementations (OpenAI, Claude, Ollama)
- **`src/rag/`**: RAG components (embeddings, vector stores, retrieval)
- **`src/prompts/`**: Prompt templates and chain management
- **`src/processing/`**: Text processing, chunking, tokenization
- **`src/inference/`**: Inference engine and response parsing
- **`tests/`**: Unit and integration tests with pytest
- **`config/`**: YAML configuration for logging and models
- **`scripts/`**: Utility scripts for setup and maintenance

## Working with This Template

### Key Files to Understand

1. **copier.yml**: Defines all template variables and their defaults
   - User inputs (project name, author, LLM providers)
   - Conditional rendering logic
   - Validation rules

2. **Jinja Templates**: All `.jinja` files use template variables
   - Use `{{ variable_name }}` for substitution
   - Use `{% if condition %}` for conditional content
   - Common variables: `project_slug`, `project_name`, `author_name`, `use_openai`, `use_claude`, etc.

3. **pyproject.toml.jinja**: Python dependencies
   - Conditional dependencies based on selected LLM providers
   - Optional dependencies for dev, test, and docs

### Template Variables

Key variables available in all templates:

- `project_name`: Human-readable project name
- `project_slug`: Python-compatible project identifier
- `project_description`: Brief project description
- `author_name`, `author_email`: Author information
- `python_version`: Target Python version
- `use_openai`, `use_claude`, `use_ollama`: LLM provider flags
- `use_docker`: Docker support flag
- `license`: License type (MIT, Apache-2.0, GPL-3.0, Proprietary)

### Testing the Template

To test template generation:

```bash
# From the template directory
copier copy . /path/to/test-output

# Or with specific answers
copier copy . /path/to/test-output \
  --data project_name="Test Project" \
  --data use_openai=true
```

### Common Tasks

#### Adding New Template Files

1. Create file in `template/` directory
2. Add `.jinja` extension if it needs variable substitution
3. Use template variables as needed
4. Test generation

#### Adding New Variables

1. Add to `copier.yml` with type, help text, and default
2. Use in templates with `{{ variable_name }}`
3. Add validation if needed

#### Modifying Dependencies

Edit `template/pyproject.toml.jinja`:

- Core dependencies in `[project.dependencies]`
- Optional dependencies in `[project.optional-dependencies]`
- Use Jinja2 conditionals for provider-specific deps

## Best Practices

### For Template Development

1. **Test Thoroughly**: Generate projects with different configurations
2. **Validate Syntax**: Ensure generated Python files are valid
3. **Document Variables**: Keep copier.yml well-commented
4. **Version Pinning**: Use flexible version constraints (e.g., `>=1.0,<2.0`)
5. **Default Values**: Provide sensible defaults for all prompts

### For Generated Projects

1. **Configuration**: Use YAML files in `config/` for model settings
2. **Environment**: Set API keys via environment variables
3. **Testing**: Run tests before deployment
4. **Docker**: Use docker-compose for local development

## Architecture Notes

### LLM Client Pattern

All LLM clients inherit from `BaseLLM` and implement:

- `generate()`: Single response generation
- `stream()`: Streaming responses
- `get_model_info()`: Model metadata

Use `ModelFactory` to instantiate clients based on configuration.

### RAG Pipeline

1. **Embedder**: Converts text to vectors
2. **VectorStore**: Stores and indexes embeddings
3. **Retriever**: Finds relevant documents
4. **Indexer**: Builds and manages indices

### Configuration Management

- `model_config.yaml`: LLM provider settings, API endpoints
- `logging_config.yaml`: Logging levels and handlers
- Environment variables: API keys, sensitive data

## Troubleshooting

### Template Issues

- **Jinja2 Syntax Errors**: Check bracket matching in `.jinja` files
- **Missing Variables**: Verify variable names in `copier.yml`
- **File Not Generated**: Check file patterns and conditions

### Generated Project Issues

- **Import Errors**: Check conditional dependencies in pyproject.toml
- **API Failures**: Verify environment variables and API keys
- **Test Failures**: Ensure fixtures and test data are correct

## Resources

- [Copier Documentation](https://copier.readthedocs.io/)
- [Jinja2 Template Designer Docs](https://jinja.palletsprojects.com/)
- [uv Package Manager](https://github.com/astral-sh/uv)

## Version

Template Version: 0.1.0
Last Updated: January 2026
