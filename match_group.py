import re
#pattern = r'(?P<year>\d{4})(?P<month>\d{2})(?P<date>\d{2})'
pattern = r'(\d{4})(\d{2})(\d{2})'
print (pattern)
string = "20220815"
match = re.search(pattern,string)
#match = re.finditer(pattern,string)
if match:
    print(match.groupdict())
    print(f"{match.group(1)} at index {match.start(1)}")
    print(f"{match.group(2)} at index {match.start(2)}")
    print(f"{match.group(3)} at index {match.start(3)}")
    print(f"{match.group('year')} at index {match.start(1)}")

else:
    print("oops")