"""""Usando o módulo ‘subprocess’ de Python, crie um processo externo e imprima o PID dele."""""
import subprocess

sbp = subprocess.Popen("calc")
print("PID do processo criado:", sbp.pid)
