from flask import Flask, request, jsonify
import baseball_scraper as statcast


app = Flask(__name__)


@app.route("/")
def index():
    return


if __name__ == "__main__":
    app.run()

