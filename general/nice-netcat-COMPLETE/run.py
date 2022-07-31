import sys
import argparse
import socket

class Main:

    def __init__(self, params):
        # collect the arguments
        self.hostname: str = ""
        self.port: int = 0
        self.params = None

        self.set_params(params)

    def get_hostname(self):
        """
        This will return the hostname.
        """
        return self.hostname

    def set_hostname(self, new_hostname):
        """
        This will set the hostname.
        """
        self.hostname = new_hostname

    def get_port(self):
        """
        This will return the port.
        """
        return self.port

    def set_port(self, new_port):
        """
        This will set the port.
        """
        self.port = new_port

    def get_params(self):
        """
        This will get the parameters.
        """
        return self.params

    def set_params(self, params):
        """
        This will set the params.
        """
        self.params = params

    def parse_params(self):
        """
        This method will parse the parameters.
        """
        parser = argparse.ArgumentParser(
                description="This script will get the ascii char code from pico ctf and decode them.")
        parser.add_argument(
                "-i", "--ip", help="The hostname/ip of the netcat server", required=True)
        parser.add_argument(
                "-p", "--port", help="The port to use for netcat.", required=True)
        print(parser.parse_args(self.get_params()))
        self.set_params(parser.parse_args(self.get_params()))

    def run(self):
        """
        This method will run the netcat.
        """
        # to use ip an port write:
        # self.get_params().ip
        # for ip
        # for port write
        # self.get_params().port
        # init the connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.get_params().ip, int(self.get_params().port)))

        res = ""
        while True:
            data = sock.recv(10000)
            if not data:
                break
            res += data.decode("ascii")

        split_res = res.split(" \n")
        del split_res[-1]
        new_res = []
        for i in enumerate(split_res):
            a = chr(int(i[1]))
            new_res.append(a)
        #res = chr(int(res))
        final_res = "".join(str(e) for e in new_res)
        print(final_res)
        sock.close()


if __name__ == "__main__":
    ncscript = Main(sys.argv[1:])
    ncscript.parse_params()
    ncscript.run()
