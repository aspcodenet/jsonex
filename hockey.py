class Player:
    Namn = ""
    Jersey  = 0
    Team = ""

    @classmethod
    def create(cls,in_dict:dict):
        a = cls()
        a.__dict__ = in_dict
        return a
