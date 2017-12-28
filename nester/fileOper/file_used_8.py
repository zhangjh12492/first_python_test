import os

os.chdir("../")

with open("james.txt") as jaf:
    data = jaf.readline()
james = data.strip().split(",")

with open("julie.txt") as juf:
    data = juf.readline()
julie = data.strip().split(",")

with open("mikey.txt") as mif:
    data = mif.readline()
mikey = data.strip().split(",")

with open("sarah.txt") as saf:
    data = saf.readline()
sarah = data.strip().split(",")

print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))


def sanitize(time_string):
    if "-" in time_string:
        splitter = "-"
    elif ":" in time_string:
        splitter = ":"
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return (mins + "." + secs)


print()
print()
clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each in james:
    clean_james.append(sanitize(each))
for each in julie:
    clean_julie.append(sanitize(each))
for each in mikey:
    clean_mikey.append(sanitize(each))
for each in sarah:
    clean_sarah.append(sanitize(each))

print(sorted(clean_james, reverse=1))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))

print()
print()
clean_mikey = [sanitize(each_t) for each_t in mikey]
print(sorted(clean_mikey))
