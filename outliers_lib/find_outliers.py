'''
hjh
jjjjjjjjjh'''

def find_outliers_quantile(data, feature, left=0.01, right=0.99):
    """_summary_

    Args:
        data (_type_): _description_
        feature (_type_): _description_
        left (float, optional): _description_. Defaults to 0.01.
        right (float, optional): _description_. Defaults to 0.99.

    Returns:
        _type_: _description_
    """
    #changes
    x = data[feature]
    lower_bound = x.quantile(left)
    upper_bound = x.quantile(right)
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
    return outliers, cleaned


def new_function(a,b):
    pass 