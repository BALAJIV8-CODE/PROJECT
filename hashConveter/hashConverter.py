# add hash(#) in before text and add comma(,) after text

''''
1 . get the string length and get the string from user
2.  declare and initilize two variable for # and ,
3. add # in str1 and add , after string
4. print the list
'''
print('hashTag Generator')
# get length of loop and iterate each loop
l = int(input('Enter the string : '))
str1 = []
space = ' '
comma = ' ,'
hashSym = '#'
#for i in range(l):
i = 1
while i <= l:
    str2 = input('Enter the string : ')
    str1.append('#' + str2 + comma)
    i += 1

while i < l-1:
    str1.append(str1)
    i -= 1 
    
for str3 in str1:
    space += (str3 + '\n')

print(space[1:])

