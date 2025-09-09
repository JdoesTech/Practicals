import requests
import os
from PIL import Image

#Preliminaries: are done on instant loading
#Don't require user input
def welcome():
    print("Welcome")

# Scrapper
def scrape():
    #check Directory
    directory= "Fetched_Images"
    if  not os.path.isdir(directory):
        os.mkdir(directory)
    #paste url link
    url = input("Paste picture link here : ")
    #Define Header parameters
    headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "image/*,image/webp"
}
    #get response
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Image accessed successfully")
    else: 
        print("Error code: ", response.status_code)
    if response.headers["content-type"] != "image/webp":
        print("Please insert image link")
    #Obtain file name
    cont_disposition =response.headers.get("content-disposition", "")
    #("No content-disposition header").split("filename")[1])
    #Assign file name
    if "filename" in cont_disposition:
        fname_raw= cont_disposition.split("filename")[1].strip('=')
        Filename= fname_raw
    else: 
        Filename=url.split("/")[-1]
    #print("From Here")
    print(f"Successfully fetched : {Filename} ")
    #save pic
    filepath=os.path.join(directory, Filename)
    with open(filepath, "wb") as f:
        f.write(response.content)
        print(f"image saved to : {filepath}")

def main():
    welcome()
    scrape()

main()



