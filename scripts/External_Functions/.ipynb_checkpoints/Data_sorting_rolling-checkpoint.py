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