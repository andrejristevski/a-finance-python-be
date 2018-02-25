import time
from multiprocessing import Process
import dataDownloader

def startUpdateDataThread():

    def doWork():
        while True:
            print("Updateting data")
            dataDownloader.updateCurrencyData()
            time.sleep(24*60*60)

    p = Process(target=doWork)
    p.start()


