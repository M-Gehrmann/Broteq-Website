from flask import Flask

app = Flask(__name__)

@app.route("/")
def under_construction():
    return "<h1>Under Construction</h1><p>This site is currently under construction. Please check back soon!</p>"

if __name__ == "__main__":
    app.run()