from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from my automated EC2 setup! 🚀</h1>
    <p>This application was deployed using EC2 automation.</p>
    """

@app.route("/about")
def about():
    return """
    <h1>About</h1>
    <p>This is my new AWS DevOps project.</p>
    """
@app.route("/hello")
def hello():
    return """
    <h1>Hello from GitHub Actions! 🚀</h1>
    <p>This page was deployed automatically.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)