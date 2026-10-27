# API Sentinel

> An API monitoring platform — **Phase 2: Database Setup**

## Prerequisites

- Python 3.11+
- PostgreSQL 16+
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
# Edit backend/.env with your database credentials

# 5. Run database migrations
cd backend
alembic upgrade head
cd ..

# 6. Start the development server
cd backend
uvicorn app.main:app --reload
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
│   ├── alembic/                 # Alembic migration scripts
│   │   ├── versions/            # Auto-generated migration files
│   │   └── env.py               # Alembic environment config
│   ├── app/
│   │   ├── core/
│   │   │   ├── config.py        # Environment-based settings
│   │   │   └── database.py      # Async SQLAlchemy engine & session
│   │   ├── models/
│   │   │   ├── base.py          # Declarative base class
│   │   │   ├── user.py          # User model
│   │   │   ├── endpoint.py      # MonitoredEndpoint model
│   │   │   ├── check_result.py  # CheckResult model
│   │   │   └── incident.py      # Incident model
│   │   └── main.py              # FastAPI application
│   ├── alembic.ini              # Alembic configuration
│   ├── requirements.txt         # Python dependencies
│   ├── .env.example             # Environment template
│   └── .env                     # Local secrets (git-ignored)
├── .gitignore
└── README.md
```

## Database Models

| Table                | Description                        |
|----------------------|------------------------------------|
| `users`              | Registered user accounts           |
| `monitored_endpoints`| API URLs being monitored           |
| `check_results`      | Individual health-check results    |
| `incidents`          | Downtime windows for endpoints     |

## License

Private — all rights reserved.
