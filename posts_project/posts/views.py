from django.shortcuts import render
from .utils import fetch_posts

def post_list(request):
    try:
        posts = fetch_posts()
    except Exception as e:
        posts = []
        print(f"Error fetching posts: {e}")  # Or log this error
    return render(request, 'posts/post_list.html', {'posts': posts})

