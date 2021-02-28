import numpy as np
from statsmodels.stats.weightstats import DescrStatsW

def get_hist_array(h):
    """Convert the count distribution to a np.array

    Args:
        h (snap.TIntPrV): <Swig Object of type 'TVec< TPair< TInt,TInt >

    Returns:
        [np.array]: count distribtuion
    """
    return np.array([np.array([p.GetVal1(), p.GetVal2()]) for p in h]) 

def get_dist_stats(h):
    """Calculate summary stats for a count distribution

    Args:
        h (np.array)

    Returns:
        dict: summary stats
    """
    arr = get_hist_array(h)
    weighted_stats = DescrStatsW(
        arr[:, 0], # value (e.g. node degree)
        arr[:, 1], # number of times value appears in graph
        ddof=0
    )
    result = {
        'mean' : weighted_stats.mean,
        'std' : weighted_stats.std,
        'var' : weighted_stats.var,
        # 'std_mean' : weighted_stats.std_mean,
    }
    return result

def calc(g):
    """Calculate a graph's features

    Args:
        g ([snap.PNGraph]): a snap directed graph
    """
    def calc_count_distributions(funcs, names):
        """Calculate summary stats given distribution count of graph

        Args:
            funcs list(lambdas): list of functions that calculate
                count distributions
            names list(str): names of funcs

        Returns:
            dict: graph features
        """
        from operator import methodcaller

        count_vals_map = map(methodcaller('__call__', g), funcs)
        count_vals_dists = list(map(get_dist_stats, count_vals_map))
        for dist, name in zip(count_vals_dists, names):
            for stat in ['mean', 'std', 'var']: #TODO more stats?
                stats[name + '_' + stat] = dist[stat]

    stats = {}
    dist_count_funcs = [
        lambda g: g.GetOutDegCnt(),
        lambda g: g.GetInDegCnt(),
        lambda g: g.GetWccSzCnt(),
    ]
    dist_count_names = [
        'OutDegCnt',
        'InDegCnt',
        'WccSzCnt',
    ]

    calc_count_distributions(dist_count_funcs, dist_count_names)
    stats['n_triads'] = g.GetTriads()
    stats['clust_coef'], _ = g.GetClustCf(CCfByDeg=True)
    
    return stats