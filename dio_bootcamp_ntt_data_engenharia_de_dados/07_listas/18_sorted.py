linguagens = ['python', 'js', 'c', 'java', 'csharp']

sorted(linguagens, key=lambda x: len(x))

sorted(linguagens, key=lambda x: len(x), reverse=True)






listtt= [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(listtt)