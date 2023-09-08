import getpass
import telnetlib

HOST = 'localhost'
user = input("sua conta: ")
password = getpass.getpass()

ip_routers = open("routers-ip")

for ip in ip_routers:
    ip = ip.strip()
    print("configurando roteador "+ip)
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"login: ")
    tn.write(user.encode("ascii")+ b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")
    
    for interface in range(1,4):
        tn.write(b"interface loopback "+str(interface).encode("ascii")+b"\n")

    tn.write(b"end\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode("ascii"))