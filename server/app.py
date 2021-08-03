from flask import Flask
from sniff import sniffPack

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    return sniffPack()


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')