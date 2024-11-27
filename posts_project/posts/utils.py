import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_posts():
    """
    Fetch all posts from the JSONPlaceholder API.
    """
    response = requests.get(f"{BASE_URL}/posts")
    response.raise_for_status()  # Raise an error for HTTP failures
    return response.json()

def fetch_post_details(post_id):
    """
    Fetch the details of a single post by its ID.
    """
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    response.raise_for_status()
    return response.json()

def fetch_comments(post_id):
    """
    Fetch all comments for a specific post.
    """
    response = requests.get(f"{BASE_URL}/posts/{post_id}/comments")
    response.raise_for_status()
    return response.json()
