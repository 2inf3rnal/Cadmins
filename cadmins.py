#!/bin/usr/python3
# coded by Yunkers Crew
# Facebook: www.facebook.com/yunkers01/
# skype: inf3rnal.king
# github: www.github.com/2inf3rnal/

import requests as r 
from colorama import Fore as F 
import sys, os, time
import argparse as arg 
from progressbar import *

user_agent = {'User-agent': 'Mozilla/5.0'}
os.system("cls" if os.name == "nt" else "reset")
login_str = "login" or "entrar" or "usuario" or "senha" or "painel" or "admin" or "restrito" or "adm"

blue2 = "\033[1;36m"
white = F.WHITE 
blue = F.BLUE 
yellow = F.YELLOW 
cyan = F.CYAN 
green = F.GREEN 
red = F.RED 
magenta = F.MAGENTA 

index = r"""===============================================================================

{}   ÛÛÛÛÛÛÛÛÛ                ÛÛÛÛÛ                  ÛÛÛ                    
  ÛÛÛ°°°°°ÛÛÛ              °°ÛÛÛ                  °°°                     
{} ÛÛÛ     °°°   ÛÛÛÛÛÛ    ÛÛÛÛÛÛÛ  ÛÛÛÛÛÛÛÛÛÛÛÛÛ   ÛÛÛÛ  ÛÛÛÛÛÛÛÛ    ÛÛÛÛÛ 
°ÛÛÛ          °°°°°ÛÛÛ  ÛÛÛ°°ÛÛÛ °°ÛÛÛ°°ÛÛÛ°°ÛÛÛ °°ÛÛÛ °°ÛÛÛ°°ÛÛÛ  ÛÛÛ°°  
°ÛÛÛ           ÛÛÛÛÛÛÛ °ÛÛÛ °ÛÛÛ  °ÛÛÛ °ÛÛÛ °ÛÛÛ  °ÛÛÛ  °ÛÛÛ °ÛÛÛ °°ÛÛÛÛÛ 
°°ÛÛÛ     ÛÛÛ ÛÛÛ°°ÛÛÛ °ÛÛÛ °ÛÛÛ  °ÛÛÛ °ÛÛÛ °ÛÛÛ  °ÛÛÛ  °ÛÛÛ °ÛÛÛ  °°°°ÛÛÛ
{} °°ÛÛÛÛÛÛÛÛÛ °°ÛÛÛÛÛÛÛÛ°°ÛÛÛÛÛÛÛÛ ÛÛÛÛÛ°ÛÛÛ ÛÛÛÛÛ ÛÛÛÛÛ ÛÛÛÛ ÛÛÛÛÛ ÛÛÛÛÛÛ  {}v2
{}  °°°°°°°°°   °°°°°°°°  °°°°°°°° °°°°° °°° °°°°° °°°°° °°°° °°°°° °°°°°°  
{}
* Admin finder && Ear scanner
* Criado por Supr3m0 & W4r1o6k (Yunkers Crew)
* Facebook: www.facebook.com/yunkers01/
===============================================================================""".format(blue2, white, blue2, white, blue2, white)
manual = """--url (-u)          Site alvo. (--url www.site.com)
--linguagem (-l)    Linguagem no qual o site foi criado. (--linguagem php)
--wordlist (-w)     Wordlist que deseja usar (Não é obrigatório). (--wordlist wordlist.txt)
--threads (-t)      Tempo para cada requisição. (--threads 10)

--ear (-E)          Buscar por falhas EAR em cada pasta que respondeu "200/OK". (--ear)
--salvar (-S)       Salvar os resultados que responderam "200/OK". (--salvar)"""

parser = arg.ArgumentParser()
parser.add_argument("--url","-u", action='store')
parser.add_argument("--linguagem", "-l", action='store', default = "php")
parser.add_argument("--wordlist", "-w", action='store')
parser.add_argument("--ear", "-E", action='store_true')
parser.add_argument("--salvar", "-S", action='store_true')
parser.add_argument("--threads", "-t", action='store', type = int, default = "10")
param = parser.parse_args()

if len(sys.argv) == 1:
	print(index)
	print(manual)
	exit()
if not param.url:
	print(index)
	print("{}[x] {}Insira uma URL para continuar.".format(red, white))
	exit()

def arruma(url):
	if url[-1] != "/":
		url = url + "/"
	if url[:7] != "http://" and url[:8] != "https://":
		url = "http://" + url
	return url

