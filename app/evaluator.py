def evaluate_response(response: str):
    """Simple evaluation: response is successful if it's long enough and not empty."""
    if response and len(response.strip()) > 20:
        return 1
    return 0