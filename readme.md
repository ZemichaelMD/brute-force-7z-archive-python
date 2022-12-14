# Bruitforce a 7z archive

### This is a python script to bruitforce a 7z archive
<br>

### Usage :
Provide all the possible combinable words or phrases to *password.txt* file. The less the files, the better time it takes to complete bruiteforce.

```
python <password.text file> <archive.7z file>
```

## You must :
### Install 7z :
On windows, install **chocolatey** by running the following as admin in powershell

```
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
Install 7z with
```
choco install 7zip.install -y
```