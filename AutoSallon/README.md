# AutoSallon - Streamlit + FastAPI + Uvicorn + SQLite

A simple car dealership project with:
- FastAPI backend (`api.py`) served by Uvicorn
- SQLite database with SQLAlchemy (`database.py`, `models.py`)
- Streamlit frontend dashboard (`streamlit_app.py`)

## 1) Install dependencies

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 2) Run the API

```powershell
uvicorn api:app --reload --port 8000
```

## 3) Run Streamlit UI (new terminal)

```powershell
streamlit run streamlit_app.py
```

## API endpoints
- `GET /health`
- `GET /cars`
- `POST /cars`
- `GET /summary`
