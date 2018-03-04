from dataAPI import DataAPI
from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

data_view = DataAPI.as_view('data_api')

app.add_url_rule(
    '/datas', defaults={'data_id': None}, view_func=data_view, methods=[
        'get',
    ])

app.add_url_rule(
    '/data', view_func=data_view, methods=[
        'post',
    ])

app.add_url_rule(
    '/data/<int:data_id>',
    view_func=data_view,
    methods=[
        'get',
        'put',
        'delete',
    ])


@app.errorhandler(400)
def not_found(error):
    return jsonify({
        'error': 'Bad Request',
    }), 400


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        'error': 'Unauthorized',
    }), 401


@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        'error': 'Forbidden',
    }), 403


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


@app.errorhandler(406)
def not_acceptable(error):
    return jsonify({
        'error': 'Not Acceptable',
    }), 406


if __name__ == '__main__':
    app.run()
