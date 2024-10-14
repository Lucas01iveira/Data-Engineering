#!/bin/bash

echo Informe a acao desejada compactar ou descompactar 
read resp

if [ $resp = compactar ];
then
	echo "Informe o nome do arquivo final de saida (extensao .tar.gz)": 
	read compactado
	echo "Informe a lista dos arquivos a serem compactados (separados por espaco)": 
	read arqs

	tar -czf $compactado $arqs
	echo $compactado gerado com sucesso!

elif [ $resp = descompactar ];
then
	echo Informe o nome do arquivo a ser descompactado: 
	read descomp
	echo Informe o diretorio no qual deseja armazenar os files descompactados: 
	read dir
	if [ ! -e $dir ];
	then
		mkdir -v $dir
	fi	

	tar -xzf $descomp -C $dir
	echo Arquivo descompactado com sucesso!
else
    echo Voce digitou uma acao invalida!
    echo O script aceita somente compactar ou descompactar
    exit 1
fi


