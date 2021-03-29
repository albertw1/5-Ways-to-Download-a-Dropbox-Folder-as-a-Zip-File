# 5-Ways-to-Download-a-Dropbox-Folder-as-a-Zip-File

Dropbox generally throws an error if you try to download a large folder from their web browser. Downloading their app and selectively syncing the folder is the standard solutions. However, with the Dropbox API, you can directly obtain the contents of a folder as a .zip file, making it easy to archive, store, and share data elsewhere. There are several ways to use their API and I've written down 5 straightfoward ways to do so. The first four ways use `Python3`, while the last solution can be used in a command line enviornment (`Bash`, `ZSH`). 

## Usage

1) Generate a Dropbox Authentican Token by going to https://www.dropbox.com/developers/apps.
2) Set the `auth_token` variable to your generated token.
3) Specify the path of your folder, treating the Dropbox folder as root. For example, if we have a folder named `Photos_Folder` in our Dropbox where the full path is `"~/Users/name/Dropbox/Photos_Folder"` or `"C:\Users\name\Dropbox/Photos_Folder"`, then the path we use will be `/Photos_Folder` or `\Photos_Folder`.
4) Finally, input the full path to where you want the zip file to be written/downloaded to.

