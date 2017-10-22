from flask import Flask, request
from openapi_spec_validator import openapi_v3_spec_validator

app = Flask(__name__)

@app.route("/", methods=['POST'])
def validate():
    for error in openapi_v3_spec_validator.iter_errors(request.data):
        return "FAIL", HTTP_400_BAD_REQUEST
    return "OK", HTTP_200_OK

if __name__ == '__main__':
    app.run(host='0.0.0.0')
