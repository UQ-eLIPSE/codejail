"""
The REST api server for the coderunner
"""

from flask import Flask, request
from json import dumps
import codejail

# Configure the jail
jail = codejail.configure('python3', '/sandbox/bin/python3')
jail = codejail.get_codejail('python3')

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run_code():
    extra_files = request.get_json()["files"]

    # Convert to a tuple, python2 syntax
    extra_files = [(str(k),str(v)) for k,v in extra_files.iteritems()] 

    # Import the test module
    result = jail.jail_code(code="import test", extra_files=extra_files)

    output = {
        "exitCode": result.status,
        "stdout": result.stdout,
        "stderr": result.stderr
    }

    return dumps(output)
