from flask import Flask, abort, jsonify, request
from flask.views import MethodView

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@app.errorhandler(400)
def not_found(error):
    return jsonify({
        'error': 'Bad Request',
    }), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Not Found',
    }), 404


@app.errorhandler(405)
def not_found(error):
    return jsonify({
        'error': 'Method Not Allowed',
    }), 405


class RootAPI(MethodView):

    def get(self, task_id):
        if task_id is None:
            return jsonify({
                'response': "'Hello, World",
                'cht': '中文～～～',
                'Method': 'This is GET',
            })
        if task_id is 4:
            abort(404)
        return jsonify({
            'response': task_id,
            'cht': '中文～～～',
            'Method': 'This is GET',
        })

    def post():
        return jsonify({
            'response': "Hello, World!",
            'cht': '中文～～～',
            'Method': 'This is POST',
        })


class PostAPI(MethodView):

    def post(self, iii):
        if iii is None:
            return jsonify({
                'uuu': 123,
            }), 201
        return jsonify(request.form), 201


root_view = RootAPI.as_view('root_api')

app.add_url_rule(
    '/', defaults={'task_id': None}, view_func=root_view, methods=[
        'GET',
    ])

app.add_url_rule(
    '/', view_func=root_view, methods=[
        'POST',
    ])

app.add_url_rule(
    '/<int:task_id>', view_func=root_view, methods=[
        'GET',
    ])

post_view = PostAPI.as_view('post_api')

app.add_url_rule(
    '/post/<iii>', view_func=post_view, methods=[
        'POST',
    ])

if __name__ == '__main__':
    app.run(debug=True)
