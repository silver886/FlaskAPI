from copy import deepcopy

from flask import abort, jsonify, request
from flask.views import MethodView

datas = []


class DataAPI(MethodView):

    def get(self, data_id):
        if data_id is None:
            _datas = deepcopy(datas)
            for _data in _datas:
                _data['uri'] = 'http://127.0.0.1:5000/data/' + str(_data['id'])
                del _data['id']
            return jsonify({
                'datas': _datas,
            })

        for _data in datas:
            if _data['id'] is data_id:
                return jsonify({'data': _data})

        abort(404)

    def post(self):
        if request.is_json:
            data = request.json
        else:
            data = request.form.to_dict()
        if data is None:
            abort(400)
        if 'title' not in data or type(data['title']) is not str:
            abort(400)
        if 'description' not in data or type(data['description']) is not str:
            abort(400)

        data['id'] = len(datas) + 1
        datas.append(data)

        _data = deepcopy(data)
        _data['uri'] = request.base_url + '/' + str(_data['id'])
        del _data['id']

        return jsonify({'data': _data}), 201

    def put(self, data_id):
        if request.is_json:
            data = request.json
        else:
            data = request.form
        if data is None:
            abort(400)
        if 'title' in data and type(data['title']) is not str:
            abort(400)
        if 'description' in data and type(data['description']) is not str:
            abort(400)

        for _data in datas:
            if _data['id'] is data_id:
                if 'title' in data:
                    _data['title'] = data['title']
                if 'description' in data:
                    _data['description'] = data['description']
                return jsonify({'data': _data})

        abort(404)

    def delete(self, data_id):
        for _data in datas:
            if _data['id'] is data_id:
                datas.remove(_data)
                return jsonify({'result': True})

        abort(404)
