a_sym, a_tem = input().split()
b_sym, b_tem = input().split()
c_sym, c_tem = input().split()

count = 0

if a_sym=='Y' and int(a_tem)>=37:
    count+=1
if b_sym=='Y' and int(b_tem)>=37:
    count+=1
if c_sym=='Y' and int(c_tem)>=37:
    count+=1

if count>=2:
    print('E')
else:
    print('N')