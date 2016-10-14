import sys 

num = int(sys.stdin.readline())
uniqkeys = []

for i in xrange(num):
    
    key = map(int,sys.stdin.readline().strip())
    key = sorted(key)
    key = map(str,key)
    key = ''.join(key)
    uniqkeys.append(key)

uniqkeys = map(int,uniqkeys)
uniqkeys = set(uniqkeys)
sys.stdout.write(str(len(uniqkeys)))
