num = input()
input_lines = int(num)
list = [str(input_lines)]
for i in range(2,10):
    a = input_lines*i
    list.append(str(a))
    
print(' '.join(list))