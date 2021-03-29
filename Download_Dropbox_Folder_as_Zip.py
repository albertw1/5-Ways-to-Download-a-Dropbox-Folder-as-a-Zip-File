# A list of 5 ways to download a folder from dropbox as a zip file
# 1) "/path/to/zip/file.zip" is where you want to download and store the resulting zip file
# 2) "/path/to/Dropbox/folder" is the path to the folder starting at the root of your Dropbox folder
# 3) Insert authentication token into auth_token

auth_token = "{PUT AUTH TOKEN HERE - GENERATE AT https://www.dropbox.com/developers/apps}"

# 1) Download zip file using files_download and open method
# python3
import dropbox
dbx = dropbox.Dropbox(auth_token)
dbx.users_get_current_account()
metadata, f = dbx.files_download_zip("/path/to/Dropbox/folder")
out = open("/path/to/zip/file.zip", 'wb')
out.write(f.content)
out.close()

# 2) Write using files_download_zip_to_file command
# python3
import dropbox
dbx = dropbox.Dropbox(auth_token)
dbx.users_get_current_account()
dbx.files_download_zip_to_file(download_path="/path/to/zip/file.zip", path="/path/in/Dropbox/folder")


# 3) Download zip file using Python Standard Library
import sys
import json
import http.client as httplib

headers = {
    "Authorization": auth_token,
    "Dropbox-API-Arg": "{\"path\":\"/path/to/Dropbox/folder\"}"
}

c = httplib.HTTPSConnection("content.dropboxapi.com")
c.request("POST", "/2/files/download_zip", "", headers)
r = c.getresponse()

# 4) Download zip file using Python Requests Library
import requests
import json

url = "https://content.dropboxapi.com/2/files/download_zip"

headers = {
    "Authorization": auth_token,
    "Dropbox-API-Arg": "{\"path\":\"/path/to/Dropbox/folder\"}"
}

r = requests.post(url, headers=headers)


# 5) Download zip file using a BASH POST Request

# curl -X POST \
# -H 'Authorization: Bearer {PUT AUTH TOKEN HERE - GENERATE AT https://www.dropbox.com/developers/apps}' \
# -H 'Dropbox-API-Arg: {"path":"/path/to/Dropbox/folder"}' \
# 'https://content.dropboxapi.com/2/files/download_zip' \
# --output "/path/to/zip/file.zip"


