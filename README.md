# Python and C/C++ solutions for Leetcode

## Problems & Solutions

| # | Title | Solution | Basic idea (One line) |
|---| ----- | -------- | --------------------- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/001_Two_Sum.py) | 1. Hash O(n) and O(n) space.<br>2. Sort and search with two points O(n) and O(1) space. |

        """
        threshold function for classification
        :param u: input number
        :return: 1 if the input is greater than 0, otherwise -1
        >>> data = [[0],[-0.5],[0.5]]
        >>> targets = [1,-1,1]
        >>> perceptron = Perceptron(data,targets)
        >>> perceptron.sign(0)
        1
        >>> perceptron.sign(-0.5)
        -1
        >>> perceptron.sign(0.5)
        1
        """
