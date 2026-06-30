# 🔗 URL Shortener API

A lightweight URL shortener built with **FastAPI** and **SQLite**, developed as part of my journey learning Python and backend development. This project applies core concepts of REST API design, database integration, and clean code structure.

## 📖 About

This project was built to practice and demonstrate fundamental backend engineering skills using Python. It takes a long URL and generates a unique short code that redirects to the original address — a classic, well-scoped problem that's great for solidifying concepts like routing, persistence, and API design.

It's part of my ongoing transition from technical support / OutSystems into Python backend and AI engineering, where I'm building hands-on projects to apply what I study.

## ✨ Features

- Shorten long URLs into compact, shareable codes
- Redirect from a short code to the original URL
- Persistent storage using SQLite
- RESTful API built with FastAPI
- Automatic interactive API documentation (Swagger UI)

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python 3** | Core language |
| **FastAPI** | Web framework / REST API |
| **SQLite** | Lightweight relational database |
| **Uvicorn** | ASGI server |

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Arantesmateus/urlshorten.git
cd urlshorten

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the app

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`, with interactive docs at `http://127.0.0.1:8000/docs`.

## 📡 API Usage

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/shorten` | Creates a short code for a given URL |
| `GET` | `/{short_code}` | Redirects to the original URL |

### Example request

```bash
curl -X POST "http://127.0.0.1:8000/shorten" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.example.com/some/very/long/path"}'
```

### Example response

```json
{
  "original_url": "https://www.example.com/some/very/long/path",
  "short_code": "aZ3kT9",
  "short_url": "http://127.0.0.1:8000/aZ3kT9"
}
```

## 🧪 Testing

The project includes a `test_db.py` file with tests covering the database layer.

```bash
pytest
```

## 📚 What I Practiced in This Project

- Building and structuring a REST API from scratch with FastAPI
- Designing and interacting with a SQLite database in Python
- Generating and validating unique identifiers
- Handling HTTP redirects and status codes
- Writing tests for the data layer
- Organizing a Python project for readability and maintainability

## 🗺️ Roadmap / Next Steps

- [ ] Add URL expiration and click-tracking analytics
- [ ] Add custom alias support for short codes
- [ ] Migrate from SQLite to PostgreSQL
- [ ] Add authentication for managing personal links
- [ ] Deploy to Railway / Fly.io

## 👤 Author

**Mateus Arantes**
Python & AI Backend Developer in training | Recife, PE - Brazil

- GitHub: [@Arantesmateus](https://github.com/Arantesmateus)

## 📄 License

This project is open source and available for learning purposes.
