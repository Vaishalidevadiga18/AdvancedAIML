'''import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, adjusted_rand_score
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris(as_frame=True)
df = iris.frame
df.to_csv("iris.csv", index=False)

# -------------------------------
# Step 1: Load dataset
# -------------------------------



# Drop non-numeric columns if any
X = df.select_dtypes(include=[np.number])

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Choose number of clusters (e.g., 3)
k = 3

# -------------------------------
# Step 2: Apply KMeans Clustering
# -------------------------------
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans_labels = kmeans.fit_predict(X_scaled)

# -------------------------------
# Step 3: Apply EM Algorithm (Gaussian Mixture)
# -------------------------------
gmm = GaussianMixture(n_components=k, random_state=42)
gmm_labels = gmm.fit_predict(X_scaled)

# -------------------------------
# Step 4: Compare Results
# -------------------------------
silhouette_kmeans = silhouette_score(X_scaled, kmeans_labels)
silhouette_gmm = silhouette_score(X_scaled, gmm_labels)

print("===== Clustering Results =====")
print(f"K-Means Silhouette Score: {silhouette_kmeans:.4f}")
print(f"EM (GMM) Silhouette Score: {silhouette_gmm:.4f}")

# If ground-truth labels exist in dataset (optional)
if 'label' in df.columns:
    true_labels = df['label']
    ari_kmeans = adjusted_rand_score(true_labels, kmeans_labels)
    ari_gmm = adjusted_rand_score(true_labels, gmm_labels)
    print(f"K-Means Adjusted Rand Index: {ari_kmeans:.4f}")
    print(f"EM (GMM) Adjusted Rand Index: {ari_gmm:.4f}")

# -------------------------------
# Step 5: Comment on Results
# -------------------------------
if silhouette_kmeans > silhouette_gmm:
    print("\nK-Means produced better-defined clusters than EM (GMM).")
elif silhouette_gmm > silhouette_kmeans:
    print("\nEM (GMM) produced better-defined clusters than K-Means.")
else:
    print("\nBoth algorithms produced similar clustering quality.")
'''
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, adjusted_rand_score
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# -------------------------------
# Step 1: Load dataset (Iris)
# -------------------------------
iris = load_iris(as_frame=True)
df = iris.frame  # includes both features and target column

# Drop non-numeric columns if any (all are numeric here)
X = df.select_dtypes(include=[np.number]).drop(columns=["target"])

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Choose number of clusters (known = 3 for Iris)
k = 3

# -------------------------------
# Step 2: Apply KMeans Clustering
# -------------------------------
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans_labels = kmeans.fit_predict(X_scaled)

# -------------------------------
# Step 3: Apply EM Algorithm (Gaussian Mixture)
# -------------------------------
gmm = GaussianMixture(n_components=k,  random_state=42)
gmm_labels = gmm.fit_predict(X_scaled)

# -------------------------------
# Step 4: Compare Results
# -------------------------------
silhouette_kmeans = silhouette_score(X_scaled, kmeans_labels)
silhouette_gmm = silhouette_score(X_scaled, gmm_labels)

print("===== Clustering Results =====")
print(f"K-Means Silhouette Score: {silhouette_kmeans:.4f}")
print(f"EM (GMM) Silhouette Score: {silhouette_gmm:.4f}")

# Ground-truth labels exist as "target" in iris.frame
true_labels = df['target']
ari_kmeans = adjusted_rand_score(true_labels, kmeans_labels)
ari_gmm = adjusted_rand_score(true_labels, gmm_labels)

print(f"K-Means Adjusted Rand Index: {ari_kmeans:.4f}")
print(f"EM (GMM) Adjusted Rand Index: {ari_gmm:.4f}")

# -------------------------------
# Step 5: Comment on Results
# -------------------------------
if silhouette_kmeans > silhouette_gmm:
    print("\nK-Means produced better-defined clusters than EM (GMM).")
elif silhouette_gmm > silhouette_kmeans:
    print("\nEM (GMM) produced better-defined clusters than K-Means.")
else:
    print("\nBoth algorithms produced similar clustering quality.")
