from dotenv import load_dotenv

load_dotenv()


def get_text_length(text: str)-> int:
    """Return the length of a text by characters"""
    return len(text)
if __name__ == "__main__":
    print("Hello react")
    print(get_text_length(text="dog"))
