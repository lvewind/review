import wmi

w = wmi.WMI()
cpu = w.Win32_Processor()

print(cpu[0].ProcessorId)
