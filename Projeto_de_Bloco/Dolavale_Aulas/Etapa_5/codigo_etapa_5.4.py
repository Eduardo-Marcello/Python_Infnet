import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)


def print_long_event(name):
    print('INICIO DO EVENTO:', time.ctime(), name)
    time.sleep(2)
    print('FIM DO EVENTO:', time.ctime(), name)


print('INICIO:', time.ctime())
scheduler.enter(5, 1, print_long_event, ('primeira chamada',))
scheduler.enter(3, 1, print_long_event, ('segunda chamada',))
print('CHAMADAS ESCALONADAS DA FUNÇÃO:', time.ctime())

scheduler.run()
