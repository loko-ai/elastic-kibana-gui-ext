from flask import Flask, request, jsonify

app = Flask("")


@app.route("/", methods=["POST"])
def test():
    args = request.json.get('args')
    print("ARGS",args)
    json = request.json.get("value")
    print("JSON",json)
    return jsonify(dict(step1="When you open Kibana GUI for the first time, select \"configure manually\" and insert this url:", step2="http://elastic_kibana_elasticsearch:9200", step3="Than, open terminal and run this command to take verification code:", step4="docker exec -it elastic_kibana_kibana bin/kibana-verification-code"))



if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
