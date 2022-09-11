#!/usr/bin/env python3
import os
import sys
import platform
import netifaces
import http.server
from colorama import Fore, Style

err = Fore.RED + '[X]' + Style.RESET_ALL
okay = Fore.GREEN + '[+]' + Style.RESET_ALL
info = Fore.YELLOW + '[!]' + Style.RESET_ALL

if sys.version_info.major != 3:
    print('\n' + err + ' please run this script with python3!\n')
    sys.exit(1)


def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')


def banner():
    print(Fore.LIGHTYELLOW_EX + ''' \
           ...    *    .   _  .   
    *  .  *     .   * (_)   *
      .      |*  ..   *   ..
       .  * \|  *  ___  . . *
    *   \/   |/ \/{o,o}     .
      _\_\   |  / /)  )* _/_ *      nest! (simple http server) v1.0.0
          \ \| /,--"-"---  ..                   by cr0w
    _-----`  |(,__,__/__/_ .
           \ ||      ..
            ||| .            *
            |||
            |||
      , -=-~' .-^- _
    ''', Style.RESET_ALL)


Handler = http.server.SimpleHTTPRequestHandler


def enum_interfaces():
    print(okay, 'welcome to the', Fore.YELLOW + 'nest!')
    print(info, 'gathering interfaces...')
    interface_list = netifaces.interfaces()
    print(info, 'got', Fore.GREEN + '{}'.format(len(interface_list)), Style.RESET_ALL + 'interfaces')
    print(okay, 'here they are!', Fore.GREEN + '{}'.format(', '.join(interface_list)), Style.RESET_ALL)
    print(info, 'please select an interface to serve on -> choose:' + Fore.LIGHTGREEN_EX,
          '1-{}'.format(len(interface_list)),
          Style.RESET_ALL, Fore.RED)

    try:
        element = input('\n\rselect an interface: ')

        if element.isdigit():
            element = int(element)
            if element > len(interface_list):
                print('\n\r' + Style.RESET_ALL + err, 'there aren\'t that many interfaces. use a valid number.\n')
            else:
                index = int(element) - 1
                print('\n\r' + okay, 'selected:' + Fore.GREEN, '{}'.format(interface_list[index]), Style.RESET_ALL)
                interface = interface_list[index]
                af_inet = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
                print(okay, Fore.YELLOW + '{}'.format(interface_list[index]), Style.RESET_ALL +
                      '--->' + Fore.GREEN, '{}'.format(af_inet), Style.RESET_ALL, '\n')
                af_inet = str(af_inet)

                print(info, 'getting port...')
                print(info, 'please note that if you supply a port number' + Fore.RED,
                      'below 1024' + Style.RESET_ALL + ', you need to run the '
                                                       'program as' + Fore.RED, 'root',
                      Style.RESET_ALL + 'since the first 1024 ports '
                                        'are reserved for the root '
                                        'user.', Style.RESET_ALL, Fore.RED)
                port = input('\n\rselect a port for hosting: ')
                if port.isdigit():
                    port = int(port)
                    print('\n\r' + Style.RESET_ALL + okay, 'got port:' + Fore.GREEN, '{}'.format(port), Style.RESET_ALL)

                    print(info, 'starting to serve...')
                    host_address = (af_inet, port)
                    print(info, 'all set!')
                    server = http.server.HTTPServer(host_address, http.server.SimpleHTTPRequestHandler)
                    print(okay, 'serving at -->' + Fore.GREEN, 'http://{}:{}'.format(af_inet, port), Style.RESET_ALL,
                          '\n')

                    print(info, 'listing files in current directory for QoL...\n', Fore.YELLOW)
                    for root, dirs, files in os.walk('.', topdown=True):
                        dirs.clear()  # with topdown true, this will prevent walk from going into subs
                        for file in files:
                            print("http://{}:{}/{}".format(af_inet, port, file))
                        print(Style.RESET_ALL, Fore.LIGHTGREEN_EX)
                    server.serve_forever()

                else:
                    print('\n\r' + err, 'please supply a' + Fore.RED, 'number', Style.RESET_ALL + 'for the port.\n')
                    sys.exit(1)

        else:
            print('\n\r' + err, 'please supply a number that corresponds to an interface. ')
            print(info, 'example: to select', Fore.GREEN + 'eth0' + Style.RESET_ALL + ',', 'input', Fore.GREEN + '2.\n')

    except KeyboardInterrupt:
        print("\n\n\r" + err, 'caught exception. exiting...\n')
        sys.exit(1)


if __name__ == "__main__":
    clear()
    banner()
    enum_interfaces()
