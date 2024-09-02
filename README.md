# Noteification - Final Project for HarvardX CS50W: Web Programming with Python and JavaScript

## Overview
**Noteification** is a dynamic note-taking web application that allows users to create, edit, and manage notes seamlessly. The application is built using Django for the backend and JavaScript for interactivity on the frontend. It is fully mobile-responsive, ensuring an optimal user experience across different devices.

## Distinctiveness and Complexity
This project is different from anything we've built before. It's not a social media app or an e-commerce site, and it's also unique compared to projects from previous years.

As for complexity, I used Django with multiple models (which I explain below) and included a JavaScript file for the frontend. Plus, the whole web application is responsive, so it works well on both mobile phones and computers.

## Features
- User registration and login functionality.
- Note creation, editing, and deletion.
- Tabbed interface to toggle between notes and fun facts.
- Fetching and displaying random fun facts from an external API.
- Mobile responsiveness for a seamless experience on all devices.

## Technologies Used
- **Python (Django)**: Backend framework handling core functionalities.
- **JavaScript**: Enhances the user interface.
- **HTML/CSS**: Structures and styles the application.
- **SQLite**: Default database for storing user data and notes.

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/noteification.git
    cd noteification
    ```
2. **Install project dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Make and apply migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
4. **Create a superuser (optional)**:
    ```bash
    python manage.py createsuperuser
    ```
5. **Run the server**:
    ```bash
    python manage.py runserver
    ```
6. **Access the application**: Open your web browser and go to `http://127.0.0.1:8000/`.

## File Structure

- **`app/views.py`**: Handles user requests and renders the necessary pages.
- **`app/templates/app`**: Contains the HTML files for the application.
  - **`layout.html`**: Base file that other pages extend, includes CSS and JS files.
  - **`index.html`**: Displays the user's notes and a bonus section for fun facts.
  - **`edit.html`**: Page for creating and editing notes.
  - **`login.html`**: User login page.
  - **`register.html`**: User registration page.
- **`app/static/app`**: Contains the static files, including JavaScript and CSS.
  - **`index.js`**: Manages tab functionality and fetching fun facts from an API.
  - **`styles.css`**: Styles the application and ensures mobile responsiveness.
- **`requirements.txt`**: Lists the Python packages required to run the project.

## Additional Information
- **API Integration**: The application fetches random fun facts from [uselessfacts.jsph.pl](https://uselessfacts.jsph.pl/) and displays them in the bonus tab.
- **Responsive Design**: The application is mobile responsive.