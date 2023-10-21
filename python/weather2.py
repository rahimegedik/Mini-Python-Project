def main():
    input = open("weather1.txt")
    lines = input.read().split()

    prev = float(lines[0]) # fencepost
    for i in range(1, len(lines)):
        next = float(lines[i])
        print(prev, "to", next, ", change =", (next - prev))
        prev = next
    
main()