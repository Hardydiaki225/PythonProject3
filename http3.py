import asyncio
from aioquic.asyncio import connect
from aioquic.asyncio.protocol import QuicConnectionProtocol

async def http3_client(url):
    try:
        async with connect(url, port=443) as protocol:
            response = await protocol.get('/')
            print(f"Réponse HTTP/3 : {response.status}")
            return response.data
    except OSError as e:
        print(f"Erreur lors de la connexion : {e}")

if __name__ == "__main__":
    url = "https://www.google.com"
    asyncio.run(http3_client(url))