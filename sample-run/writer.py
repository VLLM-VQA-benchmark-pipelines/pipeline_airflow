import datetime


with open('/data/task1.txt', 'w') as f:
    for i in range(1, 11):
        f.write(f'step {i}\n')


print('The Writer said: today is {}'.format(datetime.today().date()))
