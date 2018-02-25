import time
from multiprocessing import Process
import dataDownloader

def startUpdateDataThread():

    def doWork():
        while True:
            print("Updateting data")
            dataDownloader.updateCurrencyData()
            time.sleep(1000000)

    p = Process(target=doWork)
    p.start()


