# try:
#     data = open("missing.txt")
# except IOError as err:
#     print("File error"+ str(err))
# finally:
#     if 'data' in locals():
#         data.close()


try:
    with open('missing1.txt', 'w') as data:
        print("it's... ", file=data)
except IOError as err:
    print('File error:' + str(err))

print("\n\n-------------------------\n")

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
    with open('man_out.txt', 'w') as man_file, open('other_out.txt', 'w') as other_file:
        man.append(r"\t update")
        print(man, file=man_file)
        print(other.append("\t update"), file=other_file)
except IOError as err:
    print('\noperate man or other out file error!' + str(err))

print('\n\n write file \n\n\n')
out = open('data.out', 'w')
print('Norwegian Blues stun easily.', file=out)
out.close()
