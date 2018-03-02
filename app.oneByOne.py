from flask import Flask, abort, jsonify, request

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@app.route('/<int:task_id>', methods=['GET'])
def GET_index_with_id(task_id):
    if task_id is 4:
        abort(404)

    return jsonify({
        'response': task_id,
        'cht': '中文～～～',
        'Method': 'This is GET',
    })


@app.route('/', methods=['GET'])
def GET_index():
    return jsonify({
        'response': "'Hello, World",
        'cht': '中文～～～',
        'Method': 'This is GET',
    })


@app.route('/', methods=['POST'])
def POST_index():
    return jsonify({
        'response': "Hello, World!",
        'cht': '中文～～～',
        'Method': 'This is POST',
    })


@app.route('/post/<iii>', methods=['POST'])
def create_task(iii):
    return jsonify(request.form), 201


@app.route('/post', methods=['POST'])
def create_taskl():
    return jsonify({
        'uuu': 123,
    }), 201


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'error': 'Bad Request',
    }), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Not Found',
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        'error': 'Method Not Allowed',
    }), 405


if __name__ == '__main__':
    app.run(debug=True)
