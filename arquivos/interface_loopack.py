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
tn.write(b"interface loopback 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.0\n")
tn.write(b"end\n")
tn.write(b"exit\n")
tn.write(b"ls\n")
tn.write(b"ls\n")

print(tn.read_all().decode("ascii"))