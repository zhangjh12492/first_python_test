import os

os.chdir('../')

man = []
other = []

try:
    data = open('sketch.txt')
    for data_line in data:
        try:
            (role, line_spoken) = data_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The data file is missing!')


try:
    man_out = open('man_out.txt', 'w')
    other_out = open('other_out.txt', 'w')
    print(man, file= man_out)
    print(other, file=other_out)
except IOError:
    print('operate man or other out file error!')
finally:
    man_out.close()
    other_out.close()


print('\n\n write file \n\n\n')
out = open('data.out', 'w')
print('Norwegian Blues stun easily.', file=out)
out.close()
