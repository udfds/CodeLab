import json

from flask import Flask
from flask import jsonify

app = Flask(__name__)

def __load_drivers():
    with open('drivers.json') as file:
        return json.load(file)

@app.route('/drivers')
def drivers():
    data = __load_drivers()
    return jsonify(data['drivers'])

@app.route('/drivers/<uuid>')
def driver_by_uuid(uuid):
    data = __load_drivers()
    driver = {}
    for _driver in data['drivers']:
        if _driver['uuid'] == uuid:
            driver = _driver
            break
    return jsonify(driver)

if __name__ == '__main__':
    app.run()
