import os
import subprocess
import requests
import json
import random
import string
import hashlib
import wget

def generate_random_string(length):
    return ''.join(random.choice(string.hexdigits) for _ in range(length))

def get_csrftoken():
    response = requests.get("https://i.instagram.com/api/v1/si/fetch_headers/?challenge_type=signup")
    headers = response.headers
    return headers.get("set-cookie").split("csrftoken=")[1].split(";")[0]

def login_user(username, password):
    csrftoken = get_csrftoken()
    device = "android-" + generate_random_string(16)
    uuid = generate_random_string(32)
    phone = generate_random_string(8) + "-" + generate_random_string(4) + "-" + generate_random_string(4) + "-" + generate_random_string(4) + "-" + generate_random_string(12)
    data = {
        "phone_id": phone,
        "_csrftoken": csrftoken,
        "username": username,
        "guid": uuid,
        "device_id": device,
        "password": password,
        "login_attempt_count": "0"
    }
    ig_sig = "4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178"
    hmac = hashlib.sha256(json.dumps(data).encode()).hexdigest() + "." + json.dumps(data)
    headers = {
        "User-Agent": "Instagram 10.26.0 Android (18/4.3; 320dpi; 720x1280; Xiaomi; HM 1SW; armani; qcom; en_US)",
        "Cookie": "csrftoken=" + csrftoken
    }
    response = requests.post("https://i.instagram.com/api/v1/accounts/login/", headers=headers, data={"signed_body": hmac})
    return response.text

def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        result = login_user(username, password)
        if "logged_in_user" in result:
            print("Login Successful")
        elif "challenge" in result:
            print("Challenge required")
        else:
            print("Login failed")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
