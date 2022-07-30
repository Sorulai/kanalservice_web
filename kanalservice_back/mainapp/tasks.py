import os

import requests
from celery import shared_task
import xml.etree.ElementTree as ET

from kanalservice_back.celery import app

JSON_PATH = 'mainapp/json'


@app.task
def get_currency_beat_celery():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url).content
    tree = ET.fromstring(response)
    for i in tree:
        if i.attrib.get('ID') == 'R01235':
            for j in i:
                if j.tag == 'Value':
                    with open(os.path.join(JSON_PATH, 'valute.txt'), 'w') as f:
                        f.write(j.text)
