from flask import Flask, render_template, url_for, redirect, request
import requests
import os

API_PREFIX = 'http://transportapi.com/v3/uk/bus/stop/'
API_SUFFIX = '/live.json'

APP_ID = os.environ.get('APP_ID')
APP_KEY = os.environ.get('APP_KEY')

# BUS_STOPS = ['490008660S', '490008660N']
BUS_STOPS = ['490008660S']

app = Flask(__name__)


@app.route('/')
def index():
    buses = []
    for busStop in BUS_STOPS:
        result = requests.get(API_PREFIX + busStop + API_SUFFIX, params={'app_id': APP_ID, 'app_key': APP_KEY})
        timetable = result.json()['departures']
        for key in timetable:
            buses.append(timetable[key][0])
    return f'{buses}'


if __name__ == '__main__':
    app.run()
