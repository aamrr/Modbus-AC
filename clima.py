#!/usr/bin/env python
"""
Pymodbus Synchronous Client Examples
--------------------------------------------------------------------------

The following is an example of how to use the synchronous modbus client
implementation from pymodbus.

It should be noted that the client can also be used with
the guard construct that is available in python 2.5 and up::

    with ModbusClient('127.0.0.1') as client:
        result = client.read_coils(1,10)
        print result
"""
# --------------------------------------------------------------------------- #
# import the various client implementations
# --------------------------------------------------------------------------- #
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
# from pymodbus.client.sync import ModbusUdpClient as ModbusClient
# from pymodbus.client.sync import ModbusSerialClient as ModbusClient

# --------------------------------------------------------------------------- #
# configure the client logging
# --------------------------------------------------------------------------- #
import logging
FORMAT = ('%(asctime)-15s %(threadName)-15s '
          '%(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)

UNIT = 0x1


def run_sync_client():
    

    client = ModbusClient('127.0.0.1', retries=3, port=5020)

    client.connect()

    import time
    state = 0
    while True:
        time.sleep(1)
        # READING REGISTERS
        temps = []

        log.debug("Write to multiple holding registers and read back")
        # rq = client.write_registers(1, [temp1, temp2, temp3], unit=UNIT)
        rr = client.read_holding_registers(1, 3, unit=UNIT)

        assert(not rr.isError())     # test that we are not an error
        

        for tmp in rr.registers:
            print(tmp)
            if tmp>30:
                state=1

        message="hot" if state else "cold"
        print(message)

   
    # ----------------------------------------------------------------------- #
    # close the client
    # ----------------------------------------------------------------------- #
    client.close()


if __name__ == "__main__":
    run_sync_client()