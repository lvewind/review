import wmi
# import ctypes
# import sys
# import time
#
#
c = wmi.WMI()
# for os in c.Win32_OperatingSystem():
#     print(os.Caption)
#
# # print(c.Win32_NetworkAdapterConfiguration(IPEnabled=1))
#

def get_CPU_info():
    cpu = []
    cp = c.Win32_Processor()
    for u in cp:
        cpu.append(
            {
                "Name": u.Name,
                "Serial Number": u.ProcessorId,
                "CoreNum": u.NumberOfCores
            }
        )
    #   print(":::CPU info:", json.dumps(cpu))
    return cpu

print(get_CPU_info())

for interface in c.Win32_NetworkAdapterConfiguration(Description="Realtek PCIe 2.5GbE Family Controller"):
    print(interface)
#
# # # colNicConfigs = c.Win32_NetworkAdapterConfiguration(IPEnabled=1)
# # # colNicConfigs = c.Win32_NetworkAdapter(GUID="{E5670A34-F043-480C-9D80-BE52948BFAC1}")
# # # colNicConfigs = c.Win32_NetworkAdapter(Caption="[00000001] Realtek PCIe GbE Family Controller")
colNicConfigs = c.Win32_NetworkAdapter(Description="Realtek PCIe 2.5GbE Family Controller")
print(colNicConfigs)
print(colNicConfigs[0].NetConnectionID)
for obj in colNicConfigs:
    print(obj)
#     print(obj.Index)
#     print(obj.MACAddress)
    print(obj.NetConnectionID)
    print(obj.Description)
