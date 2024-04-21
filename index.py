import os
import sys
import argparse
import socketserver
import subprocess
import http.server
import netifaces
from colorama import Fore, Style

# Setup status colours
err = Fore.LIGHTRED_EX + "[X]" + Style.RESET_ALL
okay = Fore.LIGHTGREEN_EX + "[+]" + Style.RESET_ALL
info = Fore.LIGHTYELLOW_EX + "[!]" + Style.RESET_ALL

# Define the PHP server handler
class PHPServerHandler(http.server.CGIHTTPRequestHandler):
    # Override do_POST method
    def do_POST(self):
        # Check if request is for PHP file
        if self.is_php_request():
            self.run_php()
        else:
            super().do_POST()

    # Override do_GET method
    def do_GET(self):
        # Check if request is for PHP file
        if self.is_php_request():
            self.run_php()
        else:
            super().do_GET()

    # Check if request is for PHP file
    def is_php_request(self):
        return self.path.endswith(".php")

    # Execute PHP file
    def run_php(self):
        # Set path to PHP file
        index_path = "." + self.path

        # Check if PHP file exists
        if not os.path.exists(index_path):
            self.send_error(404, "File not found")
            return

        # Read POST data if available
        post_data = None
        if self.command == 'POST':
            content_length = self.headers.get('Content-Length')
            if content_length:
                content_length = int(content_length)
                post_data = self.rfile.read(content_length).decode('utf-8')

        # Execute PHP file with POST data and get output
        try:
            # Set environment variables including REQUEST_METHOD
            env = os.environ.copy()
            env['REQUEST_METHOD'] = self.command
            php_process = subprocess.Popen(["php", index_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, env=env)
            output, _ = php_process.communicate(input=post_data.encode('utf-8') if post_data else None)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(output)
        except Exception as e:
            self.send_error(500, "Internal server error")
            print(err, "Error executing PHP file:", e)

    # Override log_message method to remove logging
    def log_message(self, format, *args):
        return

# Define argparse + globals
interfaces = netifaces.interfaces()

parser = argparse.ArgumentParser(description="A simple PHP-enabled HTTP server")
parser.add_argument(
    "-p",
    "--port",
    dest="port",
    default=8080,
    type=int,
    required=False,
    help="Port to run the server on (default: 8080)",
)
parser.add_argument(
    "-i",
    "--interactive",
    dest="interactive",
    default=False,
    required=False,
    action="store_true",
    help="Interactively setup the server",
)

args = parser.parse_args()

# Main function to run the server
def run_server():
    try:
        # Setup server
        server_address = ("", args.port)
        httpd = socketserver.TCPServer(server_address, PHPServerHandler)
        print(okay, f"Server started at port {args.port}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n" + err, "Server stopped")
    except Exception as e:
        print(err, "An error occurred while running the server:", e)

# Run server interactively if specified
if args.interactive:
    clear()
    banner()
    run_server()
else:
    # Run server directly
    run_server()
