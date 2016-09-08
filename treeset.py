mport bisect

class TreeSet(object):
    def __init__(self, elements):
        self._treeset = []
        self.addAll(elements)

    def addAll(self, elements):
        for element in elements:
            if element in self: continue
            self.add(element)

    def add(self, element):
        if element not in self:
            bisect.insort(self._treeset, element)

    def ceiling(self, e):
        index = bisect.bisect_right(self._treeset, e)
        if self[index - 1] == e:
            return e
        return self._treeset[bisect.bisect_right(self._treeset, e)]

    def floor(self, e):
        index = bisect.bisect_left(self._treeset, e)
        if self[index] == e:
            return e
        else:
            return self._treeset[bisect.bisect_left(self._treeset, e) - 1]

    def __getitem__(self, num):
        return self._treeset[num]

    def __len__(self):
        return len(self._treeset)

    def clear(self):
        self._treeset = []

    def clone(self):
        return TreeSet(self._treeset)

    def remove(self, element):
        try:
            self._treeset.remove(element)
        except ValueError:
            return False
        return True

    def __iter__(self):
        for element in self._treeset:
            yield element

    def pop(self, index):
        return self._treeset.pop(index)

    def __str__(self):
        return str(self._treeset)

    def __eq__(self, target):
        if isinstance(target, TreeSet):
            return self._treeset == target.treeset
        elif isinstance(target, list):
            return self._treeset == target

    def __contains__(self, e):
        try:
            return e == self._treeset[bisect.bisect_left(self._treeset, e)]
        except:
            return False

