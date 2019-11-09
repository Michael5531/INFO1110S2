a = ["a", "d", "da", "dadsa", "ewrqwe", "dsad"]
a_even = []
a_odd = []
output = []
i = 0
while i < len(a):
    if i % 2 == 0:
        a_odd.append(a[i])
    if i % 2 != 0:
        a_even.append(a[i])
    i += 1
j = 0
while j < len(a_odd):
    output.append([a_odd[j],a_even[j]])
    j += 1
print(output)