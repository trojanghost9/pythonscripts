# used to convert IPv4 to an integer that browsers will resolve as an address


def convert():
    """
    ip = the IPv4 address that is entered by the user
    ip_split = the IP split into octets
    first = first octet
    second = second octet
    third = third octet
    forth = forth octet
    integer_address = the IP converted to an integer
    :return: the IPv4 address as an integer address
    """
    ip = raw_input("enter an IPv4 IP address: ")
    ip_split = ip.split(".")

    first = ip_split[0]
    second = ip_split[1]
    third = ip_split[2]
    forth = ip_split[3]

    integer_address = (int(first) * (256**3)) + (int(second) * (256**2)) + (int(third) * 256) + int(forth)

    print "http://" + str(integer_address)

if __name__ == "__main__":
    convert()
