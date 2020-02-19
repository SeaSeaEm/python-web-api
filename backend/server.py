from services.nfs_services import NfsServices
from model.nfs import *

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

    @app.route('/api/nfs/single', methods=['POST'])
    def api_id():
        obj = request.json
        print(obj)

        result = nfs_services.GetById(obj["uuid"])

        import json
        return json.dumps(result, default=str)

    @app.route('/api/nfs', methods=['POST'])
    def api_post():
        obj = request.json
        import uuid 

        quotas = Quota(value=obj["quotas"]["value"],
                       amount=obj["quotas"]["amount"])
        nfs = Nfs(id=str(uuid.uuid1()), number=obj["number"],
                  name=obj["name"], quotas=quotas.__dict__)
                  
        data = nfs.__dict__
        print(data)

        nfs_services.Add(data)

        result = nfs_services.GetById(nfs.id)
        import json
        result = json.dumps(result, default=str)
        print(result)

        return result

    app.run()


if __name__ == "__main__":
    main()
