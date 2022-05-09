import re
solution = lambda files : sorted(files, key = lambda x : (re.split('\d+', x.lower())[0], int(re.findall('\d+', x)[0])))
