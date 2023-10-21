def max_value(inputlist):
    outpulist=[0]*len(inputlist)
    for item in range(len(inputlist)):
        outpulist[item]=inputlist[item]
    outpulist.sort()
    return outpulist[-1]

print(max_value([17, 7, -1, 26, 3, 9]))
               