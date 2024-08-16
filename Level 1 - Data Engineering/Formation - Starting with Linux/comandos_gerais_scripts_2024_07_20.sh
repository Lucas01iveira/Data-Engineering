  509  vi edit2.txt
  510  vi edit2.txt
  511  ls
  512  clear
  513  cd ~/labs
  514  mkdir scripts
  515  cd scripts
  516  # iremos dar inicio agora no entendimento de scripts shell (no nosso caso, do tipo bash)
  517  # antes de iniciar, dois comandos importantes: env e echo
  518  env
  519  # o comando env lista na tela do terminal todas as "variaveis ambiente" do sistema
  520  echo teste
  521  # o comando "echo" printa na tela uma determinada informacao passada
  522  nano backup.sh
  523  ls
  524  cat backup.sh
  525  ls ~/labs
  526  mkdir ~/labs/backup # criando o diretorio de recebimento dos arquivos de backup
  527  ls
  528  ls ~/labs
  529  ls -l
  530  # precisamos dar a permissao de execucao do script executando o seguinte comando?
  531  chmod u+x backup.sh
  532  ls -l
  533  # o caractere "x" na descri;'ao do arquivo indica que agora temos a permissao de execucao
  534  backup.sh
  535  ./backup.sh # precisamos sempre passar o path completo, mesmo ja estando no diretorio do script
  536  ./backup.sh
  537  nano backup.sh
  538  # removi o comentario didatico da linha inicial (estava impactando a execucao do arquivo)
  539  ./backup.sh
  540  history
  541  history | tail - 34
  542  history | tail -34
  543  history | tail -35 >> ~/labs/comandos_aprendizado/comandos_gerais_scripts_2024_07_20.sh
