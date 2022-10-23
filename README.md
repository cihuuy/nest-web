`🐦 nest!`
---
<img src='https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white'/> <img src='https://img.shields.io/badge/NeoVim-%2357A143.svg?&style=for-the-badge&logo=neovim&logoColor=white'/> <img src ='https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue'/>

- [⭐ **download**](https://github.com/cr-0w/nest#-installation)
- [🩸 **usage**](https://github.com/cr-0w/nest#-usage)
- [⚠️ **to-do**](https://github.com/cr-0w/nest#-to-do)

I'm sure we're all sick and tired of running a HTTP Server and painstakingly finding the file we want to get on our target as well as finding our own IP to actually download the file from! I've created `nest!` in an attempt to rid us all of that headache. This program comes with _Quality-of-Life_ features such:

- **automatically serving on CTF interfaces (`tap0/tun0`)**
- **listing all the files in the current directory prepended with the whole url-shebang: e.g., `http://{ip}:{port}/{file}`**
- **asking you which interface you'd like to host the files on - no more `ifconfig` + `ls -la` spamming 😁!**



### `running w/o args` 

If you run the nest server without arguments, it will by default run on all interfaces (`0.0.0.0`) on port `8080`. You'll also see all of the interfaces populated with the sub-directories and files so it's just a matter of copy and pasting whatever link you need to download from.

---
![demo](https://github.com/cr-0w/nest/blob/main/demo/default.gif)

### `'ctf' mode [-c/--ctf]`

I've developed a special "quick" mode for CTF players; although this is certainly not limited to just them. Suppose you've got a common CTF up and running from TryHackMe or HackTheBox via OpenVPN, this mode, when toggled, will look for such interfaces (`tap0/tun0`) and automatically start serving on whichever one it finds on port 8080.

---
![ctf](https://github.com/cr-0w/nest/blob/main/demo/ctf.gif)

### `'interactive' mode [-i/--interactive]`
To run the program the way it was (interactively; meaning you'd supply whatever interface and port you'd like) in version `1.0.0`, you can run nest with `-i/--interactive`:

---
![interactive](https://github.com/cr-0w/nest/blob/main/demo/interactive.gif)

> _Oh, and don't you worry! It's got logs too 😎._

![logs](https://github.com/cr-0w/nest/blob/main/demo/logs.png)

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
ζ ›› nest -h
usage: nest [-h] [-i] [-c] [-v]

a (better) simple http server!

options:
  -h, --help         show this help message and exit
  -i, --interactive  interactively setup the server
  -c, --ctf          if you select this, nest will look for common CTF interfaces (i.e., "tun0" or
                     "tap0") and automatically start serving on that interface on port 8080.
  -v, --version      prints version.
```
```
python3 nest.py 
# or 
./nest.py
```
If you have the symbolic link as discussed above, you can call the program from anywhere:
```
nest
```
---
![help](https://github.com/cr-0w/nest/blob/main/demo/help.png)

## ⚠️ To-Do 
- ~~`add in user-arguments? perhaps...`~~ ✅
- ~~`show subdir + subdir contents`~~ ✅
- ~~`add in a "default" "no-args" setup which will run with the usual CTF-esque settings for serving files`~~ ✅
- ~~`add in an interactive switch to allow users to do the manual stuff that way instead of doing it every time on script execution`~~ ✅
