from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head><title>CodSoft Task 1 - Docker App</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>🐳 Dockerized Python Flask Web Application</h1>
            <h2>Created by Yogiraj Solanki</h2>
            <p>Successfully containerized and running inside a Docker Container!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
