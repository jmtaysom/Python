from __future__ import print_function, division
import sys

permission = {0:[], 1:['grant'], 2:['write'], 3:['write', 'grant'],
              4:['read'], 5:['read', 'grant'], 6:['read', 'write'],
              7:['read', 'write', 'grant']}

user_1 = (7,3,0)
user_2 = (6,2,4)
user_3 = (5,1,5)
user_4 = (3,7,1)
user_5 = (6,0,2)
user_6 = (4,2,6)

permissions = [[['read', 'write', 'grant'], ['write', 'grant'], []],
               [['read', 'write'], ['write'], ['read']], 
               [['read', 'grant'], ['grant'], ['read', 'grant']], 
               [['write', 'grant'], ['read', 'write', 'grant'], ['grant']], 
               [['read', 'write'], [], ['write']], 
               [['read'], ['write'], ['read', 'write']]]

string = 'user_1=>file_1=>read user_2=>file_2=>write'
stringl = string.split(' ')
for command in stringl:
    commands = command.split('=>')
    user = int(commands[0][-1]) - 1
    file = int(commands[1][-1]) - 1
    per = commands[2]
    if per not in permissions[user][file]:
        print('false')
else:
    print('ture')

#with open(sys.argv[1],'r') as f:
#    for l in f:
#        l = l.rstrip()
#        if l != '':
#            print(prefix(l))
#            
#sys.exit()