import os
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route("/1")
def fallOn():
    return render_template('index.html', rendered_diagram = "/diagram")  

@app.route("/diagram")
def diagram():
    return render_template('diagram.html')  

    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    host = '127.0.0.1' if port == 5000 else '0.0.0.0'
    app.run(host=host, port=port, debug = (port == 5000))