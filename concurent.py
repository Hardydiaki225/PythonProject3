from concurrent.futures import ThreadPoolExecutor

def fetch_parallel(urls, client_function):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(client_function, urls))
    return results
