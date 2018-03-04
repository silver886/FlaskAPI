from dataAPI import DataAPI
from flask import Flask, jsonify

# Start Flask
app = Flask(__name__)
# Minimize the response size
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# Convert DataAPI to view function
data_view = DataAPI.as_view('data_api')

# Handle GET at '/datas' with data_view passing data_id with None
app.add_url_rule(
    '/datas', defaults={'data_id': None}, view_func=data_view, methods=[
        'get',
    ])

# Handle POST at '/data' with data_view
app.add_url_rule(
    '/data', view_func=data_view, methods=[
        'post',
    ])

# Handle GET, PUT, and DELETE at'/data/<int:data_id>' with data_view
app.add_url_rule(
    '/data/<int:data_id>',
    view_func=data_view,
    methods=[
        'get',
        'put',
        'delete',
    ])


# Handle HTTP error code 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'error': 'Bad Request',
    }), 400  # Return HTTP error code 400


# Handle HTTP error code 401
@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        'error': 'Unauthorized',
    }), 401  # Return HTTP error code 401


# Handle HTTP error code 403
@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        'error': 'Forbidden',
    }), 403  # Return HTTP error code 403


# Handle HTTP error code 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Not Found',
    }), 404  # Return HTTP error code 404


# Handle HTTP error code 405
@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        'error': 'Method Not Allowed',
    }), 405  # Return HTTP error code 405


# Handle HTTP error code 406
@app.errorhandler(406)
def not_acceptable(error):
    return jsonify({
        'error': 'Not Acceptable',
    }), 406  # Return HTTP error code 406


if __name__ == '__main__':
    app.run()
