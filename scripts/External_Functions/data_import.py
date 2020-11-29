def data_import(Number_of_datasets,name,skiprows_pd):
    import pandas as pd
    import numpy as np
    Time=[]
    Voltages=[]
    for i in range(Number_of_datasets):
        g=np.arange(1,Number_of_datasets+1).astype(str)
        Data=np.array(pd.read_csv(name+g[i]+'.csv',skiprows=range(skiprows_pd)))
        Time.append(Data[:,0]-min(Data[:,0]))
        Voltages.append(Data[:,1])
    return Time,Voltages