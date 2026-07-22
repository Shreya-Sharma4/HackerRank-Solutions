n = int(input())
s = set(map(int, input().split()))
command=int(input())
for i in range(command):
    choice=input().split()
    if len(choice)==2:
        element = int(choice[-1])
        if choice[0]=="remove":
            s.remove(element)
        elif choice[0]=="discard":
            s.discard(element)
    elif choice[0]=="pop":
        s.pop()
        
print(sum(s))