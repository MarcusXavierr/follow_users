from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
url = 'https://www.instagram.com/'
driver.get(url)
sleep(30)

def find_follow_button(buttons):
    for button in buttons:
        if button.text == 'Follow':
            classes = button.get_attribute('class')
            if '_4pI4F' in classes:
                continue
            return button
    
    return None



def follow(array_users, driver):
    for link in array_users:
        try:
            driver.get(link)
            buttons = driver.find_elements_by_tag_name('button')
            button = find_follow_button(buttons)
            if button != None:
                button.click()
            sleep(1)
        except:
            print('Bug')
            
instaAccounts_String = '''instagram.com/igoritonobrasil
instagram.com/iara.maira.alves
instagram.com/joycce_b
instagram.com/barbarapennam
instagram.com/thaynarodriguess
instagram.com/ddavidreis
instagram.com/guilherme_sundermann
instagram.com/duhoshina
instagram.com/sabrinasouzac 
instagram.com/mariadrumondd
instagram.com/kareyn_f
instagram.com/joaomarcelosouza
instagram.com/henriqueluis375
instagram.com/beatrizluise_
instagram.com/lorenaealmeida
instagram.com/biatinoco_
instagram.com/frugericamila
instagram.com/fuscalldi
instagram.com/duhoshina 
instagram.com/jvcp.xxt
instagram.com/annamllrd
instagram.com/vigustavo30
instagram.com/henfranca25
instagram.com/bianca_parma
instagram.com/hype_maryana
instagram.com/nicolascortez27
instagram.com/saraah_martiinss
instagram.com/ribamar_97
instagram.com/_amandacarmo
instagram.com/maiconvalentim.f 
instagram.com/marinanogueirav
instagram.com/nana.s_lanna
instagram.com/lemoslucasr
instagram.com/vitoriamarquesf
instagram.com/ysamuca
instagram.com/diogo.leiite
instagram.com/charmgirl1997
instagram.com/cicv_oficial
instagram.com/gabrielm_santos1
instagram.com/marajulhaa_
instagram.com/clarissa_boddener
instagram.com/vitinhosantanna_
instagram.com/charlizedepp
instagram.com/jaiane_freitas1
instagram.com/carrietlol
instagram.com/emiluara
instagram.com/jao_elias02
instagram.com/hfcpablo
instagram.com/matheus_corrade
instagram.com/brenoribas9
instagram.com/atletico
instagram.com/greicemaita
instagram.com/taynara_paixao_
instagram.com/_ccarolcardoso
instagram.com/lara_kgm
instagram.com/acarladona
instagram.com/claudinhaa__
instagram.com/gabrielcgut
instagram.com/biel_coimbra2
instagram.com/belienerafael
instagram.com/betooo.jr
instagram.com/gabriel21cruz
instagram.com/lmariacamargo
instagram.com/luanauchihaa
instagram.com/juliamelx_
instagram.com/rivaldo
instagram.com/bre_rodrigosz
instagram.com/buzelipvd
instagram.com/danyelsena_
instagram.com/alexss_jean
instagram.com/gabgomes.sl
instagram.com/jaum736
instagram.com/rdapsilva
instagram.com/welskywalker
instagram.com/mccarlosoficial
instagram.com/thamyrisestefani_
instagram.com/matheuss_fonseca
instagram.com/ta_luanaa
instagram.com/aliviacorre
instagram.com/gabriel_honorato1
instagram.com/ramymoreira
instagram.com/gabrielbitaraess 
instagram.com/nando.rybeiro
instagram.com/bicortezi
instagram.com/itsihasmin
instagram.com/lumaantero
instagram.com/larabruzinga
instagram.com/leowaw
instagram.com/g_teixeira99
instagram.com/biludah
instagram.com/betobadini
https://instagram.com/evelynbelo
Instagram.com/guido.souza02
https://www.instagram.com/mclaramayrinck/
instagram.com/camila_gueds
https://www.instagram.com/marcusxavier123/
instagram.com/germanoaugustus
 '''
instaAccounts = instaAccounts_String.split('\n')
sleep(3)
follow(instaAccounts,driver)