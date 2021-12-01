import subprocess
ssid = input('insert SSID of network of which you want to find stored password: ')
results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', ssid, 'key=clear']).decode('utf-8').split('\n')
results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
print('password for this network is: ', results)