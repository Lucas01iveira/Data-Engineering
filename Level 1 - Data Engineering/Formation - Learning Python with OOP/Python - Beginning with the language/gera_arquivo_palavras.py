frutas = ('Melancia', 'Morango', 'Maca', 'Uva', 'Banana', 'Laranja')

# lembrando sempre de incluir o caractere 'r' (raw) antes de inicializar uma string com contra barra (\)
arq = open(r'Level 1 - Data Engineering\Formation - Learning Python with OOP\Python - Beginning with the language\palavras.txt', mode='w')

for fruta in frutas:
    arq.write(fruta+'\n')

arq.close()