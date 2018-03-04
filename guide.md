# How to Build an API with Flask

## Environment Setup

1.  Install Python3.
2.  Install Flask via PIPY.
3.  That's it!

## Create a Project

1.  Make a directory.

2.  New a Python file.

3.  Use Flask by adding:

    ```python
    from flask import Flask

    app = Flask(__name__)

    if __name__ == '__main__':
        app.run()

    ```

4.  No more steps!

## Use MethodView to Build API

1.  New a Python file.

2.  Use MethodView by adding:

    ```python
    from flask.views import MethodView

    class DataAPI(MethodView):
        ...

    ```

3.  The method you want to use is as same as the function name inside the class.

## Often Used Methods in Routings

### as_view

#### Imformaton

Converts the class into an actual view function that can be used with the routing system.

#### Usage

```python
# data_view is the view function
# data_api is the view name
data_view = DataAPI.as_view('data_api')
```

### add_url_rule

#### Information

Connects a URL rule.

[Official Documentation of URL Route](http://flask.pocoo.org/docs/0.12/api/#url-route-registrations)

#### Usage

```python
app.add_url_rule(
    '/data/<int:data_id>',      # The URL that this URL Route would handle
    view_func=data_view,        # Which view function is
    methods=[                   # The method that this URL Route would accept
        'get',
        'put',
        'delete',
    ])

```

### errorhandler

#### Information

A decorator that is used to register a function given an error code.

#### Usage

```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Not Found',
    }), 404

```

## Often Used Methods in API

### request

#### Information

The request object used by default in Flask.

This has various methods.

[Official Documentation of request](http://flask.pocoo.org/docs/0.12/api/#flask.Request)

#### Usage

```python
# Indicates if this request is JSON or not.
request.is_json

# If the mimetype is application/json this will contain the parsed JSON data.
# Otherwise this will be None.
request.json

# A MultiDict with the parsed form data from POST or PUT requests.
request.form

# Convert the form data to dictionary
request.form.to_dict()
```

### jsonify

#### Information

Return a json response.

It turns the JSON output into a [`Response`](http://flask.pocoo.org/docs/0.12/api/#flask.Response) object with the *application/json* mimetype.

#### Usage

```python
jsonify({'Your data': your_data})
```

### abort

#### Information

Raises an `HTTPException` for the given status code or WSGI application.

#### Usage

```python
abort(404)
```

