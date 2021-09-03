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
      print('not in del:', (pda_state, inp, top(pda_stack)), pda._del)
      return False

    if has_match_inp or has_match_inp_ep:
      i += 1

  return pda_state in pda.F


def run_pda_nondeterministic(pda, inputs, pda_state=None, pda_stack=None):
  if pda_state is None:
    pda_state = pda.q0

  if pda_state in pda.F and not len(inputs):
    return True

  if pda_stack is None:
    pda_stack = [pda.z0]

  inp = inputs[0] if len(inputs) else None

  if len(inputs) and not inp in pda.sigma:
    raise ValueError("input not in sigma")

  matchers = [
    (pda_state, None, None),
    (pda_state, None, top(pda_stack)),
    (pda_state, inp, None),
    (pda_state, inp, top(pda_stack))
  ]
  
  for matcher in matchers:
    if not matcher in pda._del:
      continue
    if inp is None and matcher[1] is not None:
      continue

    stack_input = pda_stack if matcher[2] is None else pda_stack[:-1]
    remaining_inputs = inputs if matcher[1] is None else inputs[1:]

    pda_state_new, stack_changes = pda._del[matcher]
    pda_stack_new = stack_input + stack_changes
    if run_pda_nondeterministic(pda, remaining_inputs, pda_state_new, pda_stack_new):
      return True

  return False

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


"""
PDA that matches AABBBAA style strings (where the number of A's on either side of the B's is equal)
e.g.
AAABBAAA = valid
AAAA = invalid (because this automata is deterministic!)
AAAAABAAA = invalid
"""
def abba():
  Q = set(['q1', 'q2', 'q3'])
  sigma = set(['a', 'b'])
  gamma = set(['z0', 'a'])

  _del = {
    ('q1', 'a', None): ('q1', ['a']),
    ('q1', 'b', None): ('q2', []),
    ('q2', 'b', None): ('q2', []),
    ('q2', 'a', 'a'): ('q3', []),
    ('q3', 'a', 'a'): ('q3', []),
    ('q3', None, 'z0'): ('q4', []),
  }

  q0 = 'q1'
  z0 = 'z0'
  F = set(['q4'])

  return PushdownAutomata(Q, sigma, gamma, _del, q0, z0, F)


"""
modified version of the ABBA matcher that allows zero or more B's

e.g. AAAA is now valid
AAAAA is still invalid (as it's an odd number)
"""
def abba_nondeterministic():
  modified_abba = abba()
  modified_abba._del = {
    ('q1', 'a', None): ('q1', ['a']),
    ('q1', None, None): ('q2', []),
    ('q2', 'b', None): ('q2', []),
    ('q2', None, None): ('q3', []),
    ('q3', 'a', 'a'): ('q3', []),
    ('q3', None, 'z0'): ('q4', []),
  }
  return modified_abba


if __name__ == '__main__':
  # (0^n)(1^n) example
  # example_input = "00001111"
  # output = run_pda(n_zeros_n_ones(), example_input)
  # print(f'N zeros, n ones: {output}')

  # ABBA example
  # example_input = "aaaabbbbbaaaa"
  # output = run_pda(abba(), example_input)
  # print(f'ABBA: {output}')

  # ABBA nondeterministic example
  example_input = "aaabbbaaa"
  output = run_pda_nondeterministic(abba_nondeterministic(), example_input)
  print(f'ABBA: {output}')

