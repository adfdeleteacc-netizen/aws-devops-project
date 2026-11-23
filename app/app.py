from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to AWS DevOps Project!</h1>
    <h2>Application deployed successfully.</h2>
    <p>Running on AWS EC2 using Docker.</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "hostname": socket.gethostname(),
        "version": os.getenv("APP_VERSION", "v1")
    }), 200
