#!/usr/bin/env python3
import os
import sys
import random
import platform
import argparse
import netifaces
import http.server
from colorama import Fore, Style

# setup status colours
err = Fore.LIGHTRED_EX + "[X]" + Style.RESET_ALL
okay = Fore.LIGHTGREEN_EX + "[+]" + Style.RESET_ALL
info = Fore.LIGHTYELLOW_EX + "[!]" + Style.RESET_ALL

# check python3
if sys.version_info.major != 3:
    print("\n" + err, "please run this script with python3!\n")
    sys.exit(1)
    
# set func -> clear screen
def clear():
    if platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("cls")

# set func -> display banner
def banner():
    print(
        Fore.LIGHTYELLOW_EX
        + """ \
           ...    *    .   _  .
    *  .  *     .   * (_)   *
      .      |*  ..   *   ..
       .  * \|  *  ___  . . *
    *   \/   |/ \/{o,o}     .
      _\_\   |  / /)  )* _/_ *      nest! (simple http server) v1.0.1
          \ \| /,--"-"---  ..                   by cr0w
    _-----`  |(,__,__/__/_ .
           \ ||      ..
            ||| .            *
            |||
            |||
      , -=-~' .-^- _
    """,
        Style.RESET_ALL,
    )

# setup handler and argparse + globals
Handler = http.server.SimpleHTTPRequestHandler

interfaces = netifaces.interfaces()

parser = argparse.ArgumentParser(description="a (better) simple http server!")
parser.add_argument(
    "-i",
    "--interactive",
    dest="interactive",
    default=False,
    required=False,
    action="store_true",
    help="interactively setup the server",
)
parser.add_argument(
    "-c",
    "--ctf",
    dest="ctf",
    default=False,
    required=False,
    action="store_true",
    help='if you select this, nest will look for common CTF interfaces (i.e., "tun0" or "tap0") and automatically start serving on that interface on port 8080.',
)
parser.add_argument(
    "-v",
    "--version",
    help="prints version.",
    action="version",
    version="%(prog)s v1.0.1",
)

args = parser.parse_args()

# show example
def show_example():
    tot_ifaces = len(interfaces)
    ran_iface = random.randrange(0, tot_ifaces)
    fin_iface = ran_iface + 1
    print(
        info,
        "for example >>> to select",
        Fore.LIGHTGREEN_EX + "{}".format(interfaces[ran_iface]) + Style.RESET_ALL + ",",
        "enter" + Fore.LIGHTGREEN_EX,
        fin_iface,
        Style.RESET_ALL,
    )

# enumerate network interfaces
def enum_interfaces():
    print(info, "collecting interfaces on the local machine...")
    print(
        okay,
        "finished. found" + Fore.LIGHTGREEN_EX,
        "{}".format(len(interfaces)),
        Style.RESET_ALL + "interface(s)",
    )
    print(
        info,
        "here they are:",
        Fore.GREEN + "{}".format(", ".join(interfaces), Style.RESET_ALL),
    )

