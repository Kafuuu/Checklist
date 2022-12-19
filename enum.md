Nmap
------------------------------------
nmap -sn <IP>

nmap -p 1-65535 -T4 -A -v  <IP>

nmap -sV -sC  <IP>

nmap --script smb-vuln* -p 137,139,445 <IP>

nmap --script smb-enum*,smb-ls,smb-mbenum,smb-os-discovery,smb-s*,smb-vuln* -vv <IP>

nmap --script vuln -p 137,139,445 10.11.1.227

------------------------------------
SMB
------------------------------------
smbmap -H <IP> -u guest

smbclient -L //<IP> --option="client min protocol=core" -U ''

smbclient -L //<IP>/wwwroot -N

others
------------------------------------
mount -t cifs /<IP>/backups /mnt -o user=,password=

Mount disk

rustscan <IP> -t 500 -b 1500 -- -A

Ping <IP>

If ttl ~ 128 = windows
If ttl ~ 63 = linux

dig axfr @10.10.10.13 test.htb

snmpwalk -v 1 -c public panda.htb


