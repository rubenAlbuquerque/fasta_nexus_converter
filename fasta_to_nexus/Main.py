#!/home/username/Desktop python3
# import do argv para receber os parametro passados numa lista com o nome argv
from sys import argv
import Cabecalho, EndNexus, SeparacaoNomeSequencia


#Abre o ficheiro passado no parametro com indice 1 
fasta_file = open(argv[1], 'r')


# Atribuicao do resultado da funcoes contida nos modulo para a utilizacao breve.
dicionario = SeparacaoNomeSequencia.file(fasta_file)
topoNexus = Cabecalho.topoNexus(dicionario)
fimNexus = EndNexus.fimNexus()


# O ciclo For tem como objetivo acrescentar os espacos correspondentes de um ficheiro nexus. 
DNA = ""
for i,j in dicionario.items():
		DNA += "\t"+ i + "  " + j + "\n"


#Criamos um novo ficheiro com o nome example.nex que apresenta o output de todo o código escrito.
novoFicheiro = open('example.nex','w')
novoFicheiro.write(topoNexus + DNA + fimNexus)
novoFicheiro.close()
