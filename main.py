from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
 
posts: list[dict] = [
    {
        "id": 1,
        "author": "mario",
        "title": "Hello, FastAPI",
        "content": "This is my first post using FastAPI. Next up: routing, schemas, and a database.",
        "date_posted": "2026-01-28T09:15:00",
    },
    {
        "id": 2,
        "author": "corey",
        "title": "Why I like Pydantic",
        "content": "Validation, parsing, and great editor support make it a joy to work with in APIs.",
        "date_posted": "2026-01-27T18:42:10",
    },
    {
        "id": 3,
        "author": "alex",
        "title": "API tips: consistent error shapes",
        "content": "Pick a consistent error response format early; your frontend and logs will thank you.",
        "date_posted": "2026-01-25T12:05:33",
    },
]

# HTML route - include_in_schemas will hide the Rendered HTML routes

@app.get("/",include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"},)

# API routes

@app.get("/api/posts")
def get_post():
    return posts