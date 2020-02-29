from lib.scraper import WebScraper

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config.Config')


@app.route('/')
def index():
    ws = WebScraper(app.config['URL'])
    ws.parse_page()
    return render_template('index.html', name='World')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
