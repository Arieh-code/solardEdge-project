from django.test import TestCase
from unittest.mock import patch
from posts.utils import fetch_posts, fetch_post_details, fetch_comments

class UtilsTests(TestCase):
    @patch('posts.utils.requests.get')
    def test_fetch_posts(self, mock_get):
        # Mock response data
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'id': 1, 'title': 'Test Post'}]

        # Call the function
        posts = fetch_posts()

        # Assertions
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]['title'], 'Test Post')
        mock_get.assert_called_once_with('https://jsonplaceholder.typicode.com/posts')

    @patch('posts.utils.requests.get')
    def test_fetch_post_details(self, mock_get):
        # Mock response data
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'id': 1, 'title': 'Test Post'}

        # Call the function
        post = fetch_post_details(1)

        # Assertions
        self.assertEqual(post['id'], 1)
        self.assertEqual(post['title'], 'Test Post')
        mock_get.assert_called_once_with('https://jsonplaceholder.typicode.com/posts/1')

    @patch('posts.utils.requests.get')
    def test_fetch_comments(self, mock_get):
        # Mock response data
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{'id': 1, 'body': 'Test Comment'}]

        # Call the function
        comments = fetch_comments(1)

        # Assertions
        self.assertEqual(len(comments), 1)
        self.assertEqual(comments[0]['body'], 'Test Comment')
        mock_get.assert_called_once_with('https://jsonplaceholder.typicode.com/posts/1/comments')
