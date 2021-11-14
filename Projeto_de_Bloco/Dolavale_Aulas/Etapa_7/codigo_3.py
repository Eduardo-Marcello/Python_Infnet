import psutil

p = psutil.Process(12756)
conn = p.connections()
print(conn)
