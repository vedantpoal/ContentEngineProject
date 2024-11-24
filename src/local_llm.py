import requests

def query_local_llm(prompt):
    """Query a locally running LLM (Ollama API)."""
    url = "http://localhost:11400/completion"
    payload = {"model": "llama", "prompt": prompt, "max_tokens": 300}
    response = requests.post(url, json=payload)
    return response.json().get("completion")
