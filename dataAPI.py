from copy import deepcopy

from flask import abort, jsonify, request
from flask.views import MethodView

# Create a empty data set
datas = []


# Create a MethodView class
class DataAPI(MethodView):

    # Handle GET request with 1 argument named data_id
    def get(self, data_id):
        if data_id is None:
            # Make a hard copy of datas
            _datas = deepcopy(datas)
            for _data in _datas:
                # Replace id with URI
                _data['uri'] = 'http://127.0.0.1:5000/data/' + str(_data['id'])
                del _data['id']
            return jsonify({
                'datas': _datas,
            })

        for _data in datas:
            if _data['id'] is data_id:
                return jsonify({'data': _data})

        # Raise an HTTP 404 error
        abort(404)

    # Handle POST request
    def post(self):
        if request.is_json:
            # Export JSON request to data
            data = request.json
        else:
            # Convert form request to dictionary and expoet it to data
            data = request.form.to_dict()
        if data is None:
            # Raise an HTTP 400 error
            abort(400)
        if 'title' not in data or type(data['title']) is not str:
            # Raise an HTTP 400 error
            abort(400)
        if 'description' not in data or type(data['description']) is not str:
            # Raise an HTTP 400 error
            abort(400)

        # Calculate and assign id
        data['id'] = len(datas) + 1
        datas.append(data)

        # Make a hard copy of data
        _data = deepcopy(data)
        # Replace id with URI
        _data['uri'] = request.base_url + '/' + str(_data['id'])
        del _data['id']

        return jsonify({'data': _data}), 201  # Return HTTP error code 201

    # Handle PUT request with 1 argument named data_id
    def put(self, data_id):
        if request.is_json:
            # Export JSON request to data
            data = request.json
        else:
            # Convert form request to dictionary and expoet it to data
            data = request.form.to_dict()
        if data is None:
            # Raise an HTTP 400 error
            abort(400)
        if 'title' in data and type(data['title']) is not str:
            # Raise an HTTP 400 error
            abort(400)
        if 'description' in data and type(data['description']) is not str:
            # Raise an HTTP 400 error
            abort(400)

        for _data in datas:
            if _data['id'] is data_id:
                if 'title' in data:
                    _data['title'] = data['title']
                if 'description' in data:
                    _data['description'] = data['description']
                return jsonify({'data': _data})

        # Raise an HTTP 404 error
        abort(404)

    # Handle DELETE request with 1 argument named data_id
    def delete(self, data_id):
        for _data in datas:
            if _data['id'] is data_id:
                datas.remove(_data)
                return jsonify({'result': True})

        # Raise an HTTP 404 error
        abort(404)
