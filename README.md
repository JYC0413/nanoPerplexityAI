# nanoPerplexityAI with LlamaEdge

## Description
This project extends nanoPerplexityAI to support LlamaEdge by integrating specific environment variables and dependencies.

## Setup Instructions

### Environment Variables
Before running the project, you need to set up three environment variables:
- `OPENAI_BASE_URL`: Set this to `https://llama.us.gaianet.network/v1`
- `LLM_MODEL`: Set this to `llama`
- `OPENAI_API_KEY`: Set this to `LLAMAEDGE`

#### Windows
Open Command Prompt and execute:
```cmd
set OPENAI_BASE_URL=https://llama.us.gaianet.network/v1
set LLM_MODEL=llama
set OPENAI_API_KEY=LLAMAEDGE
```
```powershell
$env:OPENAI_BASE_URL=https://llama.us.gaianet.network/v1
$env:LLM_MODEL=llama
$env:OPENAI_API_KEY=LLAMAEDGE
```
#### Mac/Linux
Open Terminal and execute:
```bash
export OPENAI_BASE_URL=https://llama.us.gaianet.network/v1
export LLM_MODEL=llama
export OPENAI_API_KEY=LLAMAEDGE
```

### Dependencies
Before running the script, install the required dependencies:
```bash
pip install googlesearch-python requests beautifulsoup4 lxml lama_index
```

## Running the Script
Once the environment variables are set and dependencies installed, you can run the script:
```bash
python nanoPerplexityAI.py
```