from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
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


def main():
    client = ModbusClient('127.0.0.1', retries=3, port=5020)
    
    client.connect()

    print("connected")

    #interfce
    #definition de fentre
    fenetre = Tk()
    fenetre.title("Capteurs")
    fenetre.geometry('520x820')

    #insert data label
    label = Label(fenetre, text="Inserer les temperatures")
    label.grid(column=1,row=1,pady=30,columnspan=3)

    #TEMP1 line
    TEMP1_LABEL = Label(fenetre, text="TEMPS: ")
    TEMP1_LABEL.grid(column=1,row=2,pady=10)
    TEMP1 = Entry(fenetre,width=10)
    TEMP1.grid(column=2, row=2,columnspan=2)

    #TEMP2 line
    TEMP2_label = Label(fenetre, text="TEMP2: ")
    TEMP2_label.grid(column=2,row=3,pady=10)
    TEMP2 = Entry(fenetre,width=10)
    TEMP2.grid(column=2, row=3,columnspan=2)

    #Prenom line
    TEMP3_label = Label(fenetre, text="TEMP3: ")
    TEMP3_label.grid(column=2,row=4,pady=10)
    TEMP3 = Entry(fenetre,width=10)
    TEMP3.grid(column=2, row=4,columnspan=2)


    def clicked():
        print(clicked)
        temp1 = int(TEMP1.get())
        temp2 = int(TEMP2.get())
        temp3 = int(TEMP3.get())
        
        log.debug("Write to multiple holding registers and read back")
        rq = client.write_registers(1, [temp1, temp2, temp3], unit=UNIT)
        rr = client.read_holding_registers(1, 3, unit=UNIT)
        assert(not rq.isError())     # test that we are not an error
        assert(not rr.isError())     # test that we are not an error
        assert(rr.registers == [temp1, temp2, temp3])      # test the expected value


    bt = Button(fenetre,text="Transfer",command=clicked)
    bt.grid(column=2,row=5,pady=10)



    fenetre.mainloop()

    

    # ----------------------------------------------------------------------- #
    # close the client
    # ----------------------------------------------------------------------- #
    client.close()


def run_sync_client(temp1,temp2,temp3):
    print (temp1,temp2,temp3)
  
    log.debug("Write to multiple holding registers and read back")
    rq = client.write_registers(1, [temp1, temp2, temp3], unit=UNIT)
    rr = client.read_holding_registers(1, 3, unit=UNIT)
    assert(not rq.isError())     # test that we are not an error
    assert(not rr.isError())     # test that we are not an error
    assert(rr.registers == [temp1, temp2, temp3])      # test the expected value

    
    
if __name__ == "__main__":
    main()
    