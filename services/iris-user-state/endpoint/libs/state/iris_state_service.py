from .abs_state_service import AbsStateService

class IrisStateService(AbsStateService):
  def __init__(self,):
    super().__init__("iris")

  def updater(self, s0, params):
    return list(params)
