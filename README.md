# API Sentinel

> An API monitoring platform — **Phase 1: Foundation**

## Prerequisites

- Python 3.11+ (ships with macOS or install via [Homebrew](https://brew.sh))
- Git

## Quick Start

```bash
# 1. Clone (or open) the project
cd "API Sentinel"

# 2. Create & activate a virtual environment
python3 -m venv backend/.venv
source backend/.venv/bin/activate

# 3. Install dependencies
pip install -r backend/requirements.txt

# 4. Create your .env from the template
cp backend/.env.example backend/.env

# 5. Start the development server
uvicorn backend.app.main:app --reload
```

The server starts at **http://127.0.0.1:8000**.

## Available Endpoints

| Method | Path      | Description               |
|--------|-----------|---------------------------|
| GET    | `/`       | Welcome message           |
| GET    | `/health` | Health-check (status JSON) |
| GET    | `/docs`   | Swagger UI documentation  |

## Project Structure

```text
api-sentinel/
├── backend/
│   ├── app/
│   │   └── main.py          # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   ├── .env.example          # Environment template
│   └── .env                  # Local secrets (git-ignored)
├── .gitignore
└── README.md
```

## License

Private — all rights reserved.
