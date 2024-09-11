from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from kneed import KneeLocator
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

#Funzione che calcola il numero di cluster ottimale per il dataset mediante il metodo del gomito
def regolaGomito(numerical_features_scaled):
    intertia = []
    #fisso un range di k da 1 a 10
    maxK=10
    for i in range(1, maxK):
        #eseguo il kmeans per ogni k, con 5 inizializzazioni diverse e con inizializzazione random. Prendo la migliore
        kmeans = KMeans(n_clusters=i,n_init=5,init='random')
        kmeans.fit(numerical_features_scaled)
        intertia.append(kmeans.inertia_)
    #mediante la libreria kneed trovo il k ottimale
    kl = KneeLocator(range(1, maxK), intertia, curve="convex", direction="decreasing")
    # Visualizza il grafico con la nota per il miglior k
    plt.plot(range(1, maxK), intertia, 'bx-')
    plt.scatter(kl.elbow, intertia[kl.elbow - 1], c='red', label=f'Miglior k: {kl.elbow}')
    plt.xlabel('Numero di Cluster (k)')
    plt.ylabel('Inertia')
    plt.title('Metodo del gomito per trovare il k ottimale')
    plt.legend()
    plt.show()
    return kl.elbow

# Funzione che calcola il numero di cluster ottimale usando il metodo del Silhouette
def regolaSilhouette(numerical_features_scaled):
    silhouette_avg = []
    maxK = 10
    for i in range(2, maxK):  # La silhouette non è definita per k=1, quindi inizio da 2
        kmeans = KMeans(n_clusters=i, n_init=5, init='random')
        labels = kmeans.fit_predict(numerical_features_scaled)
        silhouette_avg.append(silhouette_score(numerical_features_scaled, labels))
    best_k = np.argmax(silhouette_avg) + 2  # Aggiungo 2 perché ho iniziato da k=2
    plt.plot(range(2, maxK), silhouette_avg, 'bx-')
    plt.scatter(best_k, silhouette_avg[best_k - 2], c='red', label=f'Miglior k: {best_k}')
    plt.xlabel('Numero di Cluster (k)')
    plt.ylabel('Silhouette Score')
    plt.title('Metodo del Silhouette per trovare il k ottimale')
    plt.legend()
    plt.show()
    return best_k

#Funzione che esegue il kmeans sul dataset e restituisce le etichette e i centroidi
def calcolaCluster(dataSet, metodo):
    
    numerical_features = dataSet.select_dtypes(include=[np.number])
    #Standardizzazione delle feature numeriche
    scaler = StandardScaler()
    numerical_features_scaled = scaler.fit_transform(numerical_features)

    # Stampa una sola volta tutti i nomi delle colonne numeriche
    print("Campi numerici utilizzati per il clustering:", ', '.join(numerical_features))

    if metodo == 'gomito':
        k = regolaGomito(numerical_features_scaled)
    elif metodo == 'silhouette':
        k = regolaSilhouette(numerical_features_scaled)
    elif metodo == 'undefinied':
        k = 8
    else:
        raise ValueError("Metodo non valido. Usa 'gomito' o 'silhouette'.")


    km = KMeans(n_clusters=k,n_init=10,init='k-means++')
    km = km.fit(numerical_features_scaled)
    etichette = km.labels_
    centroidi = km.cluster_centers_
    return etichette, centroidi


#Funzione che visualizza il grafico a torta per la distribuzione dei valori di differentialColumn
def getRatioChart(dataSet, differentialColumn, title):    
    counts = dataSet[differentialColumn].value_counts()
    # Etichette e colori per il grafico
    labels = counts.index.tolist()
    colors = ['lightcoral', 'lightskyblue', 'lightgreen', 'gold', 'mediumorchid', 'lightsteelblue', 'lightpink','lightgrey','lightcyan','lightyellow','lightseagreen','lightsalmon','lightblue','lightgreen','lightcoral','lightpink','lightgrey','lightcyan','lightyellow','lightseagreen','lightsalmon','lightblue','lightgreen','lightcoral','lightpink','lightgrey','lightcyan','lightyellow','lightseagreen','lightsalmon','lightblue','lightgreen','lightcoral','lightpink','lightgrey','lightcyan','lightyellow','lightseagreen','lightsalmon','lightblue','lightgreen','lightcoral','lightpink','lightgrey','lightcyan','lightyellow','lightseagreen','lightsalmon','lightblue','lightgreen','lightcoral','lightpink','lightgrey','lightcyan','lightyellow','lightseagreen','lightsalmon','lightblue','lightgreen','lightcoral','lightpink','lightgrey','lightcyan','lightyellow','lightseagreen','lightsalmon','lightblue','lightgreen','lightcoral','lightpink','lightgrey','lightcyan','lightyellow','lightseagreen','lightsalmon','lightblue']
    #lunga lista di colori per evitare ripetizioni in caso di molti valori unici
    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax.pie(counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.legend(labels, loc='lower left', fontsize='small')
    plt.title(title)
    plt.show()