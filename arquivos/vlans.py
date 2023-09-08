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
tn.write(b"vlan 2\n")
tn.write(b"name sales\n")
tn.write(b"vlan 2\n")
tn.write(b"name ENG\n")
tn.write(b"vlan 2\n")
tn.write(b"name PRD\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode("ascii"))