
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
    if (fsm_state, inp) in fsm.delta:
      fsm_state = fsm.delta[(fsm_state, inp)]
    else:
      return False
  return fsm_state in fsm.F


if __name__ == '__main__':
  Q = set([0, 5, 10, 15, 20, 25])
  sigma = set()
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

  example_fsm = FiniteStateMachine(Q, sigma, q0, F, delta)
  example_input = [5, 5, 10]
  output = run_fsm(example_fsm, example_input)
  print(output)
