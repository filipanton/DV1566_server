from youtube_api import *
from flask import Flask
from api_calls import get_upcoming
from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__)

scheduler = BackgroundScheduler()
scheduler.add_job(func=get_trailers, trigger="interval", minutes=30)
scheduler.start()


@app.route("/")
def home():
    get_upcoming()
    return "endpoint"


@app.route("/trailers")
def trailers():
    get_trailers()
    return "endpoint"


if __name__ == "__main__":
    app.run(debug=True)
