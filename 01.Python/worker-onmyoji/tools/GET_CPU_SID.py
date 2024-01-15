import wmi
import time

w = wmi.WMI()
cpu = w.Win32_Processor()

print(cpu[0].ProcessorId)

while True:
    time.sleep(1)
