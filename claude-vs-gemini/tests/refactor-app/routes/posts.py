from flask import Blueprint, request, jsonify

posts_bp = Blueprint("posts", __name__)

POSTS_PER_PAGE = 10
MAX_POST_LENGTH = 5000

# In-memory store for demo
posts_store = []


@posts_bp.route("/", methods=["GET"])
def list_posts():
    token = request.headers.get("Authorization")
    if not token or token != "Bearer secret-token-123":
        return jsonify({"error": "Unauthorized"}), 401

    page = request.args.get("page", 1, type=int)
    start = (page - 1) * POSTS_PER_PAGE
    end = start + POSTS_PER_PAGE
    return jsonify({"posts": posts_store[start:end], "page": page})


@posts_bp.route("/", methods=["POST"])
def create_post():
    token = request.headers.get("Authorization")
    if not token or token != "Bearer secret-token-123":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data or not data.get("title"):
        return "Error: title is required", 400

    if len(data.get("content", "")) > MAX_POST_LENGTH:
        return "Error: post content too long", 400

    post = {"id": len(posts_store) + 1, "title": data["title"], "content": data.get("content", "")}
    posts_store.append(post)
    return jsonify(post), 201


@posts_bp.route("/<int:post_id>", methods=["GET"])
def get_post(post_id):
    token = request.headers.get("Authorization")
    if not token or token != "Bearer secret-token-123":
        return jsonify({"error": "Unauthorized"}), 401

    for post in posts_store:
        if post["id"] == post_id:
            return jsonify(post)
    return "Error: post not found", 404


@posts_bp.route("/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    token = request.headers.get("Authorization")
    if not token or token != "Bearer secret-token-123":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data:
        return "Error: no data provided", 400

    if len(data.get("content", "")) > MAX_POST_LENGTH:
        return "Error: post content too long", 400

    for post in posts_store:
        if post["id"] == post_id:
            post["title"] = data.get("title", post["title"])
            post["content"] = data.get("content", post["content"])
            return jsonify(post)
    return "Error: post not found", 404


@posts_bp.route("/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    token = request.headers.get("Authorization")
    if not token or token != "Bearer secret-token-123":
        return jsonify({"error": "Unauthorized"}), 401

    for i, post in enumerate(posts_store):
        if post["id"] == post_id:
            posts_store.pop(i)
            return jsonify({"message": "Post deleted"})
    return "Error: post not found", 404
