class Player:
    def __init__(self, name="NEO", xp=0, unlocked_level=1):
        self.name = name
        self.xp = xp
        self.unlocked_level = unlocked_level

    def gain_xp(self, amount):
        self.xp += amount

    def unlock_next(self):
        self.unlocked_level += 1

    def summary(self):
        return {"name": self.name, "xp": self.xp, "unlocked_level": self.unlocked_level}
