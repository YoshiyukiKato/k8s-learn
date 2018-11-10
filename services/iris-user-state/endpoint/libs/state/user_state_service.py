from .abs_state_service import AbsStateService
import numpy as np

class UserStateService(AbsStateService):
  def __init__(self):
    super().__init__("user")

  def updater(self, s0, params):
    if s0 is None:
      return params
    else:
      weight = 1.0
      s1 = np.array(s0) + weight * np.array(params)
      return s1.tolist()
