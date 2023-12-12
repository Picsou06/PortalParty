from random import *
n=["00-01","02-03","04-05","06-07","08","09","10","11-12","13","14","15","16","17","18","19","e00","e01","e02"]
for i in range(1,5):
    for j in range(len(n)):
        print(f"({i}, \"{n[j]}\", {randint(1,22)}, \"Picsou06\", \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\"),")