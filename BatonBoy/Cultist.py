class Cultist(object):
    """One who takes on the right of summoning the baton and completing the ritual"""

    def __init__(self, name, cultist = None):
        self.hasSummoned = False
        self.hasSpoken = False
        self.name = name

        if cultist is not None:
            self.hasSummoned = cultist.hasSummoned
            self.hasSpoken = cultist.hasSpoken

    


