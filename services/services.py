from flask import Flask, request, jsonify

app = Flask("")


@app.route("/", methods=["POST"])
def test():
    args = request.json.get('args')
    print("ARGS",args)
    json = request.json.get("value")
    print("JSON",json)

    string = "When you open Kibana GUI for the first time, select \"configure manually\" and insert this url: \nhttp://elastic-kibana-gui-ext_elasticsearch:9200\nThan, open terminal and run this command to take verification code:\ndocker exec -it elastic-kibana-gui-ext_kibana bin/kibana-verification-code"
    return string.split("\n")


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
