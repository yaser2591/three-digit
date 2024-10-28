#test
li1 = set()
count = 0

def tab_check(x):
    global count  # Declare count as global to modify it
    li1.clear()  # Clear the set for each number
    for _ in range(3):
        b = x % 10
        if b > 0:
            li1.add(int(b))
        x = x // 10  # Use integer division
    if len(li1) > 1:
        count += 1  # Increment the global count

def main():
    for i in range(111, 999):
        tab_check(i)
    print(f"Total numbers with more than one unique non-zero digit: {count}")

if __name__ == "__main__":
    main()
