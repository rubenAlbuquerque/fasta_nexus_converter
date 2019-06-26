
def file(fasta_file):
	'''
	No ciclo for em baixo, este percorre todos os nomes das sequências. 
	Caso tenha >, então é um nome da sequência.
	Percorre o fasta_file, e retira >. O strip foi utilizado para retirar todos os \n. No dicionário inicializamos o nome com a sua sequência vazia.
	Onde não tiver ">", será adicionada ao dicionário a sequência com o respetivo nome.
	'''
	dicionario = {} 
	for i in fasta_file:
		if i.startswith(">"):
			name = i.replace(">","").strip()
			dicionario[name] = ""
		else:	
			dicionario[name] += i.strip()

	return dicionario





