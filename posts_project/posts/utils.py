import requests
import logging

# Configure logger for this module
logger = logging.getLogger('utils')

BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_posts():
    """
    Fetch all posts from the JSONPlaceholder API.
    """
    try:
        logger.debug("Fetching all posts from API.")
        response = requests.get(f"{BASE_URL}/posts")
        response.raise_for_status()
        logger.info(f"Successfully fetched {len(response.json())} posts.")
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Error fetching posts: {e}")
        return []

def fetch_post_details(post_id):
    """
    Fetch the details of a single post by its ID.
    """
    try:
        logger.debug(f"Fetching details for post ID {post_id}.")
        response = requests.get(f"{BASE_URL}/posts/{post_id}")
        response.raise_for_status()
        logger.info(f"Successfully fetched details for post ID {post_id}.")
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Error fetching post details for ID {post_id}: {e}")
        return {}

def fetch_comments(post_id):
    """
    Fetch all comments for a specific post.
    """
    try:
        logger.debug(f"Fetching comments for post ID {post_id}.")
        response = requests.get(f"{BASE_URL}/posts/{post_id}/comments")
        response.raise_for_status()
        logger.info(f"Successfully fetched comments for post ID {post_id}.")
        return response.json()
    except requests.RequestException as e:
        logger.error(f"Error fetching comments for post ID {post_id}: {e}")
        return []
