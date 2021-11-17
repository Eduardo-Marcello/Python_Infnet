Para sockets UDP, responda:
1) Que sequência de chamadas de funções em Python deve ser realizada pelo cliente?
    R: socket() -> sendto() e recvfrom() -> close()

2) Que sequência de chamadas de funções em Python deve ser realizada pelo servidor?
    R: socket() -> bind() -> sendto() e recvfrom() -> close()

3) Quais destas funções são bloqueantes, isto é, o processo fica esperando?
    R: bind()