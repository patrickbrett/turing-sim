class TuringMachine:
  # defined by (Q, sigma, gamma, _del, q0, b, F)

  # Q = set of all states
  # sigma = set of all inputs
  # gamma = set of tape symbols

  # _del = transition function: (Q x sigma) -> gamma x (R/L) x Q where
  # Q is a state,
  # sigma is an input,
  # gamma is a tape symbol,
  # R/L indicates the direction to move,
  # Q is a new state

  # q0 = start state / initial state
  # b = blank symbol (does not belong to sigma/gamma)
  # F = set of final states (accept state and reject state)
  def __init__(self, Q, sigma, gamma, _del, q0, b, F):
    self.Q = Q
    self.sigma = sigma
    self.gamma = gamma
    self._del = _del
    self.q0 = q0
    self.b = b
    self.F = F