# select interface
def select_interface():
    print(
        info,
        "please select an interface to serve on ---> choose:" + Fore.LIGHTGREEN_EX,
        "1-{}".format(len(interfaces)),
        Style.RESET_ALL,
    )
    show_example()
    print(Fore.LIGHTYELLOW_EX)
    try:
        selection = input("\rnest >> ")
        if selection.isdigit():
            selection = int(selection)
        else:
            print(err, "non-digit supplied. please enter in a valid number.")
            sys.exit(1)
    except KeyboardInterrupt:
        print(
            "\n\n" + err,
            "caught" + Fore.LIGHTRED_EX,
            "KeyboardInterrupt" + Style.RESET_ALL + ". exiting...\n",
        )
        sys.exit(1)
    if selection > (len(interfaces)):
        print(
            "\n\r" + err,
            "there aren't that many interfaces on this machine. select a valid number.",
        )
    else:
        index = int(selection) - 1
        interface = interfaces[index]
        af_inet = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]["addr"]
        print(
            "\n" + okay,
            "interface selected:" + Fore.LIGHTGREEN_EX,
            "{}".format(interface),
            Style.RESET_ALL
            + Fore.LIGHTYELLOW_EX
            + "///// "
            + Fore.LIGHTGREEN_EX
            + "{}".format(af_inet),
        )
        ip = str(af_inet)

        # get the port
        print(info, "getting server port...")
        print(info, "please select a port for hosting", Fore.LIGHTYELLOW_EX)
        try:
            port = input("\n\rnest >> ")
            if port.isdigit():
                port = int(port)
                host = (ip, port)
                print(
                    "\n" + info,
                    "populated host parameters",
                    Fore.LIGHTYELLOW_EX + "/////",
                    Fore.LIGHTGREEN_EX + "{}:{}".format(ip, port),
                )
                print(okay, "starting to serve...")
                
            # introduce QoL stuff here before serving
            print(info, "listing files for QoL...\n")
            for path, subdirs, files in os.walk("."):
                for name in files:
                    print(
                        Fore.LIGHTYELLOW_EX
                        + "http://{}:{}/{}".format(
                            af_inet, port, os.path.join(path.strip("./"), name)
                        )
                        + Style.RESET_ALL
                    )
            print(
                "\n" + okay,
                "server started @" + Fore.LIGHTGREEN_EX,
                "http://{}:{}".format(af_inet, port),
                Style.RESET_ALL + "\n" + Fore.LIGHTGREEN_EX,
            )
            try:
                server = http.server.HTTPServer(
                    host, http.server.SimpleHTTPRequestHandler
                )
                server.serve_forever()
            except KeyboardInterrupt:
                print(
                    "\n\n" + err,
                    "caught" + Fore.LIGHTRED_EX,
                    "KeyboardInterrupt" + Style.RESET_ALL + ". exiting...\n",
                )
                sys.exit(1)
            else:
                print("\n" + err, "the port isn't a number. exiting.")
                sys.exit(1)
        except KeyboardInterrupt:
            print(
                "\n\n" + err,
                "caught" + Fore.LIGHTRED_EX,
                "KeyboardInterrupt" + Style.RESET_ALL + ". exiting...\n",
            )
            sys.exit(1)

