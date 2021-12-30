from collections import Counter


class Solution:
    # using most_common()
    # time O(nlogn), space O(n)
    def frequencySort(self, s: str) -> str:
        return "".join([v * k for k, v in Counter(s).most_common()])

    # using sort
    # time O(nlogn), space O(n)
    def frequencySort(self, s: str) -> str:
        return "".join(
            [v * k for k, v in sorted(Counter(s).items(), key=lambda x: -x[1])]
        )
