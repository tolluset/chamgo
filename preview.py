import os
import subprocess
import logging
import dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings

logging.basicConfig(level=logging.INFO)
dotenv.load_dotenv()


LLM_MODEL = os.getenv("LLM_MODEL") or "o1-mini"
LANGUAGE = os.getenv("LANGUAGE") or "ENGLISH"

llm = ChatOpenAI(model="o1-mini")


def main():
    check_env()

    diff = get_diff()

    review = get_review(diff)

    formatted_review = format_review(review)

    logging.info(formatted_review)


def check_env():
    required_vars = ["OPENAI_API_KEY"]

    for var in required_vars:
        if not os.getenv(var):
            raise EnvironmentError(f"Required environment variable '{var}' is not set.")


def get_diff() -> str:
    result = subprocess.run(["git", "show", "head"], capture_output=True)

    if result.returncode == 128:
        raise ValueError("No commits found")

    return result.stdout.decode("utf-8")


def get_review(diff: str) -> str:
    review = llm.invoke(
        [
            (
                "assistant",
                "Review the user's git diff, checking for typos, grammar, and code style issue.",
            ),
            ("human", diff),
        ]
    ).content

    return review


def format_review(review: str) -> str:
    formatted_review = review

    return formatted_review


if __name__ == "__main__":
    main()
