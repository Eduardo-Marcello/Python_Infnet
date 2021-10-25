Explique a principal semelhança e a principal diferença entre os comandos psutil.pids e psutil.process_iter.

R: A função psutil.process_iter() é equivalente a psutil.pids(), por retornar uma lista de processos que estão executando na máquina. A diferença está na forma de implementação, de modo que seja mais eficiente quando executado repetidamente.