import math

def minEatingSpeed(piles, H):
    def canEatAllBananas(piles, K, H):
        return sum(math.ceil(pile / K) for pile in piles) <= H

    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2
        if canEatAllBananas(piles, mid, H):
            right = mid
        else:
            left = mid + 1

    return left


piles1, H1 = [3, 6, 7, 11], 8
print(minEatingSpeed(piles1, H1))

piles2, H2 = [30, 11, 23, 4, 20], 5
print(minEatingSpeed(piles2, H2))

piles3, H3 = [30, 11, 23, 4, 20], 6
print(minEatingSpeed(piles3, H3))
