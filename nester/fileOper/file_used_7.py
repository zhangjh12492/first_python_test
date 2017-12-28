import pickle
import os
import nester

os.chdir("../")


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
    with open('man_bin.txt','wb') as man_file, open('other_bin.txt','wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print("File error:"+str(err))
except pickle.PickleError as perr:
    print("Picking error:"+str(perr))


new_man =[]

try:
    with open('man_bin.txt','rb') as man_file:
        new_man=pickle.load(man_file)
except IOError as err:
    print('File error:'+str(err))
except pickle.PickleError as pper:
    print('Picking error:'+str(pper))

nester.print_lol(new_man)
print(new_man[0])
print(new_man[-1])

sorted()