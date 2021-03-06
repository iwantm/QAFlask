from flask import Flask, Response, request, jsonify
app = Flask(__name__)

information = {'name': 'Someguy Somewhere',
               'age': '32', 'occupation': 'Somejob'}


@app.route('/')
@app.route('/info', methods=['GET'])
def get_text():
    # The API request will return text containing the information as a JSON object.
    return jsonify(information)

# Here we will add functionality to add the information dictionary. The new key is defined in the URL, and the value of the key is in the sent data. We also want to add a check for pre-existence, so that we do not update existing entires (we want to save that for PUT requests).


@app.route('/info/add/<string:key>', methods=['POST'])
def post_text(key):
    # adding the new key-value pair
    if key not in information:
        information[key] = request.get_json()[key]
        return jsonify({"added": request.get_json()})
    else:
        return jsonify({"error": "key exists"})

# We will implement update functionality (PUT request) with the same URL as the route for POST requests, but with a PUT method. Similar to before, we want to check the dictionary for pre-existence so that we only implement changes if the key already exists.


@app.route('/info/update/<string:key>', methods=['PUT'])
def put_text(key):
    if key in information:
        information[key] = request.get_json()[key]
        return jsonify({"updated": request.get_json()})
    else:
        return jsonify({"error": "key doesn't exist"})

# Finally, we add a function so that if the request is DELETE, we delete that key from the dictionary.


@app.route('/info/delete/<string:key>', methods=['DELETE'])
def delete_text(key):
    if key in information:
        information.pop(key)
        return jsonify({"deleted": key})
    else:
        return jsonify({"error": "key doesn't exist"})


# Make app callabale from the command line
if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
