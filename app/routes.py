from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .database import SessionLocal
from .models import User
from .gemini_generator import generate_workout_gemini
from .gemini_flash_generator import generate_nutrition_tip_with_flash
from .updated_plan import update_workout_plan

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@router.post("/generate-workout", response_class=HTMLResponse)
def generate_workout(
    request: Request,
    name: str = Form(...),
    user_id: str = Form(...),
    age: int = Form(...),
    weight: float = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...)
):
    db: Session = SessionLocal()

    try:
        # Generate AI workout plan
        plan = generate_workout_gemini(
            name=name,
            age=age,
            weight=weight,
            goal=goal,
            intensity=intensity
        )

        # Generate nutrition tip
        nutrition_tip = generate_nutrition_tip_with_flash(goal)

        # Check whether this User ID already exists
        user = db.query(User).filter(User.user_id == user_id).first()

        if user:
            # Update existing user
            user.name = name
            user.age = age
            user.weight = weight
            user.goal = goal
            user.intensity = intensity
            user.original_plan = plan
            user.updated_plan = None
            user.feedback = None
            user.nutrition_tip = nutrition_tip

        else:
            # Create new user
            user = User(
                user_id=user_id,
                name=name,
                age=age,
                weight=weight,
                goal=goal,
                intensity=intensity,
                original_plan=plan,
                nutrition_tip=nutrition_tip
            )

            db.add(user)

        db.commit()
        db.refresh(user)

        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "user": user,
                "updated": False
            }
        )

    finally:
        db.close()


@router.post("/submit-feedback", response_class=HTMLResponse)
def submit_feedback(
    request: Request,
    user_id: str = Form(...),
    feedback: str = Form(...)
):
    db: Session = SessionLocal()

    try:
        user = db.query(User).filter(User.user_id == user_id).first()

        if not user:
            return HTMLResponse(
                content="User not found.",
                status_code=404
            )

        updated_plan = update_workout_plan(
            original_plan=user.original_plan,
            feedback=feedback,
            name=user.name,
            age=user.age,
            weight=user.weight,
            goal=user.goal,
            intensity=user.intensity
        )

        user.feedback = feedback
        user.updated_plan = updated_plan

        db.commit()
        db.refresh(user)

        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "user": user,
                "updated": True
            }
        )

    finally:
        db.close()


@router.get("/view-all-users", response_class=HTMLResponse)
def view_all_users(request: Request):
    db: Session = SessionLocal()

    try:
        users = db.query(User).order_by(User.created_at.desc()).all()

        return templates.TemplateResponse(
            request=request,
            name="all_users.html",
            context={
                "users": users
            }
        )

    finally:
        db.close()