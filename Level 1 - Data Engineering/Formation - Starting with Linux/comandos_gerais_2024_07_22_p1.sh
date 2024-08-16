    1  history
    2  clear
    3  # vamos dar inicio agora a utilizacao da cli no controle/administracao de rede
    4  # seguem alguns comandos basicos uteis de serem conhecidos 
    5  ip # menu de comandos 
    6  ip address # apresenta as configuracoes de ip do computador
    7  ip route # apresenta as rotas disponiveis no sistema operacional
    8  # as duas saidas apresentadas pelo ip address representam as duas interfaces de rede disponiveis
    9  # uma delas e o localhost da maquina, enquanto a segunda representa uma interface complementar cujo nome pode ser diferente dependendo de onde/como o ubuntu for instalado
   10  # os ips de rede ficam dispostos na 3 linha de saida (inet)
   11  ping localhost # testando a rede local
   12  # (ctrl + c para sair do ping de localhost)
   13  cat /etc/resolv.conf
   14  # e nesse arquivo que ficam configurados os "nomes de servidores" em utilizacao
   15  # ps.: servidores de dns
   16  cat /etc/hosts # para teste/consulta
   17  sudo nano /etc/hosts
   18  # (caso seja necessario modificar o arquivo anterior, precisamos fazer isso com a permissao de admin, MAS ISSO NAO E RECOMENDADO NUNCA)
   19  clear
   20  sudo lshw # faz uma listagem do hardware da maquina
   21  sudo lshw | more
   22  sudo lshw | grep sata # exemplo
   23  cd /proc
   24  cat meninfo # informacoes de memoria
   25  cat meminfo # informacoes de memoria
   26  ls 
   27  free
   28  # mostra um relatorio geral da memoria utilizada
   29  cat cpuinfo | more
   30  cat cpuinfo | processo
   31  cat cpuinfo | grep processo
   32  cat cpuinfo | grep processo | wc
   33  cat cpuinfo | grep processo | wc -l
   34  cd /dev 
   35  ls
   36  ls -al # todos os discos disponiveis do sistema
   37  ls -l | grep sda # filtro pelo nosso disco de utilizacao
   38  # as linhas sda(n) representam as particoes do nosso disco
   39  # para buscar informacoes de sistema, nos direcionamos para o seguinte diretorio
   40  cd /var/logs
   41  cd /var/log
   42  ls -l
   43  ls
   44  clear
   45  ls
   46  dmesg
   47  # normalmente esse comando e utilizadod para verificar um relatorio geral dos logs
   48  dmesg | grep sda
   49  more syslog
   50  cat syslog | grep -i cron 
   51  # o cron e uma parte do sistema responsavel por agendar tarefas
   52  # se em algum momento tivermos interesse em agendar algum script shell para ser executado com algum tipo de periodicidade, e esse arquivo que devemos ajustar
   53  ls
   54  # arqivo auth.log - informacoes e relatorios sobre o estado das autenticacoes do sistema
   55  cat auth.log | grep -i ssh
   56  tail -f auth.log # mostra as ultimas novas entradas no arquivo de log em real time
   57  # (ctl + c para interromper o processo)
   58  clear
   59  ## processos de sistema
   60  man ps
   61  ps -e
   62  ps -ef
   63  ps aux
   64  ps aux | grep -i ssh
   65  top # listagem dos principais processos em tempo real
   66  # e de maneira dinamica (ordenados por consumo d memoria)
   67  top
   68  clear
   69  sudo apt install
   70  sudo service apache2 status
   71  sudo apt install apache2
   72  clear
   73  sudo service apache2 status
   74  ip addr
   75  ps aux | grep -i apache2
   76  # processo raiz + processos sequentes relacionados ao servidor em utilizacao
   77  top
   78  clear
   79  # ferramenta `kill` - encerra processos
   80  ps aux
   81  ps aux | grep localhost
   82  # verificando a excucao do ping localhostem uma aba auxiliar
   83  kill -l # verificando os principais parametros
   84  # os sinais 9 e 15 sao os mais famosos / utilizads
   85  # o 9 forca o encerramento de uma vez (`modo ignorante`), enquanto o 15 permite que o sistema finalize o que precise ser finalizado antes de se fechar
   86  ps aux | grep localhost
   87  kill -9 4101 # informando o id do processo raiz
   88  pstree
   89  clear
   90  ## permissionamentos e privilegios
   91  apt update
   92  # precisamos sempre utilizar o `sudo` antes de executar comandos de cunho gerencial/administrativo do sistema 
   93  cd
   94  sudo apt update
   95  # nem todos os usuarios do sistema possuem permissionamento para executar comandos `sudo`
   96  cat /etc/sudoers # arquivo com as informacoes de permissionamento
   97  sudo cat /etc/sudoers # arquivo com as informacoes de permissionamento
   98  groups # verificando a qual grupo o usuario lucas01 (meu usuario atual) pertence
   99  # podemos notar que estamos nos grupos adm/sudo, justamente os grupos com permissionamento total habilitado, conforme indicado no arquivo /etc/sudoers
  100  cat /etc/group # verificando quais usuarios estao alocados em cada grupo do sistema
  101  cat /etc/group | grep -i lucas
  102  clear
  103  history
  104  ls ~/labs
  105  history > ~/labs/comandos_aprendizado/comandos_2024_07_22_p1.sh
