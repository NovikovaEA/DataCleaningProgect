def find_outliers_quantile(data, feature, left=0.01, right=0.99):
<<<<<<< HEAD
    #changes
=======
    #update
>>>>>>> main
    x = data[feature]
    lower_bound = x.quantile(left)
    upper_bound = x.quantile(right)
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
<<<<<<< HEAD
    return outliers, cleaned
=======
    return outliers, cleaned

>>>>>>> main
