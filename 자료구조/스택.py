#선입후출

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)  # 하단원소부터 출력
print(stack[::-1])  # 상단원소부터 줄력
