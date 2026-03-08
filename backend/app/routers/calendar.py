from fastapi import APIRouter

router = APIRouter(
    prefix="/calendar",
    tags=["Calendar"]
)

@router.get("/schedule")
def get_schedule():

    return {
        "workout_time": "7:00 AM",
        "meal_reminder": "1:00 PM"
    }