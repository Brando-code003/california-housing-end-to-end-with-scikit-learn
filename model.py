"""
California Housing, End to End with Scikit-Learn

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - load_housing
import tarfile # reads .tgz archives. extractfile pulls out a single file as a stream without unpacking everything.
import tempfile  # gives you the system's temporary folder through gettempdir()
import urllib.request # download a file from a URL
from pathlib import Path
import pandas as pd

HOUSING_URL = "https://github.com/ageron/data/raw/main/housing.tgz"

def load_housing():
    tarball_path = Path(tempfile.gettempdir()) / "housing.tgz"
    if not tarball_path.is_file():
        urllib.request.urlretrieve(HOUSING_URL, tarball_path)
    with tarfile.open(tarball_path) as housing_tarball:
        member = housing_tarball.extractfile("housing/housing.csv")
        return pd.read_csv(member)

# Step 2 - income_categories
def income_categories(df):
    df = pd.DataFrame(df)
    # TODO: pd.cut median_income with edges [0, 1.5, 3, 4.5, 6, inf] and labels 1..5; return an int Series.
    return pd.cut(df['median_income'], bins = [0, 1.5, 3.0, 4.5, 6.0, np.inf], labels = [1, 2, 3, 4, 5]).astype(int)

# Step 3 - stratified_split
from sklearn.model_selection import train_test_split
def stratified_split(df, test_size=0.2, random_state=42):
    # TODO: train_test_split stratified on income_categories(df); return (train_set, test_set).
    train_test, test_set = train_test_split(df, test_size=test_size, random_state = random_state, stratify = income_categories(df))

    return train_test, test_set

# Step 4 - explore_correlations (not yet solved)
# TODO: implement

# Step 5 - add_ratio_features (not yet solved)
# TODO: implement

# Step 6 - split_features_labels (not yet solved)
# TODO: implement

# Step 7 - ClusterSimilarity (not yet solved)
# TODO: implement

# Step 8 - numeric_pipeline (not yet solved)
# TODO: implement

# Step 9 - categorical_pipeline (not yet solved)
# TODO: implement

# Step 10 - build_preprocessing (not yet solved)
# TODO: implement

# Step 11 - rmse (not yet solved)
# TODO: implement

# Step 12 - dummy_baseline_rmse (not yet solved)
# TODO: implement

# Step 13 - cross_val_rmse (not yet solved)
# TODO: implement

# Step 14 - linear_model (not yet solved)
# TODO: implement

# Step 15 - forest_model (not yet solved)
# TODO: implement

# Step 16 - random_search (not yet solved)
# TODO: implement

# Step 17 - test_rmse (not yet solved)
# TODO: implement

# Step 18 - bootstrap_rmse_ci (not yet solved)
# TODO: implement

# Step 19 - feature_importances (not yet solved)
# TODO: implement

# Step 20 - worst_errors (not yet solved)
# TODO: implement

# Step 21 - save_and_reload (not yet solved)
# TODO: implement

# Step 22 - predict_new (not yet solved)
# TODO: implement

