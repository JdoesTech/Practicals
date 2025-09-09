import requests
import os
from PIL import Image

if os.path.isdir("Fetched_Images"):
    print("Exists")
else: 
    os.mkdir("Fetched_Images")


print("Welcome")
url = input("Paste picture link here")
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print("Image accessed successfully")
else: 
    print("Error code: ", response.status_code)
if response.headers["content-type"] != "image/webp":
    print("Please insert image link")
print(response.headers.get("content-disposition", "No content-disposition header"))


