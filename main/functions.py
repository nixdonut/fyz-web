import math

def get_level(listx, done):

    listy = list(listx)

    if done in listy:
        return listy.index(done) + 2
    listy.append(done)
    listy.sort()
    return listy.index(done) + 1

def get_percent_till_next_level(listx, done):

    listy = list(listx)

    if done in listy:
        return 0
    if done < listy[0]:
        return math.floor(100 * done/listy[0])
    listy.append(done)
    listy.sort()
    n = listy.index(done)
    return math.floor(100 * (done - listy[n - 1])/(listy[n + 1] - listy[n - 1]))

def get_done_level(listx, done):

    listy = list(listx)
    
    if done in listy:
        return 0
    if done < listy[0]:
        return done
    listy.append(done)
    listy.sort()
    n = listy.index(done)
    return done - listy[n - 1]

def get_total_level(listx, done):

    listy = list(listx)

    if done < listy[0]:
        return listy[0]
    if done in listy:
        n = listy.index(done)
        return listy[n + 1] - done
    listy.append(done)
    listy.sort()
    n = listy.index(done)
    return listy[n + 1] - listy[n - 1]