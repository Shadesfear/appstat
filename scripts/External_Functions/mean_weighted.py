def weighted_mean(x,std):
    return sum(x/std**2)/sum(1/(std**2))