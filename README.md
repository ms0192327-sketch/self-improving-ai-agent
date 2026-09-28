# AI Automation Agent

A self-improving AI automation agent built with FastAPI, OpenAI, and SQLite.

## Features

- 🤖 AI-powered request handling
- 🔧 Tool-based automation (web search, task creation, API calls)
- 📊 SQLite logging and performance tracking
- 🚀 Self-improvement mechanism
- ⚡ FastAPI with async support
- 📈 Success rate tracking

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/ms0192327-sketch/self-improving-ai-agent.git
cd self-improving-ai-agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

```bash
cp .env.example .env
```

Then edit `.env` and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
MODEL_NAME=gpt-4o-mini
```

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

The app will be available at `http://localhost:8000`

## API Endpoints

### Send a request to the agent

```bash
curl -X POST http://localhost:8000/agent \
  -H "Content-Type: application/json" \
  -d '{"text":"Search latest AI automation trends and summarize them"}'
```

### View recent logs

```bash
curl http://localhost:8000/logs?limit=10
```

### Get performance statistics

```bash
curl http://localhost:8000/stats
```

### Get improvement suggestions

```bash
curl http://localhost:8000/improve
```

## Project Structure

```
ai-automation-agent/
├── app/
│   ├── __init__.py
│   ├── config.py          # Configuration and environment
│   ├── prompts.py         # System prompts for LLM
│   ├── tools.py           # Tool implementations (search, API calls, etc.)
│   ├── memory.py          # SQLite database operations
│   ├── evaluator.py       # Response evaluation logic
│   ├── agent.py           # Main agent logic and self-improvement
│   └── main.py            # FastAPI application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## How It Works

1. **User Input**: Send a request via the `/agent` endpoint
2. **Tool Decision**: Agent decides which tool to use based on keywords
3. **Tool Execution**: Executes the selected tool (search, create task, etc.)
4. **LLM Processing**: OpenAI processes the result with system prompt
5. **Logging**: Result is saved to SQLite database
6. **Evaluation**: Success is evaluated based on response quality
7. **Self-Improvement**: Agent learns from past performance

## Tools Available

- **web_search**: Search the web using DuckDuckGo
- **summarize_text**: Create summaries of text
- **create_task**: Create automation tasks
- **fetch_data_from_api**: Fetch data from APIs
- **direct_answer**: Answer without tools

## Next Steps for Enhancement

- [ ] Add authentication (JWT tokens)
- [ ] Add real task scheduling (Celery, APScheduler)
- [ ] Add user session management
- [ ] Add code execution tools
- [ ] Add workflow orchestration
- [ ] Add monitoring and dashboards
- [ ] Add database persistence (PostgreSQL)
- [ ] Add Redis caching
- [ ] Add webhook support
- [ ] Add deployment configs (Docker, Kubernetes)

## Requirements

- Python 3.9+
- OpenAI API key
- 50MB disk space for SQLite database

## License

MIT

## Support

For issues or questions, please open a GitHub issue.
