class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stream = list(range(1, n + 1))
        stack = list()
        result = list()
        count = 0

        def push(n: int):
            stack.append(n)
            result.append("Push")

        def pop():
            stack.pop()
            result.append("Pop")

        for i in range(len(stream)):
            push(stream[i])

            if stream[i] == target[count]:
                count += 1
                # If we've matched all target elements, we can stop
                if count == len(target):
                    break
            else:
                pop()  # Remove the "Push" we just added

        return result