import requests

def web_search(query: str):
    url = "https://duckduckgo.com/html/?q=" + query.replace(" ", "+")
    try:
        response = requests.get(url, timeout=10)
        return {
            "status": "ok",
            "query": query,
            "preview": response.text[:1200],
        }
    except Exception as exc:
        return {
            "status": "error",
            "query": query,
            "error": str(exc),
        }

def summarize_text(text: str):
    # In a real project, this would call an LLM or a summarizer service.
    return {
        "status": "ok",
        "summary": text[:500],
    }

def create_task(task_name: str):
    return {
        "status": "ok",
        "task_name": task_name,
        "message": "Task created successfully.",
    }

def fetch_data_from_api(url: str):
    try:
        response = requests.get(url, timeout=10)
        return {
            "status": "ok",
            "url": url,
            "data": response.text[:1200],
        }
    except Exception as exc:
        return {
            "status": "error",
            "url": url,
            "error": str(exc),
        }