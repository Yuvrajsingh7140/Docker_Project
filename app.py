from flask import Flask, render_template, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'running',
        'timestamp': datetime.now().isoformat(),
        'message': 'Mini Python app is working!'
    })

@app.route('/api/health')
def health():
    return jsonify({'health': 'OK'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)