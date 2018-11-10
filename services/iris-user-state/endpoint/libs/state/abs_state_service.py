from abc import ABCMeta, abstractmethod
import json
import redis

class AbsStateService(metaclass=ABCMeta):
  def __init__(self, namespace):
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    self.redis = redis.StrictRedis(connection_pool=pool)
    self.namespace = namespace

  def get(self, id):
    state = self.redis.hget(self.namespace, id)
    if state is None:
      return None
    else:
      return { "value": json.loads(state) }

  def set(self, id, state):
    return self.redis.hset(self.namespace, id, json.dumps(state))

  def update(self, id, params):
    s0 = self.get(id)
    s1 = self.updater(s0, params)
    return self.set(id, s1)

  def listUpdate(self, id, paramsList):
    s0 = self.get(id)
    s1 = reduce(self.updater, paramsList)
    return self.set(id, s1)

  @abstractmethod
  def updater(self, id, params):
    pass
