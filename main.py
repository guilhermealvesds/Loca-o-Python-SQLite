import os

def desenhaTopoRetangulo(colunas):
	if colunas >= 3:
		print("╔", end = '')
		colunas -=1
		while colunas >= 2:
			print("═", end = '')
			colunas -= 1
		print("╗")

def desenhaMeioRetangulo(texto):
	print("║", end = '')
	print(texto, end = '')
	print("║")

def desenhaRodapeRetangulo(colunas):
	if colunas >= 3:
		print("╚", end = '')
		colunas -=1
		while colunas >= 2:
			print("═", end = '')
			colunas -= 1
		print("╝")

os.system('clear') or None
desenhaTopoRetangulo(75)
desenhaMeioRetangulo('                           título                                        ')
desenhaRodapeRetangulo(75)
vSair = ''
input(vSair)
