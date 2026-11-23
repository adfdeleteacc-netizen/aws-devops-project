from flask import Flask, jsonify, render_template
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "hostname": socket.gethostname(),
        "version": os.getenv("APP_VERSION", "latest")
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
