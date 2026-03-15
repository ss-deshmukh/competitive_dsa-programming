class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        hash_map = dict()
        min_v = float(+inf)
        max_v = float(-inf)
        for i in range(len(arr)):
            min_v = min(min_v, arr[i])
            max_v = max(max_v, arr[i])
            hash_map[arr[i]] = i

        if (max_v - min_v) % (len(arr) - 1) == 0:
            diff = (max_v - min_v) / (len(arr) - 1)
            for i in range(len(arr)):
                if (min_v + (i * int(diff))) not in hash_map:
                    return False
        else:
            return False

        return True
