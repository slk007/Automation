with open('D:\ESO-check.txt') as f:
    output = []
    for line in f:

        if 'servlet' and 'item' in line:
            a = list(line.split("item"))
            output.append(a[1][:5])
    s = set(output)
    x = []
    count = 0
    for i in s:
        if i.isdigit():
            x.append(i)
            count += 1
    print(x, count)