def inicio():
	url = arruma(param.url)
	print(index)
	print("{}[+] {}Site: {}".format(green, white, url))
	print("{}[+] {}Linguagem/ext: {}".format(green, white, param.linguagem))
	if param.wordlist:
		print("{}[+] {}Wordlist: {}".format(green, white, param.wordlist))
	else:
		print("{}[+] {}Wordlist: padrão".format(green, white))
	sys.stdout.write("\n{}[*] {}Verificando conexão: ".format(blue, white))
	sys.stdout.flush()
	try:
		verifica = r.get(url, headers=user_agent)
		if verifica.status_code == 200 and not "not found" in verifica.text:
			sys.stdout.write("{}conectado!{}\n".format(green, white))
			sys.stdout.flush()
		else:
			sys.stdout.write("{}erro na conexão.\n".format(red))
			exit("\n")
	except Exception as erro:
		print("\n{}[x] {}Não consegui me conectar!".format(red, white))
		exit()

	progressbar_wd = ["{}[*] {}Preparando wordlist: ".format(blue, white), Percentage()]
	progressbarwd = ProgressBar(widgets=progressbar_wd, maxval=500)
	progressbarwd.start()
	for i in range(100,500+1,50):
		time.sleep(0.1)
		if param.wordlist:
			wordlist = open(param.wordlist, "r").readlines()
			wordlist = [x.replace("\n", "") for x in wordlist]
		else:
			wordlist = ["login.php","usuario/","usuarios/","admin/", "adm/", "painel/", "panel/", "administrador/", "administrator/", "administrative/", "administrar/", "intranet/", "paineldecontrole/", "painel_de_controle/", "atualizar/", "suporte/", "controle/", "controlar/", "servidor/", "server/", "root/", "admin_login/", "admin_index/", "sistema/", "sistemas/", "logar_admin/", "login_admin/", "3d/", "configurar/", "config/", "intra/", "area/","admin/login.php", "adm/login.php", "painel/login.php", "panel/login.php", "administrador/login.php", "administrator/login.php", "administrative/login.php", "administrar/login.php", "intranet/login.php", "paineldecontrole/login.php", "painel_de_controle/login.php", "atualizar/login.php", "suporte/login.php", "controle/login.php", "controlar/login.php", "servidor/login.php", "server/login.php", "root/login.php", "admin_login/login.php", "admin_index/login.php", "sistema/login.php", "sistemas/login.php", "logar_admin/login.php", "login_admin/login.php", "3d/login.php", "configurar/login.php", "config/login.php", "intra/login.php", "area/login.php", "wp-login.php", "dashboard/", "dashboard.php"]
			wordlist = [x.replace(".php", "."+param.linguagem) for x in wordlist]
		progressbarwd.update(i)
	progressbarwd.finish()
	ataque(wordlist, url)

