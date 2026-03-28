from fastapi import FastAPI

app = FastAPI()

courses = [
    {"id": 1, "title": "HTML & CSS Basics", "duration": "4 weeks"},
    {"id": 2, "title": "JavaScript for Beginners", "duration": "6 weeks"},
    {"id": 3, "title": "Python Fundamentals", "duration": "5 weeks"},
]

@app.get("/")
def read_root():
    return {"message": "Yes the 8hrs api is live"}


@app.get("/courses")
def get_courses():
    return {"courses": courses}

@app.get("/courses/{course_id}")
def get_course(course_id: int):
    course = next((c for c in courses if c["id"] == course_id), None)
    if not course:
        return {"error": "Course not found"}
    return course