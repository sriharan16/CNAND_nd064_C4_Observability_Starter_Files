from flask import Flask, render_template, request, jsonify

import os
import logging
# import pymongo
from flask_pymongo import PyMongo
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

# from jaeger_client import Config
# from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
from opentelemetry import trace
# from opentelemetry.exporter import jaeger
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
# from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.trace import TracerProvider
# from opentelemetry.sdk.trace.export import (
#     ConsoleSpanExporter,
#     SimpleExportSpanProcessor,
# )
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

trace.set_tracer_provider(TracerProvider(resource=Resource.create({SERVICE_NAME: "backend-service"})))
jaeger_exporter = JaegerExporter()
# Create a BatchSpanProcessor and add the exporter to it
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(
    span_processor
)

trace.get_tracer_provider().add_span_processor(span_processor)

tracer = trace.get_tracer(__name__)

app = Flask(__name__)

is_gunicorn = "gunicorn" in os.environ.get("SERVER_SOFTWARE", "")
if is_gunicorn:
    metrics = GunicornInternalPrometheusMetrics(app)
else:
    metrics = PrometheusMetrics(app)
FlaskInstrumentor().instrument_app(app, excluded_urls="metrics")

app.config['MONGO_DBNAME'] = 'example-mongodb'
app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'

mongo = PyMongo(app)

# def init_tracer(service):
#     logging.getLogger('').handlers = []
#     logging.basicConfig(format='%(message)s', level=logging.DEBUG)

#     config = Config(
#         config={
#             'sampler': {
#                 'type': 'const',
#                 'param': 1,
#             },
#             'logging': True,
#         },
#         service_name=service,
#     )

#     # this call also sets opentracing.tracer
#     return config.initialize_tracer()

# tracer = init_tracer('backend-service')


@app.route('/')
def homepage():
    with tracer.start_as_current_span('homepage'):
        return "Hello World"


@app.route('/api')
def my_api():
    with tracer.start_as_current_span('api'):
        answer = "something"
        return jsonify(repsonse=answer)

@app.route('/star', methods=['POST'])
def add_star():
  star = mongo.db.stars
  name = request.json['name']
  distance = request.json['distance']
  star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})

if __name__ == "__main__":
    app.run()
