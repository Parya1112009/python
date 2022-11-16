import re
ph = "(111)-789-8098"
match1 = re.compile(r'^(\d{3})[-. ]?(\d{3})[-. ]?(\d{4})$')
match2 = re.match(r'^(\(*\d{3}\)*)-\d{3}-\d{4}$',ph)
#match1 = re.match(r'^(\+?(\d[.\-]*){9,14}(e?xt?\d{1,5}?$')
print(match1.match(ph))
print (match2.group(1))


