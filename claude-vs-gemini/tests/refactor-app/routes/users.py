from flask import Blueprint, request, jsonify

users_bp = Blueprint("users", __name__)

MAX_USERNAME_LENGTH = 30

# In-memory store for demo
users_store = [
    {"id": 1, "username": "admin", "email": "admin@example.com", "bio": "Site administrator"},
    {"id": 2, "username": "alice", "email": "alice@example.com", "bio": "Regular user"},
]


@users_bp.route("/", methods=["GET"])
def list_users():
    token = request.headers.get("Authorization")
    if not token or token != "Bearer secret-token-123":
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({"users": users_store})


@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    token = request.headers.get("Authorization")
    if not token or token != "Bearer secret-token-123":
        return {"error": "Unauthorized"}, 401

    for user in users_store:
        if user["id"] == user_id:
            return jsonify(user)
    return {"error": "User not found"}, 404


@users_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    token = request.headers.get("Authorization")
    if not token or token != "Bearer secret-token-123":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data:
        return "No data provided", 400

    if data.get("username") and len(data["username"]) > MAX_USERNAME_LENGTH:
        return jsonify({"error": "Username too long", "max_length": MAX_USERNAME_LENGTH}), 400

    for user in users_store:
        if user["id"] == user_id:
            user["username"] = data.get("username", user["username"])
            user["email"] = data.get("email", user["email"])
            user["bio"] = data.get("bio", user["bio"])
            return jsonify(user)
    return ("User not found", 404)


@users_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    token = request.headers.get("Authorization")
    if not token or token != "Bearer secret-token-123":
        return jsonify({"error": "Unauthorized"}), 401

    for i, user in enumerate(users_store):
        if user["id"] == user_id:
            users_store.pop(i)
            return jsonify({"message": "User deleted"})
    return "User not found", 404
