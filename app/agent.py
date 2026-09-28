import os
from openai import OpenAI

from app.config import MODEL_NAME
from app.prompts import SYSTEM_PROMPT
from app.tools import web_search, summarize_text, create_task, fetch_data_from_api
from app.memory import save_log
from app.evaluator import evaluate_response

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def decide_tool(user_input: str):
    """Decide which tool to use based on user input keywords."""
    text = user_input.lower()

    if "search" in text or "research" in text or "latest" in text:
        return "web_search"
    if "summarize" in text:
        return "summarize_text"
    if "create task" in text or "todo" in text or "task" in text:
        return "create_task"
    if "api" in text or "fetch" in text:
        return "fetch_data_from_api"
    return "direct_answer"

def call_llm(prompt: str):
    """Call the OpenAI LLM with the given prompt."""
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content

def run_agent(user_input: str):
    """Main agent loop: decide tool, execute, and return result."""
    tool_name = decide_tool(user_input)

    if tool_name == "web_search":
        tool_result = web_search(user_input)
        prompt = f"""
        User request: {user_input}

        Tool result:
        {tool_result}

        Produce a final answer using the tool result.
        """
    elif tool_name == "summarize_text":
        tool_result = summarize_text(user_input)
        prompt = f"""
        User request: {user_input}

        Tool result:
        {tool_result}

        Produce a concise and clear summary.
        """
    elif tool_name == "create_task":
        task_name = user_input
        tool_result = create_task(task_name)
        prompt = f"""
        User request: {user_input}

        Tool result:
        {tool_result}

        Return a short confirmation message saying task creation succeeded.
        """
    elif tool_name == "fetch_data_from_api":
        tool_result = fetch_data_from_api("https://api.github.com")
        prompt = f"""
        User request: {user_input}

        Tool result:
        {tool_result}

        Present the result in a human-friendly format.
        """
    else:
        tool_result = {"status": "none"}
        prompt = f"""
        User request: {user_input}

        No tool needed.
        Answer directly and clearly.
        """

    final_output = call_llm(prompt)
    success = evaluate_response(final_output)

    save_log(user_input, final_output, tool_name, success)

    return {
        "tool_used": tool_name,
        "output": final_output,
        "success": bool(success),
    }

def self_improve_agent():
    """Analyze past performance and suggest improvements."""
    from app.memory import get_recent_logs

    recent = get_recent_logs(10)
    failed = [row for row in recent if row[4] == 0]

    if not failed:
        return {
            "status": "ok",
            "message": "No failure patterns detected. Agent is performing consistently.",
        }

    suggestions = [
        "Review tool selection logic for repeated failure cases.",
        "Add more explicit prompt instructions for ambiguous queries.",
        "Introduce user confirmation before risky automation actions.",
        "Track per-tool success rate separately to adjust routing."
    ]

    return {
        "status": "warning",
        "failed_attempts": len(failed),
        "suggestions": suggestions,
    }