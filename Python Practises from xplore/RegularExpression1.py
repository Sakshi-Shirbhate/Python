# import re
# print(re.match('ca*t','cat'))

import re
line='Welcome to Python session'
c=re.compile('.*to')
res=c.findall(line)
print(res)