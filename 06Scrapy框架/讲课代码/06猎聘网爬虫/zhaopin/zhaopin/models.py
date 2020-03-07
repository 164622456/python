import datetime
from datetime import timedelta

class ProxyModel(object):
    def __init__(self,proxy_dict):
        proxy = proxy_dict['data'][0]
        self.proxy_url = "https://" + proxy['ip'] + ":" + str(proxy['port'])
        expire_time_str = proxy['expire_time']
        # "expire_time":"2019-05-11 22:22:46"}
        self.expire_time = datetime.datetime.strptime(expire_time_str,'%Y-%m-%d %H:%M:%S')
        self.is_blacked = False

    @property
    def is_expiring(self):
        now = datetime.datetime.now()
        if (self.expire_time - now) <= timedelta(seconds=5):
            return True
        else:
            return False
