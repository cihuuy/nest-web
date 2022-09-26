`🐦 nest!`
---
<img src='https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white'/> <img src='https://img.shields.io/badge/NeoVim-%2357A143.svg?&style=for-the-badge&logo=neovim&logoColor=white'/> <img src ='https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue'/>

- [⭐ **download**](https://github.com/cr-0w/nest#-installation)
- [🩸 **usage**](https://github.com/cr-0w/nest#-usage)
- [⚠️ **to-do**](https://github.com/cr-0w/nest#-to-do)

I'm sure we're all sick and tired of running a HTTP Server and painstakingly finding the file we want to get on our target as well as finding our own IP to actually download the file from! I've created `nest!` in an attempt to rid us all of that headache. This program comes with _Quality-of-Life_ features such:

- **listing all the files in the current directory prepended with the whole url-shebang: e.g., `http://{ip}:{port}/{file}`**
- **asking you which interface you'd like to host the files on - no more `ifconfig` + `ls -la` spamming 😁!**
---
![demo](https://github.com/cr-0w/nest/blob/main/demo/server.gif)

> _Oh, and don't you worry! It's got logs too 😎._

![logs](https://github.com/cr-0w/nest/blob/main/demo/log.png)

## ⭐ Installation
```
git clone https://github.com/cr-0w/nest.git && cd nest/
python3 -m pip install -r requirements.txt
chmod +x nest.py
```
If you'd like to access the script from anywhere, you could create a symbolic link:
```
ln -s $(realpath nest.py) /usr/bin/nest
```
## 🩸 Usage 
```
python3 nest.py 
# or 
./nest.py
# if you have the symbolic link as discussed above, you can call the program from anywhere. run:
nest
```
## ⚠️ To-Do 
- `add in user-arguments? perhaps...` 

