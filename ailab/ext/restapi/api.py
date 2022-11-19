
from flask import Flask, request

app = Flask(__name__)

# NOTE: we will use PEP8 styling for python code


@app.route('/api/v1/post', methods=['GET'])
def post_generate_image():
    response = """
    <h1>POST Endpoint Index<h1>
    Accepts application/json format.

    <h3>Available Endpoints<h3>
    <li>/api/v1/post/generate/image<li>
    """
    return response

@app.route('/api/v1/post/generate/image', methods=['POST'])
def post_index():
    if request.method == 'POST':
        data = request.get_json()
        print("JSON RESPONSE", data)
    return "Good job, man"

@app.route('/')
def index():
    return "hello world"