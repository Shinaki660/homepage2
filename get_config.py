from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios_telnet",
    "ip": "192.168.100.254",
    "username": "kai",
    "password": "kai",
}
net_connect = ConnectHandler(**device)

net_connect.enable()

output = net_connect.send_command("show running-config")

print(output)

with open("/home/kai/Router_cisco891", mode="w") as f:
    f.write(output)

