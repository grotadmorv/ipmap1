import subprocess

output = subprocess.check_output(['nmap', '-sV', "127.0.0.1"])
print(str(output))