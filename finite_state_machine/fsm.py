class FiniteStateMachine:
  # Q = set of all states
  # sigma = set of all inputs
  # q0 = start state / initial state
  # F = set of final states
  # delta = transition function: (Q, sigma) -> Q
  def __init__(self, Q, sigma, q0, F, delta):
    self.Q = Q
    self.sigma = sigma
    self.q0 = q0
    self.F = F
    self.delta = delta


def run_fsm(fsm, inputs):
  fsm_state = fsm.q0
  for inp in inputs:
    if not inp in fsm.sigma:
      raise ValueError("input not in sigma")
    if (fsm_state, inp) in fsm.delta:
      fsm_state = fsm.delta[(fsm_state, inp)]
    else:
      return False
  return fsm_state in fsm.F


"""
FSM that decides if exactly 25c was produced out of
5c, 10c and 20c coins.
"""
def parking_meter():
  Q = set([0, 5, 10, 15, 20, 25])
  sigma = set([5, 10, 20])
  q0 = 0
  F = set([25])
  delta = {
    (0, 5): 5,
    (0, 10): 10,
    (0, 20): 20,
    (5, 5): 10,
    (5, 10): 15,
    (5, 20): 25,
    (10, 5): 15,
    (10, 10): 20,
    (15, 5): 20,
    (15, 10): 25,
    (20, 5): 25
  }
  return FiniteStateMachine(Q, sigma, q0, F, delta)


"""
FSM that decides if a string contains an even number of B's.
"""
def even_ones():
  Q = set(['X', 'Y'])
  sigma = set(['A', 'B'])
  q0 = 'X'
  F = set(['X'])
  delta = {
    ('X', 'A'): 'X',
    ('X', 'B'): 'Y',
    ('Y', 'A'): 'Y',
    ('Y', 'B'): 'X'
  }
  return FiniteStateMachine(Q, sigma, q0, F, delta)


if __name__ == '__main__':
  # Parking meter example
  # example_input = [20, 20]
  # output = run_fsm(parking_meter(), example_input)
  # print(f'Parking meter: {output}')

  # Count ones example
  example_input = "ABBABABABBABB"
  output = run_fsm(even_ones(), example_input)
  print(f'Count ones: {output}')