# if --ctf/-c is supplied, search for common CTF NICs and serve on them in the current directory
if args.ctf:
    clear()
    banner()
    print(okay, "ctf quick toggle enabled.")
    print(
        info,
        "searching for" + Fore.LIGHTYELLOW_EX,
        "tun0/tap0",
        Style.RESET_ALL + "on the local machine.",
    )
    ctf_nics = ["tun0", "tap0"]

    if ctf_nics[0] in interfaces:
        port = 8080
        ip = netifaces.ifaddresses("tun0")[netifaces.AF_INET][0]["addr"]
        print(
            okay,
            "found interface! >>>" + Fore.LIGHTGREEN_EX,
            "{}".format(ctf_nics[0]),
            Fore.LIGHTYELLOW_EX + "/////" + Fore.LIGHTGREEN_EX,
            "{}".format(ip),
        )
        print(okay, "default port set >>>", Fore.LIGHTGREEN_EX + "{}".format(port))
        print(
            info,
            "populated host parameters",
            Fore.LIGHTYELLOW_EX + "/////",
            Fore.LIGHTGREEN_EX + "{}:{}".format(ip, port),
        )
        host = (ip, port)
        print(info, "listing files for QoL...\n")
        for path, subdirs, files in os.walk("."):
            for name in files:
                print(
                    Fore.LIGHTYELLOW_EX
                    + "http://{}:{}/{}".format(
                        ip, port, os.path.join(path.strip("./"), name)
                    )
                    + Style.RESET_ALL
                )
        print(
            "\n" + okay,
            "server started @" + Fore.LIGHTGREEN_EX,
            "http://{}:{}".format(ip, port),
            Style.RESET_ALL + "\n" + Fore.LIGHTGREEN_EX,
        )
        try:
            server = http.server.HTTPServer(host, http.server.SimpleHTTPRequestHandler)
            server.serve_forever()
        except KeyboardInterrupt:
            print(
                "\n\n" + err,
                "caught" + Fore.LIGHTRED_EX,
                "KeyboardInterrupt" + Style.RESET_ALL + ". exiting...\n",
            )
            sys.exit(1)
    elif ctf_nics[1] in interfaces:
        clear()
        banner()
        print(okay, "ctf quick toggle enabled")
        print(
            info,
            "searching for" + Fore.LIGHTYELLOW_EX,
            "tun0/tap0",
            Style.RESET_ALL + "on the local machine.",
        )
        print(
            okay, "found interface! >>>" + Fore.LIGHTGREEN_EX, "{}".format(ctf_nics[1])
        )
        port = 8080
        ip = netifaces.ifaddresses("tap0")[netifaces.AF_INET][0]["addr"]
        print(
            okay,
            "found interface! >>>" + Fore.LIGHTGREEN_EX,
            "{}".format(ctf_nics[0]),
            Fore.LIGHTYELLOW_EX + "/////" + Fore.LIGHTGREEN_EX,
            "{}".format(ip),
        )
        print(okay, "default port set >>>", Fore.LIGHTGREEN_EX + "{}".format(port))
        print(
            info,
            "populated host parameters",
            Fore.LIGHTYELLOW_EX + "/////",
            Fore.LIGHTGREEN_EX + "{}:{}".format(ip, port),
        )
        host = (ip, port)
        print(info, "listing files for QoL...\n")
        for path, subdirs, files in os.walk("."):
            for name in files:
                print(
                    Fore.LIGHTYELLOW_EX
                    + "http://{}:{}/{}".format(
                        ip, port, os.path.join(path.strip("./"), name)
                    )
                    + Style.RESET_ALL
                )
        print(
            "\n" + okay,
            "server started @" + Fore.LIGHTGREEN_EX,
            "http://{}:{}".format(ip, port),
            Style.RESET_ALL + "\n" + Fore.LIGHTGREEN_EX,
        )
        try:
            server = http.server.HTTPServer(host, http.server.SimpleHTTPRequestHandler)
            server.serve_forever()
        except KeyboardInterrupt:
            print(
                "\n\n" + err,
                "caught" + Fore.LIGHTRED_EX,
                "KeyboardInterrupt" + Style.RESET_ALL + ". exiting...\n",
            )
            sys.exit(1)
    else:
        print(err, "no ctf interface found.\n")
        sys.exit(1)
        
# unless specified with --interactive/-i, run using the default settings -> specified in argparse.
if args.interactive:
    clear()
    banner()
    print(info, "interactive switch toggled.")
    enum_interfaces()
    select_interface()
else:
    clear()
    banner()
    all_ifaces = "0.0.0.0"
    port = 8080
    print(info, "no args supplied, defaulting to quick toggle")
    print(
        info,
        "will serve on all interfaces:" + Fore.LIGHTYELLOW_EX,
        "{}".format(all_ifaces),
    )
    print(info, "default port set:" + Fore.LIGHTYELLOW_EX, "8080")
    host = (all_ifaces, port)
    print()

    for iface in interfaces:
        print(
            okay,
            "serving on >>>" + Fore.LIGHTGREEN_EX,
            "{}".format(iface),
            Style.RESET_ALL,
        )
    print("\n" + info, "listing files for QoL...")
    for path, subdirs, files in os.walk("."):
        for iface in interfaces:
            print()
            ip = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]["addr"]
            for name in files:
                print(
                    Fore.LIGHTYELLOW_EX
                    + "http://{}:{}/{}".format(
                        ip, port, os.path.join(path.strip("./"), name)
                    )
                    + Style.RESET_ALL
                )
    print()
    for iface in interfaces:
        ip = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]["addr"]
        print(
            okay,
            "server started @" + Fore.LIGHTGREEN_EX,
            "http://{}:{}".format(iface, port) + Fore.LIGHTYELLOW_EX,
            "---> http://{}:{}".format(ip, port),
            Style.RESET_ALL + Fore.LIGHTGREEN_EX,
        )
    print()
    try:
        server = http.server.HTTPServer(host, http.server.SimpleHTTPRequestHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print(
            "\n\n" + err,
            "caught" + Fore.LIGHTRED_EX,
            "KeyboardInterrupt" + Style.RESET_ALL + ". exiting...\n",
        )
