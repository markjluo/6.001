s = 'bobobobobkhadsjlfaaahkabobbob'

bob = 0
start = 0
end = 3
for letter in s:
    if s[start:end] == 'bob':
        bob += 1
    start += 1
    end += 1

print('Number of times bob occurs:', bob)

# OR

num_bob = 0

for letter in s:
    if s[0:3] == 'bob':
        num_bob += 1
    s = s[1:]

print('Number of times bob occurs is:', num_bob)