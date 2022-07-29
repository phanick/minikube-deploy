from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Python app deployment on Minikube cluster, running!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
