# LangGraph Application Template

A template project for building AI applications using LangGraph, with integrated knowledge graph capabilities and LLM support.

## Project Overview

This template provides a foundation for building AI applications with:
- LangGraph-based workflow management
- Flexible LLM integration (OpenAI, Amazon Bedrock)

## Project Structure

```
.
├── src/
│   ├── Chains/                 # LangChain processing chains
│   │   └── example_chain.py    # Example chain implementation
│   │
│   ├── LLM/                    # LLM integration
│   │   ├── Pipeline.py         # Main LLM orchestration
│   │   ├── LLMBase.py         # Abstract LLM interface
│   │   ├── example_llm_model.py # Example LLM implementation
│   │   └── config_defs.py     # LLM configuration schemas
│   │
│   ├── Nodes/                  # LangGraph workflow nodes
│   │   ├── __init__.py
│   │   └── example_node.py    # Example workflow node
│   │
│   ├── Prompts/               # LLM prompt templates
│   │   └── example_prompt.txt
│   │
│   ├── Decorators/            # Utility decorators
│   │   └── example_decorator.py
│   │
│   ├── graph.py              # LangGraph workflow definition
│   ├── main.py              # Application entry point
│   ├── server.py           # FastAPI implementation
│   ├── ui.py              # Streamlit interface
│   ├── state_model.py    # State management
│   ├── const.py         # Constants
│   └── output_models.py # Pydantic models
│
├── configs/              # Configuration files
│   ├── GraphDatabase/   # Neo4j settings
│   └── LLM/            # LLM provider configs
│
└── tests/              # Test suite
```

## Component Details

### Core Components

#### 1. LLM Integration (`src/LLM/`)
- Abstract base class for LLM providers
- Implementation examples for OpenAI/Bedrock
- Pipeline management for LLM operations
- Configuration definitions and validation

#### 2. Workflow Nodes (`src/Nodes/`)
- Individual processing steps in LangGraph workflow
- State transformation logic
- Example node implementation

#### 3. Processing Chains (`src/Chains/`)
- Reusable LangChain components
- Task-specific processing pipelines
- Chain composition utilities

#### 4. Application Layer
- `graph.py`: LangGraph workflow definition
- `server.py`: REST API endpoints
- `ui.py`: Streamlit user interface
- `state_model.py`: Workflow state management

