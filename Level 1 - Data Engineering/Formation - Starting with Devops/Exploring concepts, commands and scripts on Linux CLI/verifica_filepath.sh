#!/bin/bash

# verifica se o usuario passou algum parametro
if [ $# -eq 0 ];
then
	echo "Voce precisa passar pelo menos 1 filepath"
	exit 1
fi

# -- x -- CASO SIMPLIFICADO: UM UNICO FILEPATH COMO PARAMETRO -- x -- #
# caso passe da condicao...
#fpath1=$1

#if [ -e $fpath1 ];
#then
#	echo O filepath que voce informou eh valido!
#else
#	echo O filepath informado nao existe!
#fi

# -- x -- CASO GENERICO: LISTA DE FILEPATHS -- x -- #
fpaths=${@:1}
for file in ${fpaths[@]}
do
	if [ ! -e $file ];
	then
		echo "O arquivo $file NAO EXISTE"
	else
		echo "O arquivo $file EXISTE CORRETAMENTE"
	fi
done

