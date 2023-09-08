import getpass
import telnetlib

HOST = 'localhost'
user = input("sua conta: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)
tn.read_until(b"login: ")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")
    
tn.write(b"conf t\n")

for vlan in range(10,15):
    tn.write(b"vlan"+str(vlan).encode("ascii")+b"\n")
    tn.write(b"name Site_"+str(vlan).encode("ascii")+b"\n")
    
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode("ascii"))