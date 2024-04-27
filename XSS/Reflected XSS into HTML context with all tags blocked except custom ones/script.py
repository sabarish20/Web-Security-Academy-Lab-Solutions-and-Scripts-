# PortSwigger Lab : All tags blocked except custom tags.

import urllib3
import requests
import sys
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.execeptions.InsecureRequestWarning)
proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}


def server(text):
    soup = BeautifulSoup(text, 'html.parser')
    res = soup.find('a', attrs={'id': 'exploit-link'})['href']
    return res

def exploit(client, server, host):
    

def main():
    print('[+] Starting Exploit...')
    try:
        host = sys.argv[1].strip().rstrip('/')
    except IndexError:
        print(f'Example: {sys.argv[0]} http://example.com')
        sys.exit(-1)
    
    client = requests.Session()
    client.verify = False
    client.proxies = proxies

    exploitServer = server(client.get(host).text)
    print(f'[+] Exploit Server : {exploitServer}')

    if not exploit(client, exploitServer, host):
        print(f'[-] Failed to deliver')
        sys.exit(-1)
    
    print(f'Delivered....')
