s = 'abcbcd'
s = s.lower()

list = []

for letter in s:
    substring = letter
    for i in range(len(s) - 1):
        if s[i] <= s[i + 1]:
            substring += s[i + 1]
        else:
            break

    list.append(substring)
    s = s[1:]

length = []
for ele in list:
    l = len(ele)
    length.append(l)

ind = length.index(max(length))
string = list[ind]

print('Longest string in alphabetical order is:', string)