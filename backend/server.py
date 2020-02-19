from services.nfs_services import NfsServices
from model.nfs import *

import flask
import json
from flask import request, jsonify
from flask_cors import CORS, cross_origin


def main():
    app = flask.Flask(__name__)
    app.config['CORS_HEADERS'] = 'Content-Type'
    
    cors = CORS(app)

    nfs_services = NfsServices()

    # A route to return all of the available entries in our catalog.
    @app.route('/api/nfs/all', methods=['GET'])
    @cross_origin()
    def api_all():
        result = nfs_services.GetAllNfs()

        return jsonify(result)

    @app.route('/api/nfs/single', methods=['POST'])
    @cross_origin()
    def api_id():
        obj = request.json

        result = nfs_services.GetById(obj["uuid"])

        return json.dumps(result, default=str)

    @app.route('/api/nfs', methods=['POST'])
    @cross_origin()
    def api_post():
        obj = request.json
        import uuid

        quotas = Quota(value=obj["quotas"]["value"],
                        amount=obj["quotas"]["amount"])
        nfs = Nfs(id=str(uuid.uuid1()), number=obj["number"],
                    name=obj["name"], quotas=quotas.__dict__)

        data = nfs.__dict__
        nfs_services.Add(data)

        result = nfs_services.GetById(nfs.id)

        if result is not None:
            return {"status": "success"}

        return {"status": "failed"}

    app.run()


if __name__ == "__main__":
    main()
