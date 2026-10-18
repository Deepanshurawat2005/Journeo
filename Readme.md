# Journeo — Multi-Agent System Using LangGraph, MCP, Supervisor, Guardrails & HITL

A demo multi-agent system that uses LangGraph and MCP to implement a travel-planning assistant with a Supervisor, input Guardrails, and Human-In-The-Loop (HITL) approval flows. The project includes a FastAPI frontend, example MCP server, and client helpers to demonstrate how agents, supervisors, and guardrails can be composed into a safe, reviewable planning pipeline.

## Key Ideas
- Multi-agent coordination using LangGraph and MCP
- Supervisor agent to manage complex workflows
- Input guardrails to validate user requests
- Human-in-the-loop approval for generated plans

## Contents
- `app.py`: FastAPI web frontend and API endpoints
- `backend.py`: Core agent orchestration / travel-planner logic
- `mcp_client.py`: Client helpers to interact with the MCP server
- `custom_weather_mcp_server.py`: Example MCP server for weather checks
- `templates/`, `static/`: Frontend UI assets (HTML, JS, CSS)

## Features
- Interactive web UI for sending travel-planning prompts
- Endpoint for drafting travel plans and separate approval endpoint
- Example MCP server demonstrating domain adapters (weather, checkpoints)

## Prerequisites
- Python 3.10+ (recommended)
- Git (to clone the repo)
- A virtual environment tool (`venv`) or similar

## Quick Start (Windows)

### 1. Create and activate a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1    # PowerShell
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Run the FastAPI app (development)

**Option A: Run module**

```powershell
python app.py
```

**Option B: Run Uvicorn**

```powershell
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

### 4. Open the web UI

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to use the Journeo frontend.

## Running the MCP Server (Example)

The repository includes `custom_weather_mcp_server.py` as an example MCP server. Run it in a separate terminal if you want to experiment with custom adapters used by the demo.

```powershell
python custom_weather_mcp_server.py
```

## API Endpoints

- `POST /api/travel` — Create or resume a travel-planning thread.

  JSON: `{ "message": "<user prompt>", "thread_id": "optional-thread-id" }`

- `POST /api/travel/approve` — Approve or request revisions for a draft.

  JSON: `{ "thread_id": "<id>", "approved": true|false, "feedback": "optional" }`

- `GET /health` — Basic health check and features list.

## Configuration & Environment

Secrets and API keys are not included in the repository. Use environment variables or a `.env` file for any required keys consumed by `langgraph`, `langchain`, or other adapters.

## Development Notes

- The project keeps synchronous convenience wrappers in `backend.py` while running an async FastAPI server — `nest_asyncio` is applied in `app.py` to allow the sync helpers to call async MCP helpers.
- Tests are not included; to experiment, interact with the web UI or call the API endpoints directly.

## Contributing

Contributions are welcome. Please open issues or pull requests for bug fixes, improvements, or new adapter examples.

## License

This repository follows the license in the `LICENSE` file.

## Acknowledgements

Built as a demonstration of LangGraph + MCP patterns with Supervisor and Guardrail concepts.

## Contact

For questions or suggestions, open an issue or contact the repository owner.