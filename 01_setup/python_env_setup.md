# Python Environment Setup

## Recommended Python Version

- **Python 3.10+** (3.11 recommended for best compatibility)

## Virtual Environment

### Using venv (Standard)

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows PowerShell)
venv\Scripts\Activate.ps1

# Activate (Windows CMD)
venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt
```

### Using conda

```bash
# Create environment
conda create -n genai python=3.11

# Activate
conda activate genai

# Install dependencies
pip install -r requirements.txt
```

### Using uv (Fast)

```bash
# Install uv if not already installed
pip install uv

# Create environment and install
uv venv
uv pip install -r requirements.txt
```

## Verify Installation

```bash
python -c "import langchain; print(f'LangChain: {langchain.__version__}')"
python -c "import pydantic; print(f'Pydantic: {pydantic.__version__}')"
```

## Deactivating

```bash
deactivate  # for venv
conda deactivate  # for conda
```
