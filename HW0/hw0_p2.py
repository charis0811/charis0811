from operator import itemgetter
import csv
#open csv file
with open("IMDB-Movie-Data.csv",newline="") as csvfile:
    #read csv file content
    allrows=csv.reader(csvfile)

#Question (1)
    #sorting rank
    sortedrows=sorted(allrows,key=lambda x: x[7],reverse=True)
        #print 1st sortedlist
    print("Question (1):")
    for index, rows in enumerate(sortedrows):
        if index == 1 or index == 2 or index == 3:
            print(sortedrows[index][1])

    #Question (2)
    print("Question (2):")
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



    #Question (3)
    print("Question (3):")
    a=0
    sum=0
    num=0
    for value in sortedrows:
        if "Emma Watson" in sortedrows[a][4]:
            #print(sortedrows[a][4])
            sum+=float(sortedrows[a][7])
            num=num+1
        a=a+1
    avgrating=sum/num
    print(avgrating)

    #Question (4)
    print("Question (4):")
    directorcolumn = [row[3] for row in sortedrows]
    directors={}
    for i in set(directorcolumn):
        if directorcolumn.count(i)>1:
            directors[directorcolumn.count(i)]=i
    for value in reversed(sorted(directors.keys())[-3:]):
        print(directors[value],value)

    #Question (5)
    print("Question (5):")
    #split Genre
    for i in range(len(rng)):
        rng[i][2]=rng[i][2].split("|")




    #Question (6)
    #print("Question (6):")


    #Question (7)
    #print("Question (7):")





