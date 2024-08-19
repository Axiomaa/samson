#Flask as webserver
from flask import Flask, send_from_directory
# keep_alive runs from a separate thread  
from threading import Thread

app = Flask('', static_url_path='', static_folder='.')

@app.route('/')
def home():
  return send_from_directory('', 'index.html')

def run():
  app.run(host = '0.0.0.0', port = 8080)

def keep_alive():
  t = Thread(target = run)
  t.start()