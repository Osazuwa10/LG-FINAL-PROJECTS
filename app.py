import os
from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import pandas as pd
from utils import load_data, run_clustering   # ✅ helper functions

app = Flask(__name__)

# =========================
# 🔧 Configurable Settings
# =========================
DATA_PATH = "lg_customer_data.csv"
PLOTS_DIR = "plots"

# Load dataset
df = load_data(DATA_PATH)

# Ensure plots directory exists
os.makedirs(PLOTS_DIR, exist_ok=True)


# =========================
# 🌐 Routes
# =========================

@app.route("/", methods=["GET"])
def home():
    """Home page: display plots and cluster summary."""
    images = [f for f in os.listdir(PLOTS_DIR) if f.endswith(".png")]

    # Load cluster summary if available
    summary_path = os.path.join(PLOTS_DIR, "cluster_summary.csv")
    cluster_summary = None
    if os.path.exists(summary_path):
        cluster_summary = pd.read_csv(summary_path).to_html(
            classes="table table-striped", index=False)

    return render_template("index.html", images=images, cluster_summary=cluster_summary)


@app.route("/plots/<path:filename>")
def plots(filename):
    """Serve images from the plots/ folder."""
    return send_from_directory(PLOTS_DIR, filename)


@app.route("/update", methods=["POST"])
def update():
    """Update clustering with new number of clusters."""
    global df
    if df is None:
        return "⚠️ Dataset not found. Cannot update clusters.", 500

    n_clusters = int(request.form["clusters"])
    df = run_clustering(df, n_clusters, PLOTS_DIR)
    return redirect(url_for("home"))


@app.route("/download_summary")
def download_summary():
    """Allow user to download the cluster summary CSV."""
    return send_from_directory(PLOTS_DIR, "cluster_summary.csv", as_attachment=True)


# =========================
# 🚀 Run App
# =========================
if __name__ == "__main__":
    app.run(debug=True)
