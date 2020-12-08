#csv files with name_number and return it in a libery with the all the data set from 0:number
def data_import(Number_of_datasets,name,skiprows_pd,location):
    import pandas as pd
    import numpy as np
    Time=[]
    Voltages=[]
    for i in range(Number_of_datasets):
        g=np.arange(1,Number_of_datasets+1).astype(str)
        Data=np.array(pd.read_csv(location+name+g[i]+'.csv',skiprows=range(skiprows_pd)))
        Time.append(Data[:,0]-min(Data[:,0]))
        Voltages.append(Data[:,1])
    return Time,Voltages

    # find index for when the ball roll in and out and give out the points.
def data_sorting(Time,Voltages):
    import numpy as np
    #rescale voltages
    Voltages_rescaled=np.array(Voltages-min(Voltages))
    #removes all voltages below 0.1 to remove the noise 
    Voltages_rescaled_nonzeros=Voltages_rescaled[Voltages_rescaled>0.1]
    # remove the top of the voltages so we only have the slope of voltages left 
    Voltages_rescaled_nonzeros_mtop=Voltages_rescaled_nonzeros[Voltages_rescaled_nonzeros<4]
    Time_rescaled=Time[Voltages_rescaled>0.1]
    Time_rescaled_mtop=Time_rescaled[Voltages_rescaled_nonzeros<4]
    #calculate the time diffrence between a point and the point before that
    DT=Time_rescaled_mtop-np.roll(Time_rescaled_mtop,-1)
    #calculate the voltages diffrence between a point and the point before that
    DV=Voltages_rescaled_nonzeros_mtop-np.roll(Voltages_rescaled_nonzeros_mtop,-1)
    #calulate the slope between a point and the point after
    a=DV/DT
    #if slope is positive and above zero it is inroll
    inroll=Time_rescaled_mtop[np.where(a>10,1,0).astype(bool)]
    #if slope is positive and above zero it is outroll
    outroll=Time_rescaled_mtop[np.where(a<-10,1,0).astype(bool)]
    #delta_T between inrolls 
    DT_in=np.roll(inroll,1)-inroll
    # find last point of each data from introl and outroll at the lasers
    index_in=list(np.where(abs(DT_in)>0.08)[0])
    index_in.append(len(inroll)-1)
    DT_out=np.roll(outroll,1)-outroll
    index_out=list(np.where(abs(DT_out)>0.08)[0])
    index_out.append(len(outroll)-1)
    #return introll and outroll points and indexes
    return inroll,outroll,np.array(index_in).astype(int),np.array(index_out).astype(int)

    #calculate the time when the ball goes through  the middle of the laser 
def mean_func(Time,Voltages):
    from Rolling_ball_functions import data_sorting
    import numpy as np
    mean_Roll={}
    std_Roll={}
    for i in range(len(Time)):
        mean_Roll[i]=[]
        std_Roll[i]=[]
        Roll=data_sorting(Time[i],Voltages[i])
        for j in range(0,len(Roll[3])-1):
            mean_Roll[i].append((np.mean(Roll[1][Roll[3][j]:Roll[3][j+1]])+np.mean(Roll[0][Roll[2][j]:Roll[2][j+1]]))/2)
            std_Roll[i].append((np.std(Roll[1][Roll[3][j]:Roll[3][j+1]])+np.std(Roll[0][Roll[2][j]:Roll[2][j+1]])))
        mean_Roll[i]=np.array(mean_Roll[i])-min(mean_Roll[i])
    return mean_Roll,std_Roll
