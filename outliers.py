def detect_outliers(df, col, ecart_accepte):
    q1 = df[col].quantile(q=0.25)
    q3 = df[col].quantile(q=0.75)
    diff = q3 - q1
    lower_bound = q1 - ecart_accepte*diff
    upper_bound = q3 + ecart_accepte*diff
    outliers = df[(df[col]>upper_bound) | (df[col]<lower_bound)]
    return [lower_bound, upper_bound], outliers

IC, outliers  = detect_outliers(products, 'price', ecart_accepte=1.5)
