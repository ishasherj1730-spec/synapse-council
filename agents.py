from prompts import COUNCIL_PROMPT

from llm import generate_response


def council_agent(question):

    prompt = f"""
    {COUNCIL_PROMPT}

    User Question:
    {question}
    """

    return generate_response(prompt)
