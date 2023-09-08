import getpass
import telnetlib

HOST = 'localhost'
user = input("sua conta: ")
password = getpass.getpass()

ip_routers = open("routers-ip")

for ip in ip_routers:
    ip = ip.strip()
    print("backups "+ip)
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"login: ")
    tn.write(user.encode("ascii")+ b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode("ascii") + b"\n")
    tn.write("terminal length 0\n")
    tn.write("show run\n")
    tn.write(b"exit\n")
    read_config = tn.read_all()
    save_config = open("backup-"+ HOST,"w")
    save_config.write(read_config("ascii"))
    save_config.write("\n")
    save_config.close()

print("backup completo")