# =====================================
# PERSONAL AI AGENT SBC
# routes/__init__.py
# =====================================

from .chat import chat

def register_routes(app):
    app.register_blueprint(chat)
