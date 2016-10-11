# -*- coding: utf-8 -*-
from math import sqrt
import csv

# Return a similarity score based on Euclidean distance score
def sim_distance(prefs, person1, person2):
    # obtain a shared item list
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    if len(si)==0:
        return 0
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sqrt(sum_of_squares))

def sim_pearson(prefs, p1, p2):
    # Return a Pearson correlation score
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1
    n = len(si)
    if n ==0:
        return 1
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])

    sum1Sq=sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it], 2) for it in si])

    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

    num = pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1, 2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0:
        return 0
    r = num/den
    return r

def topMatches(prefs,person, n=5,similarity=sim_pearson):
    # Return a list of taste similarity from high to low
    scores=[(similarity(prefs,person,other), other) for other in prefs if other!=person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

def getRecommendations(prefs,person,similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
        if other == person:
            continue
        sim=similarity(prefs,person,other)
        if sim<=0:
            continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item]==0:
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
                simSums.setdefault(item,0)
                simSums[item]+=sim
    rankings=[(total/simSums[item],item) for item, total in totals.items()]

    rankings.sort()
    rankings.reverse()
    return rankings
    
def transformPrefs(prefs):
    results={}
    for person in prefs:
        for item in prefs[person]:
            results.setdefault(item, {})
            results[item][person]=prefs[person][item]
    return results

def calculateSimilarItems(prefs,n=10):
    #initialize a dict to store the result
    result={}
    #inverse the pref matrix
    itemPrefs=transformPrefs(prefs)
    c=0
    for item in itemPrefs:
        c+=1
        if c%100==0: print "%d / %d" % (c,len(itemPrefs))
        scores=topMatches(itemPrefs,item,n=n,similarity=sim_distance)
        result[item]=scores
    return result

def getRecommendedItems(prefs,itemMatch,user):
    userRatings=pref[user]
    scores={}
    totalSim={}

    #search through the rated item of current user
    for (item,rating) in userRatings.items():
        #search through the similar items 
        for (similarity, item2) in itemMatch[item]:
            if item2 in userRatings: continue

            scores.setdefault(item2,0)
            scores[item2]+=similarity*rating

            totalSim.setdefault(item2,0)
            totalSim[item2]+=similarity

        rankings=[(score/totalSim[item],item) for item,score in scores.item()]

        rankings.sort()
        rankings.reverse()
        return rankings


critics={'Lisa Rose':{'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
        'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
    'Gene Seymour':{'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 'Just My Luck': 1.5,
        'Superman Returns': 5.0, 'You, Me and Dupree': 2.5, 'The Night Listener': 3.0},
    'Micheal Phillips':{'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0, 'Superman Returns': 3.5, 
        'The Night Listener': 4.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0, 'Superman Returns': 4.0, 
        'The Night Listener': 4.5, 'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 'Just My Luck': 2.0,
        'Superman Returns': 3.0, 'You, Me and Dupree': 2.0, 'The Night Listener': 3.0},
    'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
        'Superman Returns': 5.0, 'You, Me and Dupree': 3.5, 'The Night Listener': 3.0},
    'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}
}



def loadMovieLens(path='/Users/samuel/Downloads/ml-20m'):
    movies={}
    moviesAddress=path+'/movies.csv'
    with open(moviesAddress,'rb') as csvfile:
        movieReader = csv.DictReader(csvfile)
        for row in movieReader:
            movies[row['movieId']]=row['title']

    prefs={}
    ratingsAddress=path+'/ratings.csv'
    with open(ratingsAddress,'rb') as csvfile:
        ratingsReader=csv.DictReader(csvfile)
        for row in ratingsReader:
            userId=row['userId']
            movieId=row['movieId']
            rating=row['rating']
            prefs.setdefault(userId,{})
            prefs[userId][movies[movieId]]=float(rating)
        return prefs


