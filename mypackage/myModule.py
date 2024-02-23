
def returnTopN(items,n):
    """
    This function accept an input and output the top N 
    values in ascending order of magnitude.

    args:
     items - list,tuple,set
     n - n values to be returned.

     Returns:
        top n values to be returned.

    """

    sort_ = sorted(items,reverse= True)
    return sort_[:n]



a= returnTopN([1,2,3,5,76,67],3)
print(a)