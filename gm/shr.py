class SharedGameState:
    def __init__(self):
        self._itemQueue = []
        self._stats = {}

        self.set_stat('hp-xyz', .5)
        self.set_stat('hp-rust', .5)
        self.set_stat('energy', 1)

    def set_stat(self, name, value):
        self._stats[name] = min(max(0., value), 1.)

    def get_stat(self, name):
        return self._stats[name]

    def apply_effects(self, effects):
        for stat, f in effects.items():
            self.set_stat(stat, eval(f.format(self.get_stat(stat))))

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
        state.apply_effects(self._effect)

    @property
    def sprite(self):
        return self._spriteName

    @property
    def name(self):
        return self._name
