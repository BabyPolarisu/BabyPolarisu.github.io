Django + uvicorn minimal project

This workspace contains a minimal Django project with a single homepage routed at `/`.

Quick start (Windows PowerShell):

1. Create and activate a virtual environment (optional but recommended):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run Django checks (optional):

```powershell
python manage.py check
```

4. Run with uvicorn (ASGI):

```powershell
# from the project root (where manage.py lives)
uvicorn mysite.asgi:application --reload --port 8000
```

Open http://127.0.0.1:8000/ to see the homepage.
