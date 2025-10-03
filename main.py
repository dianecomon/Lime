from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/bike_data")
def bike_data():
    # Get current time in UTC
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    return f"<html><body><h1>Hello</h1><p>Current time: {now}</p></body></html>"

# Render looks for 'app' by default, so no need for __main__ guard
