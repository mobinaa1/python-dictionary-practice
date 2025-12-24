numbers={"even":[],"odd":[]}
for i in range(int(input("how many numbers do you want to add?"))):
    n=int(input(f"enter number{i+1}:"))
    if n%2==0:
        numbers["even"].append(n)
    else:
        numbers["odd"].append(n)
print(numbers)





