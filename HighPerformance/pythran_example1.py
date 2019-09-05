#pythran export min_product(float32 list, float32 list)
def min_product(arr1, arr2):
    assert (len(arr1) == len(arr2)), 'mismatch in dimensions'
    return min([a*b for a,b in zip(arr1,arr2)])

