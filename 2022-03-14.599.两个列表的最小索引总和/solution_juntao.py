class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        inCommon = list(set(list1).intersection(set(list2)))
        indexSum = defaultdict(list)
        for restaurant in inCommon:
            indexSum[list1.index(restaurant) + list2.index(restaurant)].append(restaurant)
        return min(indexSum.items())[1]