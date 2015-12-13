from __future__ import division
from recommendations import critics
from math import sqrt


# returns a distance based similarity score for person1 and person2
def sim_distance(prefs, person1, person2):
    # get list of shared items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # if no ratings in common return 0
    if len(si) == 0: return 0

    # add up sum of squares
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]])

    return 1 / (1 + sum_of_squares)


# returns the Pearsons correlation coefficient for p1 and p2
def sim_pearson(prefs, p1, p2):
    # get list of shared items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    n = len(si)

    # if no ratings in common return 0
    if n == 0: return 0

    # add up all preferences
    sum1 = sum(prefs[p1][it] for it in si)
    sum2 = sum(prefs[p2][it] for it in si)

    # sum up the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    # sum up products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # calculate Pearson score
    num = pSum - (sum1 * sum2 / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))

    if den == 0: return 0;

    r = num / den

    return r


# returns the best matches to a person from the prefs dictionary.
# number of results and similarity parameters are optional
def topMatches(prefs, person, n = 5, similarity = sim_pearson):
    scores = [(similarity(prefs, person, other), other)
              for other in prefs if other != person]

    # sort for highest
    scores.sort()
    scores.reverse()
    return scores[0:n]



# gets recommendations for a person using a weighted average
# of every other user's rankings
def getRecommendations(prefs, person, similarity = sim_pearson):
    totals = {}
    simSums = {}

    for other in prefs:
        # dont compare to self
        if other == person: continue
        sim = similarity(prefs, person, other)

        # ignore scores of 0 or lower
        if sim <= 0: continue
        for item in prefs[other]:

            # only score movies i havent seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # similarity * score
                totals.setdefault(item, 0)
                totals[item] += prefs[other][item] * sim

                # sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim

    # create the normalized list
    rankings = [(total / simSums[item], item) for item, total in totals.items()]

    # return sorted list
    rankings.sort()
    rankings.reverse()
    return rankings



def transformPrefs(prefs):
    result = {}

    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})

            # flip item and person
            result[item][person] = prefs[person][item]

    return result









if __name__ == "__main__":
    print "Top matches between Lisa and Gene, Euclidean method"
    print sim_distance(critics, 'Lisa Rose', 'Gene Seymour')
    print

    print "Top matches between Lisa and Gene, Pearson method"
    print sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')
    print

    print "Top people matches for Toby"
    print topMatches(critics,'Toby',n=3)
    print

    print "Top movie picks for Toby"
    print getRecommendations(critics,'Toby')

    reversed_critics = transformPrefs(critics)
    print "Top  matches for Superman Returns"
    print topMatches(reversed_critics,'Superman Returns',n=3)
    print
    print "People who would probably like Just My Luck"
    print getRecommendations(reversed_critics, "Just My Luck")


