from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics
import os
 
app = Flask(__name__)
is_gunicorn = "gunicorn" in os.environ.get("SERVER_SOFTWARE", "")
if is_gunicorn:
    metrics = GunicornInternalPrometheusMetrics(app)
else:
    metrics = PrometheusMetrics(app)

@app.route('/')
def homepage():
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=False)