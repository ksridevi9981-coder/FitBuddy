\# FitBuddy – AI Fitness Plan Generator



FitBuddy is an AI-powered fitness planning web application built with \*\*FastAPI, Google Gemini, SQLite, and SQLAlchemy\*\*. It generates personalized 7-day workout plans based on a user's fitness details, provides nutrition and recovery tips, and allows users to refine their plans through feedback.



\## Features



\* ??? Personalized 7-day workout plans

\* ?? Goal-based fitness planning

\* ?? Nutrition and recovery tips

\* ?? Feedback-based workout plan updates

\* ?? User profile and plan storage

\* ??? SQLite database with SQLAlchemy

\* ??? Interactive Jinja2 web interface

\* ?? Admin / coach dashboard

\* ?? FastAPI interactive API documentation



\## Technologies Used



\* \*\*Python\*\*

\* \*\*FastAPI\*\*

\* \*\*Uvicorn\*\*

\* \*\*Google Gemini API\*\*

\* \*\*SQLAlchemy\*\*

\* \*\*SQLite\*\*

\* \*\*Jinja2\*\*

\* \*\*HTML\*\*

\* \*\*CSS\*\*

\* \*\*JavaScript\*\*



\## How It Works



1\. The user enters their name, age, weight, fitness goal, and workout intensity.

2\. FitBuddy sends the information to Google Gemini.

3\. Gemini generates a personalized 7-day workout plan.

4\. FitBuddy generates a nutrition and recovery tip based on the selected goal.

5\. The user can submit feedback, such as requesting more cardio or additional rest days.

6\. The existing plan is updated according to the feedback.

7\. User details and generated plans are stored in the SQLite database.

8\. The admin dashboard allows stored users and workout plans to be viewed.



\## Setup



\### 1. Create a Virtual Environment



```bash

python -m venv venv

```



\### 2. Activate the Virtual Environment



\*\*Windows PowerShell:\*\*



```powershell

venv\\Scripts\\Activate.ps1

```



\### 3. Install Dependencies



```bash

pip install -r requirements.txt

```



\### 4. Configure the Gemini API Key



Create a `.env` file in the project root:



```env

GEMINI\_API\_KEY=your\_api\_key\_here

```



> Keep your API key private. The `.env` file is excluded from Git using `.gitignore`.



\### 5. Run the Application



```bash

uvicorn app.main:app --reload

```



Open the application at:



```text

http://127.0.0.1:8000

```



\## API Documentation



FastAPI automatically provides interactive API documentation at:



```text

http://127.0.0.1:8000/docs

```



\## Admin Dashboard



The admin / coach dashboard can be accessed at:



```text

http://127.0.0.1:8000/view-all-users

```



\## Project Structure



```text

FitBuddy/

¦

+-- app/

¦   +-- \_\_init\_\_.py

¦   +-- main.py

¦   +-- routes.py

¦   +-- database.py

¦   +-- models.py

¦   +-- schemas.py

¦   +-- gemini\_generator.py

¦   +-- gemini\_flash\_generator.py

¦   +-- updated\_plan.py

¦   +-- nutrition.py

¦

+-- templates/

¦   +-- index.html

¦   +-- result.html

¦   +-- all\_users.html

¦

+-- static/

¦   +-- style.css

¦   +-- images/

¦

+-- .env

+-- .gitignore

+-- requirements.txt

+-- README.md

```



The SQLite database `fitbuddy.db` is generated automatically when the application starts.



\## Security



The Gemini API key is stored in the local `.env` file and is excluded from Git using `.gitignore`.



Sensitive files such as API keys, the local database, and the virtual environment should not be committed to the repository.



