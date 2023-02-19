from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('data.json', encoding='UTF-8') as f:
        data = json.load(f)
    return render_template('video_card.html', videos=data)

if __name__ == '__main__':
    app.run()

