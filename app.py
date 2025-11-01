import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Route to display all plots


@app.route("/")
def home():
    # Look inside the "plots" folder and grab all .png files
    plot_dir = "plots"
    images = [f for f in os.listdir(plot_dir) if f.endswith(".png")]
    return render_template("index.html", images=images)

# Route to serve images from the plots folder


@app.route("/plots/<path:filename>")
def plots(filename):
    return send_from_directory("plots", filename)


if __name__ == "__main__":
    app.run(debug=True)
