from services.nfs_services import NfsServices

import flask
from flask import request, jsonify


def main():
    app = flask.Flask(__name__)

    nfs_services = NfsServices()

    # A route to return all of the available entries in our catalog.
    @app.route('/api/nfs/all', methods=['GET'])
    def api_all():
        result = nfs_services.GetAllNfs()

        return jsonify(result)

    @app.route('/api/nfs/single', methods=['GET'])
    def api_id():
        # Check if an ID was provided as part of the URL.
        # If ID is provided, assign it to a variable.
        # If no ID is provided, display an error in the browser.
        id = 0

        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            return "Error: No id field provided. Please specify an id."

        result = nfs_services.GetSingle(id)

        # Use the jsonify function from Flask to convert our list of
        # Python dictionaries to the JSON format.
        return jsonify(result)

    app.run()


if __name__ == "__main__":
    main()
