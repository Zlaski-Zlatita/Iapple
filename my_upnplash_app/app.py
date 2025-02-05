from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

UNSPLASH_API_KEY = 'YOUR_UNSPLASH_API_KEY' 
UNSPLASH_API_URL = 'https://api.unsplash.com/search/photos'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    page = request.args.get('page', 1)

    response = requests.get(
        UNSPLASH_API_URL,
        params={
            'query': query,
            'page': page,
            'client_id': UNSPLASH_API_KEY
        }
    )

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Failed to fetch data'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
