#!/bin/bash

# nesse script vamos explorar o recebimento de parametros externos ao notebook
# para serem utilizados durante a execucao do codigo

if [ $# -lt 2 ]; # comparando se a quantidade de parametros eh menor que 2
then
	echo "O script $0 precisa de no minimo 2 parametros para funcionar:"
	echo "o nome do arquivo de saida o path dos arquivos a serem compactados"
	exit 1 # saindo da execucao do script com um log de erro
fi

arquivo_saida=$1 # selecionando o primeiro parametro do codigo
arquivos_a_compactar=${@:2} # definindo um array com todos os parametros informados, a partir do segundo
#arquivo_a_compactar=$2

echo $arquivos_a_compactar
# executa a compactacao (o [@] indica que queremos varrer todos os parametros da variavel referenciada)
tar -czf $arquivo_saida ${arquivos_a_compactar[@]} 
#tar -czf $arquivo_saida $arquivo_a_compactar

# exibe uma mensagem de feedback
#echo "Arquivo $arquivo_saida gerado com sucesso!"
