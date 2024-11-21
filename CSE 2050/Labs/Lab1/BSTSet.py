from BSTNode import BSTNode

# Public interface: users only interact with the class BSTMap.
# Methods in BSTSet often call BSTNode methods, which do the heavy lifting.
class BSTSet:
    def __init__(self):
        self._head = None

    # classic iteration (bad)
    def __iter__(self):
        return iter(self._head)

    # generator based iteration (good)
    def in_order(self):
        yield from self._head.in_order()



    # TODO: How should these methods call the BSTNode methods?
    def put(self, key):
        """Add a specified key to the BSTSet."""
        if self._head is None:
            self._head = BSTNode(key)
        else:
            self._head.put(key)

    def pre_order(self):
        """Iterates through the BSTSet in pre-order."""
        if self._head is not None:
            yield from self._head.pre_order()

    def post_order(self):
        """Iterates through the BSTSet in post-order."""
        if self._head is not None:
            yield from self._head.post_order()