#!/user/bin/python3

from socket import gethostbyname
import requests as req

if __name__ == "__main__":
    base_link = "http://freegeoip.net/json/{}"

    hosts = ("lipe.velasco.one",        #1
             "google.com",              #2
             "facebook.com",            #3
             "amazon.com.br",           #4
             "amazon.com",              #5
             "packtpub.com",            #6
             "si3.ufc.br",              #7
             "python.org",              #8
             "store.playstation.com",   #9
             
             )

    for host in hosts:
        hostname = gethostbyname(host)
        dados = req.get( base_link.format(hostname) ).json()
        print(host)
        print("\tIP:\t{}\n\tPaís:\t{}\n\tRegião:\t{}".format(dados["ip"],
                                                             dados["country_name"],
                                                             dados["region_name"]))
