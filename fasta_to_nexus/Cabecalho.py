#Nesta função, criamos o cabecário.

def topoNexus(dicionario):
	'''
	Este metodo não recebe nenhum argumento.
	Este Metodo retorna uma varivel (topo) que é uma string que serve para colocar no final do ficheiro nexus. A string (topo) contem alem de texto, duas variaveis que sao os numero de nomes das sequencias(Key) e os tamanho sequencias(Values).
	'''
	NumeroNomes = len(dicionario.keys())
	Nchar = []
	[Nchar.append(len(v)) for v in dicionario.values() if len(v) not in Nchar]
	
	topo = '#NEXUS\n\nBEGIN DATA;\nDIMENSIONS NTAX={} NCHAR={};\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\n'.format(NumeroNomes,Nchar[0])
		
	return topo
