from flask import Flask, request, jsonify
from EndpointHandler import handle_action

app = Flask(__name__)

@app.route('/<string:repoID>/<string:action>')
def index(repoID, action):
    response, code = handle_action(repoID, action)
    print(repoID)
    print(action)
    print(response)
    print(code)
    response  =  "OK: Authorized" if code == 200 else "Not OK: Not Allowed"
    return jsonify({"response": response}), code

if __name__ == '__main__':
    app.run()