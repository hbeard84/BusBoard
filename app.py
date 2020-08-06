from flask import Flask, render_template, url_for, redirect, request
import requests
import os

API_PREFIX = 'http://transportapi.com/v3/uk/bus/stop/'
API_SUFFIX = '/live.json'

APP_ID = os.environ.get('APP_ID')
APP_KEY = os.environ.get('APP_KEY')

BUS_STOPS = ['49000866S','49000866N']

app = Flask(__name__)

@app.route('/')
def index():
    for busStop in BUS_STOPS:
        result = requests.get(API_PREFIX + busStop + API_SUFFIX, params={'app_id':APP_ID,'app_key':APP_KEY})
        print result
    return "Hello"

if __name__ == '__main__':
    app.run()