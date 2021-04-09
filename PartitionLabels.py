class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        n = len(S)
        if n == 0:
            return []

        output = []
        start = 0
        # find the last occurrence of S[0]
        end = S.rfind(S[0])
        i = 0

        while i < n - 1:
            if i == end:
                # If none of the letters in the range [start, end] appears in the rest part,
                # append this range to the output
                output.append(end - start + 1)
                start = i + 1
                end = S.rfind(S[i + 1])
            else:
                end = max(end, S.rfind(S[i]))
            i += 1
        # append the rest part
        output.append(end - start + 1)

        return output
