import os
from flask import Flask

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mini App</title>
    <style>
        body {
            margin: 0;
            background-color: #111111;
            color: #ffffff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: sans-serif;
            font-size: 28px;
        }
    </style>
</head>
<body>
    <div>HELLO WORLD</div>
</body>
</html>
"""


@app.route("/")
def index():
    return HTML_PAGE


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)