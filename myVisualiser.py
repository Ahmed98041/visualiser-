import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def cluster_and_visualise(datafilename, K, featurenames):
    
     data = np.genfromtxt(datafilename, delimiter=',')
     kmeans = KMeans(n_clusters=K)
     kmeans.fit(data)
     labels = kmeans.labels_

     
     n_features = len(featurenames)
     fig, axs = plt.subplots(n_features, n_features, figsize=(12, 12))

     
      
     for i, feature_i in enumerate(featurenames):
         axs[i, i].hist(data[:, i], bins=20)
         axs[i, 0].set_ylabel(feature_i)

         for j, feature_j in enumerate(featurenames):
             axs[i, j].set_xlabel(feature_j)
             if i != j:
                 axs[i, j].scatter(data[:, i], data[:, j], c=labels, 
                cmap='Set2', s=50, edgecolors='k')
                

   
     for ax in axs.flat:
         ax.tick_params(axis='both', which='major')

  
     fig.suptitle(f'KMeans Clustering by a222-mohamed ({K} Clusters)')
     plt.savefig('myVisualisation.jpg')

     
     return fig, axs