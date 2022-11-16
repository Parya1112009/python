import re
match = re.search(r"(\d+)\.(\d+)", "27.1835")
print (match.groups())
print (match.group(1))
print (match.group(2))
if match:
    print(f"{match.group(1)} at index {match.start(1)}")
    print(f"{match.group(2)} at index {match.start(2)}")
    #print(f"{match.group(3)} at index {match.start(3)}")
    #print(f"{match.group('year')} at index {match.start(1)}")

