import sys

"""
Useful resources:

- https://raphiinconcordia.files.wordpress.com/2015/10/encyclopedia-of-cryptography-and-security.pdf (355-358)
- https://www.youtube.com/watch?v=Ks1pw1X22y4
- https://www.youtube.com/watch?v=1UCaZjdRC_c
- https://en.wikipedia.org/wiki/Linear-feedback_shift_register
"""


# dimension = 4
dimension = int(input("Dimension = "))
# initial_state = "1001"
initial_state = input("Binary string of dimension = {}: ".format(dimension))

# Where `1` -> apply `XOR``.
# coef_arr = [0, 0, 1, 1]
raw_coef_str = input("The coefficients array of dimension = {}: ".format(dimension))
coef_arr = [*map(int, list(raw_coef_str))]

def is_state_valid (state: str):
  return not all(c == '0' for c in state)

def is_coef_arr_valid (coef_arr):
  ones_count = 0

  for digit in coef_arr:
    if digit == 1:
      ones_count += 1
    
    if ones_count > 1:
      return True
  
  return False

if not is_state_valid(initial_state):
  print("The initial state is not valid!")
  sys.exit(1)

if not is_coef_arr_valid(coef_arr):
  print("The coefficients array is not valid!")
  sys.exit(1)

initial_state_nr = int(initial_state, 2)
state_len = len(initial_state)

last_state = initial_state_nr

period_length = 1
print(bin(initial_state_nr))

while True:
  feedback_bit = None
  for idx in range(0, state_len):
    val = coef_arr[idx]
    if val == 0:
      continue

    mirror_idx = state_len - idx - 1
    if feedback_bit == None:
      feedback_bit = last_state >> mirror_idx
      continue
    else:
      # is_first_operand = False
      feedback_bit = feedback_bit ^ (last_state >> mirror_idx)

  # Taking only the rightmost bit into account.
  feedback_bit = feedback_bit & 1

  result = (last_state >> 1) | (feedback_bit << (state_len - 1))
  print(bin(result))

  last_state = result

  if last_state == initial_state_nr:
    break

  period_length += 1

print(period_length)