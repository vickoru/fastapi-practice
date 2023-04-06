from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get('/hello')
def index():
    return {'message': 'Hello World!'}

# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message': 'All blogs provided'}

@app.get('/blog/all')
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page}'}

@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int,
                valid: bool = True, username: Optional[str] = None):
    return {
        'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}


# @app.get('/blog/{id}', status_code=status.HTTP_404_NOT_FOUND)
# # @app.get('/blog/{id}', status_code=404)
# def get_blog(id: int):
#     if id > 5:
#         return {'error': f'Blog with id {id} not found'}
#     else:
#         return {'message': f'Blog with id {id}'}


@app.get('/blog/{id}', status_code=status.HTTP_200_OK) # Default status code is 200
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog with id {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog with id {id}'}
