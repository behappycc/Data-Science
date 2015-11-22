from sklearn import datasets
from sklearn.decomposition import PCA

from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.externals.six import StringIO
import pydot 

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

def pca():
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target
    target_names = iris.target_names

    #2 first principal components
    pca = PCA(n_components=2)
    X_r = pca.fit(X).transform(X)
    plt.figure(1)
    for c, i, target_name in zip("rgb", [0, 1, 2], target_names):
        plt.scatter(X_r[Y == i, 0], X_r[Y == i, 1], c=c, label=target_name)
    plt.legend()
    plt.title('2 first principal components')
    plt.xlabel('1st eigenvector')
    plt.ylabel('2nd eigenvector')

    #3 first principal components
    pca = PCA(n_components=3)
    X_r = pca.fit(X).transform(X)
    fig = plt.figure(2, figsize=(8, 6))
    ax = Axes3D(fig, elev=-150, azim=110)
    ax.set_title('3 first principal components')
    for c, i, target_name in zip("rgb", [0, 1, 2], target_names):
        ax.scatter(X_r[Y == i, 0], X_r[Y == i, 1], X_r[Y == i, 2], c=c, label=target_name)
    #handles, labels = ax.get_legend_handles_labels()
    #ax.legend([ 'setosa', 'versicolor', 'virginica' ],[ 'setosa', 'versicolor', 'virginica' ])
    ax.set_xlabel("1st eigenvector")
    ax.set_ylabel("2nd eigenvector")
    ax.set_zlabel("3rd eigenvector")

    plt.show()

def decisionTree():
    iris = load_iris()
    clf = tree.DecisionTreeClassifier(criterion='gini', splitter='best', min_samples_split=2, min_samples_leaf=1)
    clf = clf.fit(iris.data, iris.target)

    dot_data = StringIO() 
    tree.export_graphviz(clf, out_file=dot_data, feature_names=iris.feature_names, class_names=iris.target_names) 
    graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
    graph.write_pdf("iris.pdf")

def kmeansClustering():
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

    estimators = {'k_means_iris_1': KMeans(n_clusters=1),
                  'k_means_iris_2': KMeans(n_clusters=2),
                  'k_means_iris_3': KMeans(n_clusters=3),
                  'k_means_iris_4': KMeans(n_clusters=4),
                  'k_means_iris_5': KMeans(n_clusters=5),
                  'k_means_iris_6': KMeans(n_clusters=6),
                  'k_means_iris_7': KMeans(n_clusters=7),
                  'k_means_iris_8': KMeans(n_clusters=8)
                 }

    fignum = 1
    for name, est in estimators.items():
        fig = plt.figure(fignum, figsize=(4, 3))
        plt.clf()
        ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

        plt.cla()
        est.fit(X)
        labels = est.labels_

        ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=labels.astype(np.float))
        ax.set_xlabel('Petal width')
        ax.set_ylabel('Sepal length')
        ax.set_zlabel('Petal length')
        fignum = fignum + 1

    plt.show()


def main():
    #pca()
    #decisionTree()
    kmeansClustering()

if __name__ == '__main__':
    main()