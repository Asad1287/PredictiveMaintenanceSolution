#learn distribution of the data vector 

import scipy.stats as stats
from typing import List , Tuple
import numpy as np
def learn_distribution(data:List[float]) -> Tuple[str, str]:
    """
    learn distribution of the data vector using scipy stats
    """
    dist_names = ['gamma', 'beta', 'norm','weibull_min', 'weibull_max','lognorm', 'expon', 'uniform']

    dist_results = []
    params = {}
    for dist_name in dist_names:
        dist = getattr(stats, dist_name)
        param = dist.fit(data)
        params[dist_name] = param
        # Applying the Kolmogorov-Smirnov test
        D, p = stats.kstest(data, dist_name, args=param)
        print("p value for {} is {}".format(dist_name, p))
        dist_results.append((dist_name, p))
    best_dist, best_p = (max(dist_results, key=lambda item: item[1]))
    
    #return as a json file with best fit distribution and parameters
    return best_dist, params[best_dist]

best_fit_dist,params = learn_distribution([1,5,7,4,5,3,4,5,7,8,5,4,3,4,5,7,8,6,6,5,5,4])


def generate_random_data(data:List[float], n:int) -> List[float]:
    """
    randomly sample n values from data vector
    """
    random_data = np.random.choice(data, n)
    mean = np.mean(random_data)
    std = np.std(random_data)
    #random generate 1000 values from the distribution
    random_data = np.random.normal(mean, std, n)
    return random_data
