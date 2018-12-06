from IPy import IP


def convert():
    """
    used to convert IPv4 to an integer that browsers will resolve as a web address
    ip = the IPv4 address that is entered by the user
    ip_split = the IP split into octets
    first = first octet
    second = second octet
    third = third octet
    forth = forth octet
    integer_address = the IP converted to an integer
    :return: the IPv4 address as an integer address
    """
    ip = input("enter an IPv4 IP address: ")
    try:
        IP(ip)
        ip_split = ip.split(".")

        first = ip_split[0]
        second = ip_split[1]
        third = ip_split[2]
        forth = ip_split[3]

        integer_address = (int(first) * (256**3)) + (int(second) * (256**2)) + (int(third) * 256) + int(forth)

        print("http://" + str(integer_address))
    except Exception as e:
        print(e, "- You need to enter a valid IPv4 address. i.e. 127.0.0.1")


if __name__ == "__main__":
    convert()
