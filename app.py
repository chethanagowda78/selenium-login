
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

# Get the project folder location
PROJECT_FOLDER = Path(__file__).resolve().parent
os.chdir(PROJECT_FOLDER)

# Start the local web server
HOST = "127.0.0.1"
PORT = 8000

server = HTTPServer(
    (HOST, PORT),
    SimpleHTTPRequestHandler
)

print(f"Login page running at http://{HOST}:{PORT}")
print("Press Ctrl+C to stop the server.")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
finally:
    server.server_close()
