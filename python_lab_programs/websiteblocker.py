import time
from datetime import datetime as dt
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
web_sites_list = ["instagram.com","www.instagram.com","www.facebook.com", "facebook.com"]
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 16) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,20):
        with open(hosts_path, "r+") as file:
           content = file.readlines()
           for website in web_sites_list:
               if website in content:
                   pass
               else:
                   file.write(redirect+" "+website+"\n")
        print("you cannot access mentioned websites")
        break
    else:

        with open(hosts_path, "r+") as file:
           content = file.readlines()
           file.seek(0)
           for line in content:
               if not any(website in line for website in web_sites_list):
                   file.write(line)
                   file.truncate()
        print("websites unblocked")
        break
time.sleep(5)
