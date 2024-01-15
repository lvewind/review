import subprocess
import sys

# ret = subprocess.Popen(["ping", "10.0.0.24"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

ret = subprocess.Popen(["ping", "10.0.0.24"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

for line in iter(ret.stdout.readline, ''):
    print(line)
ret.stdout.close()
ret.wait()

# for line in iter(ret.stdout.readline, b''):
#     print(line.decode("ansi")),
# ret.stdout.close()
# ret.wait()
