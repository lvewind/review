import pywifi
from pywifi import const


profile = pywifi.Profile()
profile.ssid = 'U+NetB9B1'
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_WPA2PSK)
# profile.cipher = const.CIPHER_TYPE_NONE
profile.cipher = const.CIPHER_TYPE_CCMP
profile.key = '12@8PGB131'

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
profile = iface.add_network_profile(profile)
iface.connect(profile)
print(iface.status())
