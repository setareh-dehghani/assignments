def gemstones(arr):
    minerals=[set(i) for i in arr]
    return len(set.intersection(*minerals))