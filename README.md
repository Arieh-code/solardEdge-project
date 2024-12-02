# **Django Posts and Comments Viewer**

This Django application interacts with the JSONPlaceholder API to display posts and their associated comments. It demonstrates Django's core functionality, external API integration, and basic frontend rendering.

---

## **Features**

1. **List All Posts:**

   - Displays a list of posts retrieved from the JSONPlaceholder API.
   - Each post shows the title and a snippet of the body.
   - Clicking on a post navigates to its detail page.

2. **Post Detail View:**

   - Displays the full content of a selected post (title and body).
   - Lists all comments associated with the post.
   - Each comment includes the author’s name, email, and comment text, formatted for readability.

3. **Error Handling:**

   - Gracefully handles API failures and displays appropriate messages when data cannot be retrieved.

4. **Logging:**
   - Logs API interactions and errors for better monitoring and debugging.

---

## **Technologies Used**

- **Backend:**

  - Django 5.1.3
  - Python 3.12.4
  - `requests` library for API interaction

- **Frontend:**

  - HTML for templates
  - Basic Django templating system

- **Utilities:**
  - Custom utility functions for external API calls
  - Logging for debugging and monitoring

---

## **Installation**

### **Prerequisites**

- Python 3.10 or higher
- `pip` package manager

### **Setup Steps**

1. Clone the repository:
   ```bash
   git clone https://github.com/username/posts_project.git
   cd posts_project
   ```
