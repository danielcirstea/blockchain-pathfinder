from collections import deque
import copy


class Profile:
    """
    This implementation will use shift registers (deque in python) to transform the nodes into a register, based on the
    given pattern (p and q). The result will be a pq-profile list of deques of all nodes, which are passed ONLY ONCE.
    """

    def __init__(self, tree, p, q, rate=0):
        """
        :param tree: input_data graph
        :param p: depth
        :param q: breadth
        :param rate: user threshold
        """
        self.tree = tree
        self.p = p
        self.q = q
        self.profile = []
        self.root = tree[0][0]
        self.rate = rate
        self.leaves = self.get_leaves()
        self.children = self.get_children()

    @staticmethod
    def shift(reg, el):
        """
        :param reg: register shallow copy
        :param el: element to be shifted
        :return: new deque
        """
        reg = copy.copy(reg)
        reg.popleft()
        reg.append(el)
        return reg

    def get_leaves(self):
        """
        :return: all leaf nodes
        """
        leaves = []
        for item in self.tree[1]:
            if item not in self.tree[0]:
                leaves.append(item)
        return leaves

    def get_children(self):
        """
        :return: all children of a node
        """
        children = {}
        for node1, node2 in zip(self.tree[0], self.tree[1]):
            if node1 in children.keys():
                children[node1].append(node2)
            else:
                children[node1] = []
                children[node1].append(node2)
        return children

    def pq_gram_profile(self):
        """
        :return: graph profile
        """
        anc = deque(['*'] * self.p)
        profile = self.get_profile(self.profile, self.root, anc)
        return profile

    def append_profile(self, profile, gram) -> None:
        """
        :param profile: current pq-profile
        :param gram: the pq-gram to be appended
        :return: nothing
        """
        rate = 1.0
        for item in gram:
            if item == "*":
                rate -= 1 / len(gram)
        if rate >= self.rate:
            profile.append(gram)

    def get_profile(self, profile, node, anc):
        """
        :param profile: current profile of tree
        :param node: root node of profile
        :param anc: ancestor register
        :return: new profile
        """
        anc = self.shift(anc, node)
        sib = deque(['*'] * self.q)

        if node in self.leaves:
            self.append_profile(profile, anc + sib)
        else:
            for c in self.children[node]:
                sib = self.shift(sib, c)
                self.append_profile(profile, anc + sib)
                self.get_profile(profile, c, anc)
            for k in range(1, self.q):
                sib = self.shift(sib, '*')
                self.append_profile(profile, anc + sib)

        return profile
