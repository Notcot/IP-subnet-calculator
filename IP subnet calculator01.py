import re

def listli_to_str(aa: list):
    holder = []
    for li in aa:
        holder.append(str(li))
    return ".".join(holder)

input_ip = input("Enter ip address with CIDR included, like: xxx.xxx.xxx.xxx/xx  ")

ip_list = re.split(r"[./]", input_ip)
int_ip_list = []
for li in ip_list:
    li = int(li)
    int_ip_list.append(li)

cidr = int_ip_list.pop(-1)
a = int(cidr)%8
subnet_num = 0
start_bin = 128

for i in range(0, a):
    subnet_num += start_bin 
    start_bin /= 2

if a == 0:
    subnet_num = 255
else:
    subnet_num = int(subnet_num)

magic_num = 256 - subnet_num

if cidr in range(9, 17):
    subnet_mask = [255, subnet_num, 0, 0]
elif cidr in range(17, 25):
    subnet_mask = [255, 255, subnet_num, 0]
elif cidr in range(25, 31):
    subnet_mask = [255, 255, 255, subnet_num]

track = 0
network_addr = []
broadcast_addr = []
for li in subnet_mask:
    if li == 255:
        network_addr.append(int_ip_list[track])
        broadcast_addr.append(int_ip_list[track])
        track += 1
    elif li == 0:
        network_addr.append(0)
        broadcast_addr.append(255)
        track += 1
    else:
        interesting = int_ip_list[track] - int_ip_list[track]%magic_num
        network_addr.append(interesting)
        broadcast_addr.append(interesting + magic_num - 1)
        track += 1

track = 0

first_available = network_addr[:]
first_available[-1] += 1

last_available = broadcast_addr[:]
last_available[-1] -= 1

total_addr = 2**(32 - cidr)
usable_host = total_addr - 2

print("------------------------------------------------------")
print("------------------------------------------------------")
print(f"Ip address entered: {input_ip}")
print(f"Subnet mask: {listli_to_str(subnet_mask)}")
print("------------------------------------------------------")
print(f"Network address is: {listli_to_str(network_addr)}")
print(f"Broadcast address is: {listli_to_str(broadcast_addr)}")
print(f"First available address is: {listli_to_str(first_available)}")
print(f"Last available address is: {listli_to_str(last_available)}")
print(f"Total address available: {total_addr}")
print(f"Total usable host: {usable_host}")
print("------------------------------------------------------")
print("------------------------------------------------------")
