#!/home/username/Desktop python3
# import do argv para receber os parametro passados numa lista com o nome argv
from sys import argv

def converterParaFasta(Nexus_file):
	Sequence = ''
	for i in Nexus_file:
		if i.startswith("\t"):
			Seq_row = i.replace("\t",">").replace('  ','\n').strip()
			if Sequence == '':
				Sequence = Seq_row
			else:
				Sequence = Sequence + '\n' + Seq_row
	print(Sequence)
	return Sequence

#Abre o ficheiro passado no parametro com indice 1 
Nexus_file = open(argv[1], 'r')

nexus = converterParaFasta(Nexus_file)



novoFicheiro = open('example.fasta','w')
novoFicheiro.write(nexus)
novoFicheiro.close()


