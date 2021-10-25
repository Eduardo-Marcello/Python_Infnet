Sobre variáveis de ambiente, responda:

A) O que são?

R: Variáveis de ambiente são valores nomeados dinamicamente no sistema operacional. O comportamento de um programa é
afetado ao consumir essas variáveis.

B) Como elas podem ser obtidas pelo módulo ‘os’ de Python?

R: Podem ser obtidas através do comando os.environ

C) Como pode ser obtido o caminho completo do diretório de usuário em Python, através das variáveis de ambiente?

R: Utilizando o comando os.eviron você pode mapear para encontrar o diretório do usuário, como por 
exemplo os.environ['HOMEDRIVE'] .