def until(n, filter_func, v):
    if v == n: return []
        if filter_func(v): return [v] + until( n, filter_func, v+1 )
    else: return until(n, filter_func, v+1)
