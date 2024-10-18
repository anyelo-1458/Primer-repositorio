import time

while True: 

    tiempo = time.strftime('%H:%M:%S:')
    print (f'\rHora acual : {tiempo}', end='')
    time.sleep = 1