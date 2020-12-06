def Residual_time(Time,Number):
    import numpy as np
    return Time/Number-np.mean(Time/Number)