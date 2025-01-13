import matplotlib.pyplot as plt

def plot_results(http1, http2, http3):
    versions = ['HTTP/1.1', 'HTTP/2.0', 'HTTP/3.0']
    times = [http1, http2, http3]

    plt.bar(versions, times, color=['blue', 'green', 'orange'])
    plt.ylabel('Temps (s)')
    plt.title('Comparaison des performances HTTP')
    plt.show()

plot_results(1.2, 0.8, 0.5)  # Exemple de données
