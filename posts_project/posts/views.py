from django.shortcuts import render
from .utils import fetch_posts, fetch_comments, fetch_post_details
from django.http import Http404

def post_list(request):
    try:
        posts = fetch_posts()
    except Exception as e:
        posts = []
        print(f"Error fetching posts: {e}")  # Or log this error
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    """
    View to display the details of a single post.
    """
    try:
        post = fetch_post_details(post_id)  # Fetch the post details
        comments = fetch_comments(post_id)  # Fetch comments for the post
    except Exception as e:
        print(f"Error fetching post or comments: {e}")  # Log the error (or use logging)
        raise Http404("Post not found.")
    
    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})

