import csv
from operator import le
from re import L
#open csv file
with open("IMDB-Movie-Data.csv",newline="") as csvfile:
    #read csv file content
    allrows=csv.reader(csvfile)
# allrows=open("IMDB-Movie-Data.csv","r")
    rng=[]

    for row in allrows:
    #     # delete header
        if row[0] != "Rank":
            rng.append(row)

    # #split Genre and Actors
    for i in range(len(rng)):
        rng[i][2]=rng[i][2].split("|")
        rng[i][4]=[x for i in rng[i][4].split('|') for x in i.split('| ')]

    #不重複actors list
    actors=[]
    for i in range(len(rng)):# len(rng)=1000
        for j in range(len(rng[i][4])): # len(rng[i][4])=4
            check=False
            if check==False:
                actors.append(rng[i][4][j])
            if rng[i][4][j] in actors:
                check=True

    actors_revenue = [[] for i in range(len(actors))]
    for i in range(len(actors)):
        actors_revenue[i].append(actors[i])


    for i in range(len(actors)):
        for j in range(len(rng)):
            if actors[i] in rng[j]:
                actors_revenue[i].append(rng[j][9])
    
    actors_revenue.sort(key=lambda x:x[1])
    print(actors_revenue[0])

