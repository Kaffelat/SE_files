import subprocess

black_list = '&', '|' ,';', '$', '>', '<', '`', ',', '@'
domain_name = input("Enter the domain name: ")
if not domain_name:
    print('you didnt type anything')
else:
    flag = 0
    for i in domain_name:
        for j in black_list:
            if i == j:
                flag = 1
                break
    if flag == 1:
        print('surt show')
    else:
        command = "nslookup {}".format(domain_name)
        response = subprocess.check_output(command, shell=True, encoding="UTF-8")
        print(response)
