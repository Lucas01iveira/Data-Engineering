#!/bin/bash

echo "Digite um numero "
read num1

echo "Digite outro numero "
read num2

#num1=10
#num2=20

if [ "$num1" -gt "$num2" ]; 
then
	echo "$num1 eh maior que $num2"
elif [ "$num1" -lt "$num2" ]; 
then
	echo "$num1 eh menor que $num2"
else
	echo "$num1 e $num2 sao iguais"
fi
