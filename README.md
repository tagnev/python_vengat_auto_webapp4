# Blog Web App

This is a simple Flask web app for managing blog posts. It includes CRUD functionality for creating, reading, updating, and deleting posts.

## Installation

1. Clone this repository
2. Install the required dependencies using `pip install -r requirements.txt`

## Usage

1. Run the Flask app using `python app.py`
2. Access the blog app in your browser at `http://localhost:5000`

## API Endpoints

- `GET /posts` - Get all posts
- `GET /post/<post_id>` - Get a specific post
- `POST /post` - Create a new post
- `PUT /post/<post_id>` - Update an existing post
- `DELETE /post/<post_id>` - Delete a post