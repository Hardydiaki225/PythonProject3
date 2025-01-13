import httpx

def http2_client(url):
    with httpx.Client(http2=True) as client:
        response = client.get(url)
        print(f"HTTP/2 Status: {response.status_code}")
        return response.text
