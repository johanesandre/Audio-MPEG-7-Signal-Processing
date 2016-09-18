from sklearn.decomposition import PCA

def pca2(data, pc_count = None):
    return PCA(n_components = 2).fit(data).transform(data)

    
