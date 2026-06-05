import subprocess
import threading

class backendTygra(threading.Thread):
    def main(self):
        subprocess.run(["code"], shell=True)
        pass

    def sync(self):

        pass