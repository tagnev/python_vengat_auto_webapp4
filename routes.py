from flask import Blueprint, request, jsonify
from models import db, Post

blog_routes = Blueprint("blog", __name__)

@blog_routes.route("/posts", methods=["GET"])
def get_all_posts():
    posts = Post.query.all()
    return jsonify([post.__dict__ for post in posts])

@blog_routes.route("/post/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify(post.__dict__)

@blog_routes.route("/post", methods=["POST"])
def create_post():
    data = request.get_json()
    new_post = Post(title=data["title"], content=data["content"])
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.__dict__)

@blog_routes.route("/post/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json()
    post.title = data["title"]
    post.content = data["content"]
    db.session.commit()
    return jsonify(post.__dict__)

@blog_routes.route("/post/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted"})