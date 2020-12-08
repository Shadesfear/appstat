# calcualte the weighted mean
def uncertainty_weighted(y_std):
    import numpy as np
    y_std=np.array(y_std)
    return np.sqrt(1/sum(1/y_std**2))
#Calculate weighted standard deviation
def weighted_mean(x,std):
    import numpy as np
    std=np.array(std)
    x=np.array(x)
    return sum(x/std**2)/sum(1/std**2)
def fit_multiple(func,x,y,y_std):
    import sys                                             # Modules to see files and folders in directories
    sys.path.append('External_Functions')
    from ExternalFunctions import Chi2Regression
    import numpy as np
    from iminuit import Minuit
    fit_slope=[]
    slope_uncertainty=[]
    fit_intersection=[]
    intersection_uncertainty=[]
    for i in range(len(x)):
        chi2_object=Chi2Regression(func,x[i],y, y_std)
        minuitLin = Minuit(chi2_object, pedantic=False, intersection=0, slope=1.5, print_level=0) 
        minuitLin.migrad();
        fit_slope.append(minuitLin.args[0])
        slope_uncertainty.append(minuitLin.errors["slope"])
        fit_intersection.append(minuitLin.args[1])
        intersection_uncertainty.append(minuitLin.errors["intersection"])
    return np.array(fit_slope),np.array(fit_intersection),np.array(slope_uncertainty),np.array(intersection_uncertainty)