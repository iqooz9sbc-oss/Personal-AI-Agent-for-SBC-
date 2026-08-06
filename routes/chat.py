from flask import Blueprint, request, jsonify
from services.ai import get_ai_response

chat = Blueprint("chat", __name__)

@chat.route("/chat", methods=["POST"])
def chat_api():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No data received."
        }), 400

    message = data.get("message", "").strip()

    if message == "":
        return jsonify({
            "error": "Message cannot be empty."
        }), 400

    response = get_ai_response(message)

    return jsonify({
        "reply": response
    })
