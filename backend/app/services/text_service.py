import re

def clean_text(text: str) -> str:
    text = text.replace("\r", "\n")

    text = re.sub(r"[\t]+", " ", text)

    text = re.sub(r"\n{3,}", "\n\n", text)

    lines = [line.strip() for line in text.split("\n")]

    cleaned_lines = [line for line in lines if line]

    return "\n".join(cleaned_lines)
