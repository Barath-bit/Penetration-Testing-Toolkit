import socket

def port_scan(target):
    print(f"\n[+] Scanning ports on {target}")

    for port in range(20, 1025):
        s = socket.socket()
        s.settimeout(0.5)

        try:
            s.connect((target, port))
            print(f"[OPEN] Port {port}")
        except:
            pass
        finally:
            s.close()
