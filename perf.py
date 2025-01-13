import time

def measure_performance(client_function, url):
    start = time.time()
    client_function(url)
    end = time.time()
    return end - start

