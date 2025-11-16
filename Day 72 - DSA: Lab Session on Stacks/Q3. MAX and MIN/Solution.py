class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        MOD = 10**9 + 7

        def get_contribution(array, n, is_max):
            stack = []
            left = [0] * n
            right = [0] * n

            # Calculate left distance
            for i in range(n):
                count = 1
                while stack and ((array[stack[-1][0]] < array[i]) if is_max else (array[stack[-1][0]] > array[i])):
                    count += stack.pop()[1]
                stack.append((i, count))
                left[i] = count

            stack.clear()
            # Calculate right distance
            for i in range(n - 1, -1, -1):
                count = 1
                while stack and ((array[stack[-1][0]] <= array[i]) if is_max else (array[stack[-1][0]] >= array[i])):
                    count += stack.pop()[1]
                stack.append((i, count))
                right[i] = count

            contribution = 0
            for i in range(n):
                contribution += array[i] * left[i] * right[i]
                contribution %= MOD
            return contribution

        n = len(A)
        max_sum = get_contribution(A, n, True)
        min_sum = get_contribution(A, n, False)

        return (max_sum - min_sum) % MOD
