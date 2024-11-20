import subprocess
import dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings

dotenv.load_dotenv()

llm = ChatOpenAI(model="o1-mini")


def main():
    diff = get_diff()

    review = get_review(diff)

    formatted_review = format_review(review)

    print(formatted_review)


def get_diff() -> str:
    result = subprocess.run(["git", "show", "head"], capture_output=True)

    if result.returncode == 128:
        raise ValueError("No commits found")

    return result.stdout.decode("utf-8")


def get_review(diff: str):
    review = llm.invoke(
        [
            (
                "assistant",
                "Review user git diff. Check typo, grammar, and code style.",
            ),
            ("human", diff),
        ]
    ).content

    return review


def format_review(review: str):
    formatted_review = review

    return formatted_review


if __name__ == "__main__":
    main()
