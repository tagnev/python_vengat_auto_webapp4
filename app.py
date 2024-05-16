from flask import Flask
from routes import blog_routes

app = Flask(__name__)

app.register_blueprint(blog_routes)

if __name__ == "__main__":
    app.run()