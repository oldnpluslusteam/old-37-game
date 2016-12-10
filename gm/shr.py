
class SharedGameState:
    def __init__(self):
        self._itemQueue = []
        self._stats = {}

        self.set_stat('hp-xyz', 1)
        self.set_stat('hp-rust', 1)
        self.set_stat('energy', 1)

    def set_stat(self, name, value):
        self._stats[name] = min(max(0., value), 1.)


    def get_stat(self, name):
        return self._stats[name]

    @property
    def items_queue(self):
        return self._itemQueue


class ItemType:
    def __init__(self, name, effect, spriteName):
        self._name = name
        self._effect = effect
        self._spriteName = spriteName

    def apply(self, state):
        """
        :param state:SharedGameState
        :return:
        """
        for stat, f in self._effect.items():
            state.set_stat(stat, eval(f.format(state.get_stat(stat))))

    @property
    def sprite(self):
        return self._spriteName

    @property
    def name(self):
        return self._name

