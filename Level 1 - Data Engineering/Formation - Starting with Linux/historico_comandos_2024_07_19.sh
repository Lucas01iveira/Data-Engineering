    1  ls
    2  sudo apt update
    3  ls
    4  sudo apt update
    5  cls
    6  clear
    7  pwd
    8  ls -a
    9  pwd --help
   10  pwd -L
   11  pwd -l
   12  pwd -P
   13  pwd
   14  ls --help
   15  clear --help
   16  clear
   17  cd etc
   18  ls
   19  cd Downloads
   20  cd
   21  cd Downloads
   22  ls
   23  clear
   24  cd
   25  ls
   26  cd Documents
   27  ls
   28  ls -a
   29  cd .
   30  cd ..
   31  ls -a
   32  cd .local
   33  ls
   34  cd share
   35  ls
   36  ls -a
   37  cd
   38  cd /local/share
   39  cd /.local/share
   40  cd /.local
   41  cd .local/share
   42  cd
   43  clear
   44  cd --help
   45  cd var/log
   46  clear
   47  ls -a
   48  sudo ls -a /etc
   49  sudo ls -a
   50  clear
   51  cd /
   52  ls
   53  cd etc
   54  d
   55  cd
   56  cd 
   57  cd /
   58  ls
   59  cd home
   60  ls
   61  cd
   62  cd --help
   63  ls
   64  ls a
   65  ls -a
   66  cd 
   67  cd/
   68  cd /
   69  ls -al
   70  cd
   71  touch --help
   72  clear
   73  pwd
   74  ls
   75  mkdir labs
   76  ls
   77  cd labs
   78  mkdir dir1
   79  mkdir dir2
   80  ls
   81  ls -a
   82  ls -al
   83  ls
   84  clear
   85  cd dir1
   86  mkdir dir2
   87  cd dir2
   88  mkdir -p dir3/dir4
   89  pwd
   90  cd dir3/dir4
   91  mkdir dir5
   92  cd dir5
   93  touch teste.txt
   94  touch teste3.txt
   95  touch a.csv
   96  cd
   97  cd labs/dir1/dir2/dir3/dir4/dir5/
   98  . teste.txt
   99  ls
  100  cd
  101  cd labs
  102  mkdir arqsdir
  103  cd arqsdir
  104  cd ..
  105  rmdir arqsdir
  106  rmdir lab1
  107  rmdir dir1
  108  rm dir1
  109  rm -r dir1
  110  ls
  111  pwd
  112  clear
  113  mkdir arqsdir
  114  ls
  115  ls -al
  116  ls
  117  ls -a
  118  ls
  119  pwd
  120  cd labs
  121  cd ..
  122  rmdir labs
  123  cd labs 
  124  ls
  125  cd ..
  126  cls
  127  clear
  128  ls
  129  rm -r labs
  130  mkdir labs
  131  cd labs
  132  mkdir copy_files_folders
  133  rm copy_files_folders
  134  rmdir copy_filed_folders
  135  rmdir copy_files_folders
  136  mkdir copy_ff
  137  cd copy_ff
  138  mkdir dir1 dir2
  139  cd dir1
  140  touch arq1 arq2 arq3
  141  mkdir -p sub1/sub2
  142  ls
  143  cp -r * ../dir2
  144  cd ..
  145  clear
  146  cd dir1
  147  ls
  148  ls ../dir2
  149  cd ../dir2
  150  ls
  151  cd ..
  152  rm -r dir1 dir2
  153  ls
  154  mkdir dir1 dir2
  155  cd dir1
  156  touch arq1 arq2 arq3
  157  mkdir -p sub1/sub2
  158  ls
  159  cd
  160  cp labs/copy_ff/dir1/* labs/copy_ff/dir2
  161  cp * labs/copy_ff/dir1/* labs/copy_ff/dir2
  162  cp -r labs/copy_ff/dir1/* labs/copy_ff/dir2
  163  clear
  164  cd labs/copy_ff
  165  ls
  166  dir2
  167  cd dir2
  168  ls
  169  clear
  170  cd ..
  171  ls
  172  mkdir dir1
  173  mkdir dir3
  174  mv -r dir1/* dir4
  175  mv --help
  176  clear
  177  ls
  178  mv dir1/* dir4
  179  mkdir dir4
  180  mv dir1/* dir4
  181  ls
  182  cd dir1
  183  ls
  184  cd ../dir4
  185  ls
  186  clear
  187  history
  188  clear
  189  ls
  190  cd 
  191  cd labs
  192  ls
  193  rm -r copy_ff
  194  ls
  195  mkdir glob
  196  cd glob
  197  touch arq1 arq2 arq10 arq100
  198  touch arq3
  199  touch tmp1 tmp2
  200  ls
  201  ls arq*
  202  ls arq1*
  203  ls tmp*
  204  ls arq1??
  205  ls arq1?
  206  ls
  207  touch arq5 arq9 arq010
  208  ls
  209  ls ????
  210  ls ???1
  211  ls --help
  212  clear
  213  ls
  214  ls ???[1-5]
  215  cd 
  216  cd labs
  217  rm -r glob
  218  ls
  219  clear
  220  cp /etc/services .
  221  ls
  222  /etc/passwd
  223  cp /etc/passwd .
  224  ls
  225  cd labs
  226  ls
  227  cat services
  228  grep http services
  229  grep -i http services
  230  grep -L http
  231  ls
  232  cd labs
  233  ls
  234  grep -i ssh *
  235  more services
  236  clear
  237  less
  238  less passwd
  239  ls
  240  cat passwd
  241  less passwd
  242  grep -i lucas *
  243  grep --help
  244  grep -li lucas
  245  grep -l lucas
  246  grep -i Lucas passwd
  247  grep -i Lucas servi*
  248  grep -L Lucas
  249  clear
  250  tail 10 services
  251  tail -10 services
  252  tail -10 passwd
  253  cat passwd
  254  clear
  255  grep -rl Lucas *
  256  grep -l Lucas
  257  grep -rl Lucas *
  258  mkdir teste
  259  cp passwd teste
  260  ls
  261  ls teste
  262  grep -rl Lucas *
  263  ls
  264  mkdir glob
  265  touch glob/arq1 glob/arq3 glob/arq5 
  266  touch glob/temp1 glob/temp2
  267  touch glob/arq10 glob/arq100
  268  cd glob
  269  ls
  270  echo teste
  271  clear
  272  ls
  273  cd ..
  274  ls
  275  find / -name .config
  276  sudo find / -name *.config
  277  clear
  278  find . -amin -10
  279  find . -amin -30
  280  find . -atime -5
  281  find /home/lucas/ -size +10M
  282  ccd
  283  cd
  284  ls
  285  cd ..
  286  cd
  287  cd ..
  288  ls
  289  pwd
  290  cd ..
  291  ls
  292  pwd
  293  find . -size +1G
  294  clear
  295  ls
  296  cd home/lucas/labs
  297  cd home/lucas
  298  cd home
  299  ls
  300  cd lucas01/labs
  301  mkdir redirecionamento
  302  ls
  303  cp /etc/services .
  304  ls
  305  cd redirecionamento
  306  cp /etc/services .
  307  ls
  308  cat services > copia_services.txt
  309  ls
  310  tail -10 copia_services.txt
  311  tail -10 services
  312  cat services
  313  more services
  314  find / -name .config
  315  clear
  316  ls
  317  rm copia_Servics.txt
  318  rm copia_services.txt
  319  ls
  320  grep ssh services > listagem.txt
  321  ls
  322  cat listagem.txt
  323  grep 3389 services >> listagem.txt
  324  ls
  325  cat listagem.txt
  326  cat /etc/passwd | grep -i lucas
  327  cat /etc/passwd | grep -i lucas > teste_arq.txt
  328  ls
  329  sudo find -name .config
  330  sudo find / -name .config
  331  sudo find / -name *.config
  332  lear
  333  clear
  334  ls
  335  grep http services
  336  ls -al
  337  sudo find / -name *.config
  338  clear
  339  ls
  340  ls -al
  341  grep -i http * 
  342  sudo find / -name *.config
  343  clear
  344  ls
  345  ls -al
  346  grep -i http *
  347  sudo find / -name *.config]
  348  sudo find / -name *.config
  349  ls
  350  ls -al
  351  grep -i http *
  352  sudo find / -name *.config
  353  cd /var/log
  354  ls
  355  tail -10 syslog
  356  grep systemd syslog
  357  ls /home/lucas01/labs
  358  mkdir /home/lucas01/labs/combinando_comandos
  359  grep systemd syslog | sort | tail -10 > teste_log.txt
  360  grep systemd syslog | sort | tail -10 > /home/lucas01/combinando_comandos/teste_log.txt
  361  grep systemd syslog | sort | tail -10 > /home/lucas01/labs/combinando_comandos/teste_log.txt
  362  cd
  363  cd labs/combinando_comandos
  364  ls
  365  cat teste_log.txt
  366  clear
  367  cd /
  368  cd var/logs
  369  var/log
  370  ls
  371  cd var/log
  372  ls
  373  tail -10 syslog
  374  cat syslog
  375  history
  376  cd -
  377  cd-
  378  cd -
  379  cd -/labs
  380  mkdir /home/lucas01/labs/extraindo_conteudos
  381  ls /home/lucas01/labs/
  382  cut --help
  383  grep systemd syslog | tail 10
  384  grep systemd syslog | tail -10
  385  grep systemd syslog | sort | tail -10
  386  cp syslog ~/labs/extraindo_conteudos
  387  cd ~labs/extraindo_conteudos
  388  cd ~/labs/extraindo_conteudos
  389  ls
  390  grep systemd syslog
  391  grep systemd syslog | sort | tail -10 | cut -d " " f1
  392  cut --help
  393  grep systemd syslog | sort | tail -10 | cut -d " " -f1
  394  grep systemd syslog | sort | tail -10 | cut -d " " -f1-6
  395  grep systemd syslog | sort | tail -10 | cut -d " " -f 1-3,6-
  396  grep systemd syslog | sort | tail -10 | cut -d " " -f 1-3,6- > syslog_tratado
  397  rm syslog_tratado
  398  grep systemd syslog | sort | tail -10 | cut -d " " -f 1-3,6- > syslog_tratado.txt
  399  grep systemd syslog | sort | tail -10 | cut -d " " -f 1-3,6- 
  400  grep systemd syslog | sort | tail -10 | cut -d " " -f -3 
  401  grep systemd syslog | sort | tail -10 | cut -d " " -f -7
  402  grep --help
  403  cd ~
  404  ls
  405  ls -al
  406  ls -a
  407  clear
  408  cd labs
  409  sudo apt update
  410  ls
  411  clear
  412  sudo apt update
  413  sudo apt install wamerican
  414  find / -name wamerican
  415  sudo find / -name wamerican
  416  sudo find / -name american
  417  sudo find / -name *american
  418  sudo find / -name *american*
  419  ls
  420  mkdir expressoes_regulares
  421  cp /usr/share/dict/american-english ./expressoes_regulares
  422  ls
  423  cd expressores_regulares
  424  cd expressoes_regulares
  425  ls
  426  cat american-english
  427  grep computer american-english
  428  cat american-english | grep -E "computer"
  429  cat american-english | grep -E "^computer"
  430  cat american-english | grep -E "computer$"
  431  cat american-english | grep -E "^computer$"
  432  history
  433  history > historico_comandos_2024_07_19
  434  rm historico_comandos_2024_07_19
  435  ls ~
  436  mkdir ~/labs/comandos_aprendizado
  437  history > ~/labs/historico_comandos_2024_07_19.txt
  438  clear
  439  ls
  440  cat american-english | grep -iE "^computer$"
  441  echo "Computer" >> american-english
  442  echo "COMPUTER" >> american-english
  443  echo "COMPUTER"
  444  grep -i computer american-english
  445  grep smartphone american-english
  446  echo "Smartphone" >> american-english
  447  echo "SMARTPHONE" >> american-english
  448  cat american-english | grep -iE "computer|smartphone"
  449  cat american-english | grep -iE "^computer$|^smartphone$"
  450  #testando
  451  cat american-english | grep -iE "^computer$|^smartphone$" # estamos querendo trazer ou "computer" ou "smartphone", de modo case-insensitive
  452  # o parametro -E do grep indica que estamos trabalhando com expressoes regulares
  453  history
  454  history > ~/labs/historico_comandos_2024_07_19.txt
  455  history >> ~/labs/historico_comandos_2024_07_19.sh
  456  history >> ~/labs/comandos_aprendizado/historico_comandos_2024_07_19.sh
