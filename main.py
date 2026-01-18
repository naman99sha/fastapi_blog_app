from fastapi import FastAPI, status, HTTPException
from schemas import PostCreate, PostResponse

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "title": 'Post 1',
        "author": "Author 1",
        "content": "Content 1",
        "date_posted": "January 18, 2026"
    },
    {
        "id": 2,
        "title": 'Post 2',
        "author": "Author 2",
        "content": "Content 2",
        "date_posted": "January 18, 2026"
    }
]

@app.get("/")
def home():
    return {"message": "Hello world!"}

@app.get("/api/posts/", response_model=list[PostResponse])
def get_posts():
    return posts

@app.get("/api/posts/{post_id}", response_model=PostResponse)
def get_post_by_id(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Postid not found")

@app.post("/api/posts", response_model=PostCreate, status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate):
    new_id = max(p["id"] for p in posts) + 1 if posts else 1
    new_post = {
        "id": new_id,
        "title": post.title,
        "author": post.author,
        "content": post.content,
        "date_posted": "January 18, 2026" 
    }
    posts.append(new_post)
    return new_post