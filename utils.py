from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")   # ✅ Use non-GUI backend (avoids Tkinter errors)


def load_data(path):
    """
    Load and clean dataset.
    Renames columns for consistency so the rest of the app
    can always use 'Annual_Income' and 'Spending_Score'.
    """
    if not os.path.exists(path):
        print(f"⚠️ Dataset not found at {path}")
        return None

    df = pd.read_csv(path)

    # Rename columns for consistency
    df = df.rename(columns={
        "Income": "Annual_Income",
        "Spend": "Spending_Score"
    })

    return df


def run_clustering(df, n_clusters, plots_dir):
    """
    Run KMeans clustering, save updated scatter plot and cluster summary.
    Returns the updated dataframe with cluster labels.
    """
    # Select features
    X = df[["Age", "Annual_Income", "Spending_Score"]]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Run clustering
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df["Cluster"] = model.fit_predict(X_scaled)

    # Save scatter plot
    plt.figure(figsize=(6, 4))
    df.plot.scatter(
        x="Annual_Income",
        y="Spending_Score",
        c="Cluster",
        colormap="viridis"
    )
    plt.title(f"Customer Segmentation (k={n_clusters})")
    plot_path = os.path.join(plots_dir, "updated_clusters.png")
    plt.savefig(plot_path)
    plt.close()

    # Save cluster summary
    cluster_summary = df.groupby("Cluster").agg({
        "Age": "mean",
        "Annual_Income": "mean",
        "Spending_Score": "mean"
    }).reset_index()

    # ✅ Round values for readability
    cluster_summary = cluster_summary.round({
        "Age": 1,              # 1 decimal place
        "Annual_Income": 0,    # whole numbers
        "Spending_Score": 0    # whole numbers
    })

    # ✅ Format numbers with commas for presentation
    cluster_summary["Annual_Income"] = cluster_summary["Annual_Income"].map(
        lambda x: f"{int(x):,}")
    cluster_summary["Spending_Score"] = cluster_summary["Spending_Score"].map(
        lambda x: f"{int(x):,}")

    summary_path = os.path.join(plots_dir, "cluster_summary.csv")
    cluster_summary.to_csv(summary_path, index=False)

    return df
