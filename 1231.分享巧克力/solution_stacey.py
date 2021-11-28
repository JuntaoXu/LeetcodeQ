def maximizeSweetness(sweetness, k):
    k+=1
    if k == len(sweetness): return min(sweetness)
    min_sweet = max(sweetness)
    mean_sweet = sum(sweetness)/k
    i = 0
    while i < len(sweetness) and k > 0:
        cur_sum = 0
        if k == len(sweetness) - i:
            return min(min_sweet,min(sweetness[i:]))
        if sweetness[i] <= mean_sweet:
            while i < len(sweetness) and cur_sum < mean_sweet and k<=len(sweetness)-i:
                cur_sum+=sweetness[i]
                i += 1
                print(cur_sum)
            k-=1
            if cur_sum<min_sweet: min_sweet=cur_sum
        elif sweetness[i] > mean_sweet:
            k-=1
            i+=1
        print(min_sweet)
    return min_sweet

m = maximizeSweetness([1,2,3,4,5,6,7,8,9],5)
print(m)
