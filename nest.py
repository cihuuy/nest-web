#!/usr/bin/env python3
import os
import sys
import platform
import argparse
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

# unless specified with --interactive/-i, run using the default settings -> specified in argparse.
if args.interactive:
    clear()
    banner()
    print(info, "interactive switch toggled.")
    # Interactive mode functions can be added here
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

    print("\n" + info, "listing files for QoL...")
    for path, subdirs, files in os.walk("."):
        for name in files:
            print(
                Fore.LIGHTYELLOW_EX
                + "http://localhost:{}/{}".format(
                    port, os.path.join(path.strip("./"), name)
                )
                + Style.RESET_ALL
            )
    print()
    print(
        okay,
        "server started @" + Fore.LIGHTGREEN_EX,
        "http://{}:{}".format(all_ifaces, port) + Style.RESET_ALL,
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
