from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

queues = {}


@app.route('/<name>/_add')
def enqueue(name="default"):
    msg = request.args.get('msg', "", type=str)
    time = request.args.get('time', "", type=str)
    if name in queues:
        queues[name].append({"time": time, "msg": msg})
    else:
        queues[name] = [{"time": time, "msg": msg}]
    return jsonify(status="Success")


@app.route('/<name>/_top')
@app.route('/<name>/_top/<int:n>')
def show(name="default", n=5):
    if name in queues:
        msgs = queues[name][-n:]
    else:
        msgs = []
    return jsonify(msgs=msgs)


@app.route('/')
def hello_world():
    return render_template('index.html', title="Messaging Test")


if __name__ == '__main__':
    app.run(port=26220)
