from database import init_db


def main() -> None:
    init_db()
    print("Database initialized. Run:")
    print("1) uvicorn api:app --reload --port 8000")
    print("2) streamlit run streamlit_app.py")


if __name__ == "__main__":
    main()


