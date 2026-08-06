from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    return "PERSONAL AI AGENT SBC is running successfully."

if __name__ == "__main__":
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Personal AI Agent for SBC"

if __name__ == "__main__":
    app.run(debug=True)
