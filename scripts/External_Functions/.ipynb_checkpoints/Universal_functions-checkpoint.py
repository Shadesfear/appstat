# calcualte the weighted mean
def unicertainty_weighted(y_std):
    import numpy as np
    return np.sqrt(1/sum(1/y_std**2))
#Calculate weighted standard deviation
def weighted_mean(x,std):
    return sum(x/std**2)/sum(1/std**2)