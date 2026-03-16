from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, servidor CI/CD actualizado con webhook!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
