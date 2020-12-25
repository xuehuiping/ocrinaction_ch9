# -*- encoding: utf-8 -*-
"""
@date: 2020/12/25 8:10 上午
@author: xuehuiping
"""


# https://github.com/ryanfox/bktree
class Node(object):
    def __init__(self, num):
        self.num = num
        self.children = {}

    def __str__(self):
        return str(self.num)


class BKTree(object):
    def __init__(self, nums=None):
        self.root = None
        if nums:
            for num in nums:
                self.add(num)

    def add(self, num):
        if self.root is None:
            self.root = Node(num)
        else:
            node = Node(num)
            curr = self.root
            distance = self._hamming(num, curr.num)

            while distance in curr.children:
                curr = curr.children[distance]
                distance = self._hamming(num, curr.num)

            curr.children[distance] = node
            node.parent = curr

    def search(self, num, max_distance):
        candidates = [self.root]
        found = []

        while len(candidates) > 0:
            node = candidates.pop(0)
            distance = self._hamming(node.num, num)

            if distance <= max_distance:
                found.append(node)

            candidates.extend(child_node for child_dist, child_node in node.children.items()
                              if distance - max_distance <= child_dist <= distance + max_distance)

        return found

    @staticmethod
    def _hamming(num1, num2):
        return bin(num1 ^ num2).count('1')


if __name__ == "__main__":
    tree = BKTree([0xff, 0xfe, 0xfd])
    r = tree.search(0xff, 1)
    print(r)
