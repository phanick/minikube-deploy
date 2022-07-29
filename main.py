from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Python app running on Minikube cluster!!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
