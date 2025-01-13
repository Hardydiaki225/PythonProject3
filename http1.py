import http.client

def http1_1_client(url):
    conn = http.client.HTTPConnection(url)
    conn.request("GET", "/")
    response = conn.getresponse()
    print(f"Status: {response.status}, Reason: {response.reason}")
    data = response.read()
    conn.close()
    return data
