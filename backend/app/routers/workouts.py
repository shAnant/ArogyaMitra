from fastapi import APIRouter
from datetime import datetime

from app.services.calendar_service import CalendarService


router = APIRouter(prefix="/calendar", tags=["Calendar"])


@router.post("/schedule-workout")
def schedule_workout(access_token: str):

    calendar = CalendarService(access_token)

    event = calendar.create_workout_event(
        "ArogyaMitra Workout Session",
        datetime.now()
    )

    return event

@router.get("/plan")
def get_workout_plan():

    return {
        "exercises": [
            {
                "name": "Push Ups",
                "sets": 3,
                "reps": 10,
                "video": "https://example.com/pushup.mp4"
            },
            {
                "name": "Squats",
                "sets": 3,
                "reps": 12,
                "video": "https://example.com/squat.mp4"
            }
        ]
    }


@router.post("/start")
def start_workout(data: dict):
    return {"message": "Workout started"}


@router.post("/complete")
def complete_workout(data: dict):
    return {"message": "Workout completed"}