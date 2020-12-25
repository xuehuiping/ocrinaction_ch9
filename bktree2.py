# -*- encoding: utf-8 -*-
"""
@date: 2020/12/24 10:11 下午
@author: xuehuiping
"""
import editdistance as ed


class Node(object):
    def __init__(self, word):
        self.word = word
        self.children = {}

    def __str__(self):
        return '<Node: %r>' % self.word


class BKTree(object):
    '''
    单词构建树
    '''

    def __init__(self, dist_func=ed.eval):
        self.root = None
        self.dist_func = dist_func

    def add(self, word):
        if self.root is None:
            self.root = Node(word)

        else:
            node = Node(word)
            curr = self.root
            distance = self.dist_func(word, curr.word)

            while distance in curr.children:
                curr = curr.children[distance]
                distance = self.dist_func(word, curr.word)

            curr.children[distance] = node
            node.parent = curr

    def search(self, word, max_distance):
        candidates = [self.root]
        found = []

        while len(candidates) > 0:
            node = candidates.pop(0)
            distance = self.dist_func(node.word, word)

            if distance <= max_distance:
                found.append(node)

            candidates.extend(child_node for child_dist, child_node in node.children.items()
                              if distance - max_distance <= child_dist <= distance + max_distance)

        return found


if __name__ == "__main__":
    words = ['word', 'work', 'warp', 'with', 'cord', 'sort', 'wise']
    tree = BKTree()
    for w in words:
        tree.add(w)

    r = tree.search('cord', 1)
    print(r)
