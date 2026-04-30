import os

n = int(input("Enter number of commits: "))

for i in range(n):
    with open("log.txt", "a") as f:
        f.write(f"hello {i}\n")
    
    os.system("git add .")
    os.system(f'git commit -m "hello {i}"')

os.system("git push")

