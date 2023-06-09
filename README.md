
# visualiser-
This repository houses a Python script for KMeans clustering and visualisation of datasets. The function cluster_and_visualise(datafilename, K, featurenames) takes in a CSV file, the desired number of clusters, and a list of feature names to create a KMeans model. It fits the data to the model, assigns labels, and then generates a comprehensive visualisation of the data and the clusters.

The visualisation generated includes histograms for each feature along the diagonal and scatter plots in off-diagonal cells that compare two different features, with colors representing different clusters. The final visualisation is saved as a JPEG file.

This script is versatile and can be applied to any dataset, making it a valuable tool for data exploration and understanding the structure and relationships within your data.
