'''
Example:
If we have one model whose precision = 0.0 and 
recall = 1.0, and we want to measure average?
'''
import numpy as np 
from scipy.stats import hmean
precision=0.0
recall=1.0

# taking arithmetic mean
arithmetic_mean=np.mean([precision,recall])
print("arithmetic_mean:",arithmetic_mean)

# taking harmonic mean
harmonic_mean=hmean([precision,recall])
print("harmonic mean:",harmonic_mean)

'''
Output:
arithmetic_mean: 0.5
harmonic mean: 0.0
'''

'''
Conclusion:
Taking arithmetic mean it says,
our model predicts each observation is 50% 
correct, but when we take the hmean of this 
data, then reality reveals that the model 
correctly predicted 0% of the observations. 
So whenever we want to take an average of the 
rate at that time, we should use the harmonic mean.
'''
