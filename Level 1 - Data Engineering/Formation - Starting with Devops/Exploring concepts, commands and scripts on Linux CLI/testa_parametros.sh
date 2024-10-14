#!/bin/bash

if [ $# -lt 2 ];
then
	echo "Voce informou menos de 2 parametros ao script"
	exit 1
fi

arg1=$1
arg2=$2

echo "O primeiro parametro informado foi $arg1"
echo "O segundo parametro informado foi $arg2"
