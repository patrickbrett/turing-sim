class PushdownAutomata:
  # Q = set of all states
  # sigma = set of all inputs
  # gamma = stack alphabet

  # _del = transition function: (q, a, X) -> Q where
  # 'q' is a state in Q, 'a' is either an input symbol in sigma or epsilon,
  # and 'X' is a stack symbol that is a member of gamma.
  # the output is (p, y) where p is a new state and
  # y is a string of stack symbols that replaces X at the top of the stack.

  # q0 = start state / initial state
  # z0 = start stack symbol
  # F = set of final states
  def __init__(self, Q, sigma, gamma, _del, q0, z0, F):
    self.Q = Q
    self.sigma = sigma
    self.gamma = gamma
    self._del = _del
    self.q0 = q0
    self.z0 = z0
    self.F = F


def top(stack):
  return stack[-1] if len(stack) else None


def run_pda(pda, inputs):
  pda_state = pda.q0
  pda_stack = [pda.z0]

  i = 0
  while i < len(inputs) or len(pda_stack) > 0:
    inp = inputs[i] if i < len(inputs) else None

    if i < len(inputs) and not inp in pda.sigma:
      raise ValueError("input not in sigma")

    has_match = (pda_state, None, top(pda_stack)) in pda._del
    has_match_ep = (pda_state, None, None) in pda._del
    has_match_inp = (pda_state, inp, top(pda_stack)) in pda._del
    has_match_inp_ep = (pda_state, inp, None) in pda._del

    if has_match:
      pda_state, stack_changes = pda._del[(pda_state, None, top(pda_stack))]
      pda_stack = pda_stack[:-1] + stack_changes
    elif has_match_ep:
      pda_state, stack_changes = pda._del[(pda_state, None, None)]
      pda_stack += stack_changes
    elif has_match_inp:
      pda_state, stack_changes = pda._del[(pda_state, inp, top(pda_stack))]
      pda_stack = pda_stack[:-1] + stack_changes
    elif has_match_inp_ep:
      pda_state, stack_changes = pda._del[(pda_state, inp, None)]
      pda_stack += stack_changes
    else:
      print('not in del: ', pda_state, inp, top(pda_stack))
      return False

    if has_match_inp or has_match_inp_ep:
      i += 1

  return pda_state in pda.F


"""
PDA that matches L = { (0^n)(1^n) | n >= 0 }
"""
def n_zeros_n_ones():
  Q = set(['q1', 'q2', 'q3'])
  sigma = set(['0', '1'])
  gamma = set(['z0', '0'])

  _del = {
    ('q1', '0', None): ('q1', ['0']),
    ('q1', '1', '0'): ('q2', []),
    ('q2', '1', '0'): ('q2', []),
    ('q2', None, 'z0'): ('q3', []),
  }

  q0 = 'q1'
  z0 = 'z0'
  F = set(['q3'])

  return PushdownAutomata(Q, sigma, gamma, _del, q0, z0, F)


if __name__ == '__main__':
  # (0^n)(1^n) example
  example_input = "00001111"
  output = run_pda(n_zeros_n_ones(), example_input)
  print(f'N zeros, n ones: {output}')
