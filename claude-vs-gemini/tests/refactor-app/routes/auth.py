from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)

TOKEN_EXPIRY = 3600
MAX_LOGIN_ATTEMPTS = 5


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password required"}), 400

    # Fake auth check
    if data["username"] == "admin" and data["password"] == "password":
        return jsonify({
            "token": "Bearer secret-token-123",
            "expires_in": TOKEN_EXPIRY
        })

    return jsonify({"error": "Invalid credentials"}), 401


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password required"}), 400

    if len(data["username"]) > 30:
        return jsonify({"error": "Username too long"}), 400

    return jsonify({"message": "User registered", "username": data["username"]}), 201


@auth_bp.route("/logout", methods=["POST"])
def logout():
    token = request.headers.get("Authorization")
    if not token or token != "Bearer secret-token-123":
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({"message": "Logged out successfully"})


@auth_bp.route("/profile", methods=["GET"])
def get_auth_profile():
    token = request.headers.get("Authorization")
    if not token or token != "Bearer secret-token-123":
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({
        "username": "admin",
        "token_expires_in": TOKEN_EXPIRY,
        "max_login_attempts": MAX_LOGIN_ATTEMPTS
    })


@auth_bp.route("/change-password", methods=["PUT"])
def change_password():
    token = request.headers.get("Authorization")
    if not token or token != "Bearer secret-token-123":
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data or not data.get("new_password"):
        return jsonify({"error": "New password required"}), 400

    return jsonify({"message": "Password changed"})
