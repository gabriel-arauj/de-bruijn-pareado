# de-bruijn-pareado
Remontando genomas. Bioinformática 

Preâmbulo:
Crie	 um	 programa	 chamado	 kdMer.	 Tal	 programa	 tem	 como	 entrada	 uma	 sequencia	
genômica	no	formado	FASTA,	o	tamanho	da	leitura	(k)	e	a	distância	entre	as	leituras	(d).	
A	partir	desse	programa,	ele	gera,	em	ordem	lexicográfica	o	(k,d)	mers,	em	um	arquivo	
texto.	Supondo	que	k	=	50	e	d	=	20,	o	arquivo	de	saída	do	programa	será	k50d20mer.txt.	A	
entrada	deverá	ter	o	seguinte	formato:

INPUT - arquivo	fasta	com	o	seguinte	layout:
\>k=999d=999
Sequencia de Nucleotideos
OUTPUT	– arquivo	texto com	os	kdmers	em	ordem	lexicográfica:
[ATTG|TTGG,	GCTG|GGTG,	...]


Crie	 um	 programa	 chamado	 Assembler	 capaz	 de remontar uma	 sequência genética	 a	
partir	de	um	arquivo	texto	contendo	os	kdmers	em	ordem	lexicográfica.	 A	entrada	será	
a	 saída	 do	 programa	 anterior	 (preâmbulo)	 e	 a	 saída	 será	 um	 arquivo	 FASTA	 como	 a	
sequencia	remontada.
