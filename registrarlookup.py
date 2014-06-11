#python-whois must be installed https://code.google.com/p/pywhois/

import whois

domain_list = "domain_list.txt"
registrar_list = "registrar_list.txt"

def lookup(domain_list, registrar_list):
    """
    Runs a whois to lookup registrar for a domain from a list.
    """
    for domain in domain_list:
		domain = domain.rstrip()
		registrar = whois.whois(domain).registrar
		registrar_list.write("Domain name: " + domain) 
		registrar_list.write("Registrar(s):")
        registrar_list.write(registrar)
		registrar_list.write(" ")
		registrar_list.write("-----------------------")
		registrar_list.write(" ")

if __name__ == "__main__":
	import whois

domain_list = open("domain_list.txt", "r")
registrar_list = open("registrar_list.txt", "a")

lookup(domain_list, registrar_list)

domain_list.close()
registrar_list.close()
