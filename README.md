# EXPERIMENT 4 – EXECUTION OF NETWORK COMMANDS

## AIM

To understand and execute basic networking commands in a real-time environment, configure router interfaces, and capture Ping and Traceroute PDUs using a Network Protocol Analyzer.

## SOFTWARE REQUIREMENTS

* Windows Command Prompt / Linux Terminal
* Cisco Packet Tracer
* Wireshark Network Protocol Analyzer

## PROCEDURE

### 1. Basic Network Commands

| Command                 | Description                              |
| ----------------------- | ---------------------------------------- |
| `ping google.com`       | Checks network connectivity              |
| `ipconfig`              | Displays IP configuration in Windows     |
| `ipconfig /all`         | Displays detailed network configuration  |
| `ifconfig`              | Displays network interfaces in Linux     |
| `ip addr`               | Displays IP address information in Linux |
| `netstat -an`           | Displays active network connections      |
| `netstat -r`            | Displays routing table                   |
| `nslookup google.com`   | Finds the IP address of a domain         |
| `tracert google.com`    | Traces packet route in Windows           |
| `traceroute google.com` | Traces packet route in Linux             |
| `sudo tcpdump -i any`   | Captures network packets in Linux        |

### 2. IP Configuration Commands

**Display IP Configuration**

```cmd
ipconfig
```

**Release IP Address**

```cmd
ipconfig /release
```

**Renew IP Address**

```cmd
ipconfig /renew
```

**Clear DNS Cache**

```cmd
ipconfig /flushdns
```

### 3. Router Configuration Commands

**Enter Privileged Mode**

```bash
Router> enable
```

**Enter Global Configuration Mode**

```bash
Router# configure terminal
```

**Configure Router Interface**

```bash
Router(config)# interface gigabitEthernet 0/0
```

**Assign IP Address**

```bash
Router(config-if)# ip address 192.168.1.1 255.255.255.0
```

**Enable Interface**

```bash
Router(config-if)# no shutdown
```

**Exit Configuration Mode**

```bash
Router(config-if)# exit
Router(config)# exit
```

**Save Configuration**

```bash
Router# copy running-config startup-config
```

### 4. Privileged Mode Commands

| Command                   | Description                      |
| ------------------------- | -------------------------------- |
| `enable`                  | Enters privileged mode           |
| `disable`                 | Returns to user mode             |
| `show running-config`     | Displays current configuration   |
| `show startup-config`     | Displays saved configuration     |
| `show version`            | Displays router information      |
| `show interfaces`         | Displays interface details       |
| `show ip interface brief` | Displays IP and interface status |
| `show ip route`           | Displays routing table           |
| `show clock`              | Displays router date and time    |
| `reload`                  | Restarts the router              |

### 5. Router Processes and Statistics

| Command           | Description                    |
| ----------------- | ------------------------------ |
| `show processes`  | Displays router processes      |
| `show memory`     | Displays memory information    |
| `show interfaces` | Displays interface statistics  |
| `show ip traffic` | Displays IP traffic statistics |
| `show protocols`  | Displays network protocols     |

### 6. IP Routing Commands

**Display IP Routing Table**

```bash
Router# show ip route
```

**Display IP Interface Information**

```bash
Router# show ip interface brief
```

**Display Routing Protocols**

```bash
Router# show ip protocols
```

**Configure Default Route**

```bash
Router(config)# ip route 0.0.0.0 0.0.0.0 192.168.1.254
```

### 7. Capturing Ping and Traceroute PDUs Using Wireshark

**Procedure:**

1. Open Wireshark.
2. Select the active network interface.
3. Start packet capturing.
4. Open Command Prompt.
5. Execute the Ping command.

```cmd
ping google.com
```

6. Apply the following display filter in Wireshark.

```text
icmp
```

7. Observe ICMP Echo Request and Echo Reply packets.
8. Execute the Traceroute command.

```cmd
tracert google.com
```

9. Observe the packets generated during traceroute.
10. Analyze source IP, destination IP, protocol type and packet information.
11. Stop packet capturing.

**Wireshark Display Filters:**

| Filter | Purpose               |
| ------ | --------------------- |
| `icmp` | Displays ICMP packets |
| `udp`  | Displays UDP packets  |
| `dns`  | Displays DNS packets  |
| `ip`   | Displays IPv4 packets |

## Program
developed by T.GOSHANRAJAN(212225040098)
### `client.py`

```python

import socket

s = socket.socket()
s.connect(('localhost', 8000))

while True:
    ip = input("Enter website to ping (or exit): ")

    s.send(ip.encode())

    if ip.lower() == "exit":
        break

    result = s.recv(4096).decode()
    print(result)

s.close()


```
### `server.py`
``` python

import socket
from pythonping import ping

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(1)

print("Server waiting for connection...")

c, addr = s.accept()
print("Connected to:", addr)

while True:
    msg = c.recv(1024).decode()

    if not msg or msg.lower() == "exit":
        print("Client disconnected")
        break

    try:
        result = ping(msg, count=4, verbose=False)
        c.send(str(result).encode())

    except Exception as e:
        c.send(f"Ping failed: {e}".encode())

c.close()
s.close()

```

## OUTPUT

The following outputs are obtained:

<img width="1317" height="290" alt="Screenshot 2026-11-04 142653" src="https://github.com/user-attachments/assets/fece0c24-14d0-4e88-9501-7aabc129b976" />
<img width="1306" height="537" alt="Screenshot 2026-11-04 142722" src="https://github.com/user-attachments/assets/48d5c025-9437-4432-aade-91821c0a1acb" />


## RESULT

Thus, various network commands were successfully studied and executed in a real-time environment. Router configuration, IP configuration, network connectivity testing, routing information and packet capturing using Wireshark were performed successfully.
