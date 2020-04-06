# 	cep2csv: utilitário simples que faz consultas de cep e imprime o resultado na saída padrão
# 
#	autor: Lucas Cavalini Barboza
#	e-mail: lucas.cavalini.barboza@gmail.com
# 	licença: GNU General Public License, versão 3 (ou superior) 
#	

import requests
import json
import sys
import getopt

mensagem_ajuda = """
cep2csv: utilitário simples que faz consultas de cep e imprime o resultado na saída padrão

Uso: python cep2csv.py cep [-s separador] [-H]

cep: um ou mais números de CEP, sem hífen

-s: usa o separador especificado, em vez da vírgula
-H: não exibe o cabeçalho
"""

try:
	opcoes, ceps = getopt.gnu_getopt(sys.argv[1:], 's:H')

except getopt.GetoptError as err:
	print(mensagem_ajuda)
	sys.exit(2)

if len(ceps) < 1:
	print(mensagem_ajuda)
	sys.exit(2)

separador = ','
cabecalho = ['cep','logradouro','complemento','bairro','localidade','uf','unidade','ibge','gia']

for opcao in opcoes:
	if opcao[0] == '-H':
		cabecalho = []
	elif opcao[0] == '-s':
		separador = opcao[1]

if cabecalho != []:
	cabecalho = separador.join(cabecalho)
	print(cabecalho)

for cep in ceps:
	viacep = requests.get("http://viacep.com.br/ws/%s/json/" %cep)

	if viacep.status_code  == requests.codes.ok:
		
		resultado = json.loads(viacep.text)
		valores = list(resultado.values())

		print(separador.join(valores))	



	

