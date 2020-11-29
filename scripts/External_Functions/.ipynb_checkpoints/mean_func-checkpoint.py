def mean_func1(Time,Voltages):
    from Data_sorting_rolling import data_sorting
    import numpy as np
    Roll=[]
    mean_Roll={}
    std_Roll={}
    for i in range(len(Time)):
        mean_Roll[i]=[]
        std_Roll[i]=[]
        Roll=data_sorting(Time_big[i],Voltages_big[i])
        for j in range(len(Roll[3])-1):
            mean_Roll[i].append((np.mean(Roll[1][Roll[3][j]:Roll[3][j+1]])+np.mean(Roll[0][Roll[2][j]:Roll[2][j+1]]))/2)
            std_Roll[i].append((np.std(Roll[1][Roll[3][j]:Roll[3][j+1]])+np.std(Roll[0][Roll[2][j]:Roll[2][j+1]]))/2)
    return mean_Roll,std_Roll