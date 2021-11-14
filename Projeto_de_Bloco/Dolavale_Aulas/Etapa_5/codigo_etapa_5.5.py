import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)


def print_event(name):
    print('EVENTO:', time.ctime(), name)


agora = time.time()
print('INICIO:', agora)
scheduler.enterabs(agora + 2, 3, print_event, ('primeira chamada',))
scheduler.enterabs(agora + 2, 1, print_event, ('segunda chamada',))
print('CHAMADAS ESCALONADAS DA FUNÇÃO:', time.ctime())

scheduler.run()
