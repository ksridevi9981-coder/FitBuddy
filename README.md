# FitBuddy – AI Fitness Plan Generator

FitBuddy is a FastAPI-based AI fitness planning application powered by Google's Gemini models.

## Features

- Personalized 7-day workout plans
- Goal-based nutrition and recovery tips
- Feedback-based workout plan updates
- SQLite database with SQLAlchemy
- Jinja2 frontend
- Admin / coach dashboard
- FastAPI API documentation

## Technologies

- Python
- FastAPI
- Uvicorn
- Google Gemini API
- SQLAlchemy
- SQLite
- Jinja2
- HTML
- CSS

## Setup

Create and activate a virtual environment:

python -m venv venv

Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Create a .env file:

GEMINI_API_KEY=your_api_key_here

Run:

uvicorn app.main:app --reload

Open:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs

Admin dashboard:

http://127.0.0.1:8000/view-all-users

## Project Structure

app/
    main.py
    routes.py
    database.py
    models.py
    schemas.py
    gemini_generator.py
    gemini_flash_generator.py
    updated_plan.py
    nutrition.py

templates/
    index.html
    result.html
    all_users.html

static/
    style.css
    images/

The SQLite database itbuddy.db is generated automatically when the application starts.

## Security

The Gemini API key is stored in .env and excluded from Git using .gitignore.
