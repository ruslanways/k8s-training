import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({
        "message": os.environ.get("APP_MESSAGE", "hello"),
        "color": os.environ.get("APP_COLOR", "gray"),
        "pod": socket.gethostname(),
        "secret_loaded": bool(os.environ.get("API_KEY")),
    })


@app.route("/healthz")
def healthz():
    # liveness: is the process itself alive?
    return jsonify({"status": "alive"}), 200


@app.route("/ready")
def ready():
    # readiness: is it ready to take traffic?
    return jsonify({"status": "ready"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
