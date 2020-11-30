from flask import Flask
from api_calls import get_upcoming

app = Flask(__name__)


@app.route("/")
def home():
    get_upcoming()
    return "endpoint"



if __name__ == "__main__":
    app.run(debug=True)
    





