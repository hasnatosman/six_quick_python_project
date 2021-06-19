import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        times = '{:02d}:{:02d}'.format(mins, secs)
        print(times, end='\r')
        time.sleep(1)
        t -= 1

    print('TIME COMPLETED!!')


t = input('Input the seconds: ')
countdown(int(t))