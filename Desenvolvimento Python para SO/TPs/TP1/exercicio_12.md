Indique uma maneira de criar um processo externo ao seu programa usando o módulo ‘os’ e usando o módulo ‘subprocess’ de Python. Dê um exemplo de cada.

1 - os:
    import os
    osCommandString = "notepad.exe"
    os.system(osCommandString)

2 - subprocess:
    import subprocess
    print(subprocess.run("calc"))
