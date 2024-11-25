import datetime

input_file_path = '/data/task1.txt'
output_file_path = '/data/task2.txt'

with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    for line in infile:
        outfile.write(f'readed {line.strip()}\n')


print('... And The Reader said: "Today is {}"'.format(datetime.today().date()))
