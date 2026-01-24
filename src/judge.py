from openai import OpenAI

def llm_judge(context, rule_result):

    client = OpenAI()
    prompt = f"""
    Context:
    - {context[0]}
    - {context[1]}

        Rule decision: {rule_result}

        Do you agree with the rule's decision?
        Answer ONLY in this format:
        AGREE or DISAGREE
        Reason: <short explanation>
        """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an impartial AI judge for evaluating LLM systems."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    text = response.choices[0].message.content.strip()

    if text.startswith("AGREE"):
        agrees = True
    elif text.startswith("DISAGREE"):
        agrees = False
    else:
        raise ValueError("Unexpected LLM response format: " + text)

    comment = text
    return agrees, comment


