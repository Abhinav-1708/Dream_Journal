import subprocess
import webbrowser
import time
import signal
import sys

def main():
    try:
        # Start the Flask server as a subprocess.
        # Adjust the command if your environment needs it.
        server_process = subprocess.Popen(["python", "server.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait a couple of seconds for the server to start.
        time.sleep(2)

        # Open the default web browser to the Dream Journal URL.
        webbrowser.open("http://127.0.0.1:5000")

        print("Dream Journal is running!")
        print("Press CTRL+C in this window to stop the server and exit.")

        # Keep the launcher running until user interrupts it.
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting... shutting down the server.")
        # Terminate the Flask server.
        server_process.terminate()
        try:
            server_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            server_process.kill()
        sys.exit(0)

if __name__ == "__main__":
    main()