def ataque(wordlist, url):
	resultados_ok = []
	num = 0
	sys.stdout.write("{}\n[*] {}Iniciando ataque".format(blue, white))
	sys.stdout.flush()
	for li in range(3):
		time.sleep(0.5)
		sys.stdout.write(".")
		sys.stdout.flush()
	print("\n{}    [!] {}Não será mostrado diretórios que retornarem '404'.".format(yellow, white))

	for path in wordlist:
		url_usar = url + path
		num +=1
		try:
			verifica = r.get(url_usar, headers=user_agent, timeout=param.threads)
			if verifica.status_code == 200  and login_str in verifica.text:
				sys.stdout.write("\r{}    [p] {}Contém um formulário de login: {}\n".format(green, white, url_usar))
				sys.stdout.flush()
				resultados_ok.append(url_usar)
			elif verifica.status_code == 403:
				sys.stdout.write("\r{}    [p] {}Diretório bloqueado: {}\n".format(green, white, url_usar))
				sys.stdout.flush()
				resultados_ok.append(url_usar)
			elif verifica.status_code == 501:
				sys.stdout.write("\r{}    [p] {}Diretório com erro interno: {}\n".format(green, white, url_usar))
				sys.stdout.flush()
				resultados_ok.append(url_usar)
			elif verifica.status_code == 200:
				sys.stdout.write("\r{}    [p] {}Apenas retornou 200/OK: {}\n".format(green, white, url_usar))
				sys.stdout.flush()
				resultados_ok.append(url_usar)
		except Exception as erro:
			sys.stdout.write("\r{}    [x] {}Não consegui me conectar! {}({})\n".format(red, white,erro, url_usar))
			sys.stdout.flush()
			continue
		sys.stdout.write("\r{}    Status: {}/{}".format(white, str(num), str(len(wordlist))))
		sys.stdout.flush()
	if param.ear:
		sys.stdout.write("\r{}    Completo: {}/{}\n".format(white, str(num), str(len(wordlist))))
		sys.stdout.flush()
	else:
		sys.stdout.write("\r{}    Completo: {}/{}".format(white, str(num), str(len(wordlist))))
		sys.stdout.flush()

	if param.salvar:
		print()

		sys.stdout.write("{}[*] {}Salvando todos resultados no arquivo 'cadmins.txt'".format(blue, white))
		cadmins_log = open("cadmins.txt", "w")
		cadmins_salvar = [cadmins_log.write(x + "\n") for x in resultados_ok]
		for li in range(3):
			time.sleep(0.2)
			sys.stdout.write(".")
			sys.stdout.flush()
		sys.stdout.write("pronto\n")
		sys.stdout.flush()

	if param.ear:
		if len(resultados_ok) == 0:
			pass
		else:
			sys.stdout.write("\n{}[*] {}Iniciando ear scan".format(blue, white))
			sys.stdout.flush()
			for li in range(3):
				time.sleep(0.5)
				sys.stdout.write(".")
				sys.stdout.flush()
			ear_dirs = ["admin.php", "logado.php", "principal.php", "painel.php", "sistema.php", "noticias.php", "index.php", "index2.php", "index1.php", "inicial.php", "inicio.php", "menu.php", "upload.php", "agenda.php", "pagina.php", "admin/", "adm.php", "adm/", "admin_index.php", "paineladministrativo.php", "paineladministrativo", "intranet/", "intranet.php", "intra/", "intra.php", "paineldecontrole.php", "controle.php", "paineldecontrole/", "controle/", "gerenciador/", "gerencia/", "gerenciar/", "gerenciador.php", "gerencia.php", "gerenciar.php", "dashboard/", "dashboard.php", "control/", "control.php", "main.php", "main/", "iniciar.php", "inicia/", "login1.php", "login1/", "album.php", "album/", "noticias/", "manager.php", "manage/", "star.php", "start/", "lista.php", "lista/", "editar.php", "editar/", "inserir.php", "inserir/", "usuario/", "usuario.php", "server/", "server.php", "root.php", "root/"]
			ear_dirs = [x.replace(".php", "."+param.linguagem) for x in ear_dirs]
			ear_scan(ear_dirs, resultados_ok)

def ear_scan(wordlist1, resultados__ok):
	num = 0
	num2 = 0
	ear_res_ok = []

	print("\n{}    [!] {}Não será mostrado diretórios que retornarem '404'.".format(yellow, white))
	for resultado_x in resultados__ok:
		num +=1
		if resultado_x[-1] != "/":
			continue
		else:
			for path in wordlist1:
				num2 += 1
				url_usar = resultado_x +path
				try:
					verifica = r.get(url_usar, headers=user_agent, timeout=param.threads)
					if verifica.status_code == 200:
						sys.stdout.write("\r{}    [p] {}Possível vulnerabilidade: {}\n".format(green, white, url_usar))
						sys.stdout.flush()
						ear_res_ok.append(url_usar)
				except Exception as erro:
					sys.stdout.write("\r{}    [x] {}Não consegui me conectar! {}({})\n".format(red, white,erro, url_usar))
					sys.stdout.flush()
					continue
				sys.stdout.write("\r{}    Status: {}/{} {}/{}".format(white, str(num), str(len(resultados__ok)), str(num2), str(len(wordlist1))))
				sys.stdout.flush()
	sys.stdout.write("\r{}    Completo!".format(white))
	sys.stdout.flush()
	if param.salvar:
		print()
		sys.stdout.write("{}[*] {}Salvando todos resultados no arquivo 'cadmins_ear.txt'".format(blue, white))
		cadmins_log_ear = open("cadmins_ear.txt", "w")
		cadmins_salvar_ear = [cadmins_log_ear.write(x + "\n") for x in ear_res_ok]
		for li in range(3):
			time.sleep(0.2)
			sys.stdout.write(".")
			sys.stdout.flush()
		sys.stdout.write("pronto\n")
		sys.stdout.flush()
if __name__ == "__main__":
	try:
		inicio()
		print("\n{}[+] {}Finalizado.".format(green, white))
		exit()
	except KeyboardInterrupt:
		exit("\nbye")
