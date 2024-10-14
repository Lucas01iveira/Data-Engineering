#!/bin/bash

echo "Digite um numero: "
read input

rest_of_division=$(($input%2))

if [ $rest_of_division = 0 ]
then
	echo "O numero $input e par"
else
	echo "O numero $input e impar"
fi

echo "Script finalizado!"
