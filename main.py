from dotenv import load_dotenv
from pathlib import Path
import os

os.environ["OPENAI_API_KEY"] = (
    "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"
)

# load_dotenv(r"C:\langchain-course\.env")
# print(os.listdir("."))
# print("Current directory:", os.getcwd())
# print(".env exists:", Path(".env").exists())
# result =load_dotenv()
# print("load_dotenv returned:", result)


def main():
    print("Hello from langchain-course!")
    print(os.environ.get("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
