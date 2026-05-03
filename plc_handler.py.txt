from pymodbus.client.sync import ModbusTcpClient
from config import PLC_IP, PLC_PORT, SLAVE_ID

class PLCHandler:
    def __init__(self):
        self.client = ModbusTcpClient(PLC_IP, port=PLC_PORT, timeout=1)

    def read_data(self, start_address=0, count=90):
        try:
            if self.client.connect():
                res = self.client.read_coils(start_address, count, unit=SLAVE_ID)
                if not res.isError():
                    return res.bits
            return None
        except Exception as e:
            print(f"Polling Error: {e}")
            return None

    def write_coil(self, address, value):
        # Gunakan koneksi singkat untuk penulisan agar tidak tabrakan dengan polling
        w_client = ModbusTcpClient(PLC_IP, port=PLC_PORT, timeout=1)
        try:
            if w_client.connect():
                w_client.write_coil(address, value, unit=SLAVE_ID)
                w_client.close()
        except Exception as e:
            print(f"Write Error @{address}: {e}")
