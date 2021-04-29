from riotwatcher import LolWatcher, ApiError


class Lolapi:
    def __init__(self):
        self.token = 'RGAPI-856c54bd-f78c-4f5e-b9cc-2f640fa33104'
        self.region = 'EUN1'

    def status(self, name):
        status = LolWatcher(self.token)
        me = status.summoner.by_name(self.region, name)
        my_rank = status.league.by_summoner(self.region, me['id'])
        return my_rank
