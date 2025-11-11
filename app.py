from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def wisecow():
    quotes = [
        "Don't be afraid to be udderly different!",
        "Moo-tivate yourself every day!",
        "Stay calm and milk the moment!",
        "Be-leaf in yourself, grasshopper!"
    ]
    return f"<h1>🐮 Wisecow Says:</h1><p>{random.choice(quotes)}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

