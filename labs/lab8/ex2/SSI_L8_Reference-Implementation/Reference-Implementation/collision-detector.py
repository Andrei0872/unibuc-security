HASH_SEPARATOR = ' ::::: '
OUTPUT_TEST_FILE = 'output_test.txt'
OUTPUT_FILE = 'output.txt'

output_test_dict = None
with open(OUTPUT_TEST_FILE, 'r') as output_test:
  meaningful_lines = map(lambda line: tuple(reversed(line.strip().split(HASH_SEPARATOR))), output_test.readlines()[1:])
  output_test_dict = dict(meaningful_lines)

has_found_collision = False
with open(OUTPUT_FILE, 'r') as output:
  meaningful_lines = [*map(lambda line: tuple(reversed(line.strip().split(HASH_SEPARATOR))), output.readlines()[1:])]
  for hash, input in meaningful_lines:
    if hash in output_test_dict:
      print('Collision found!')
      print('{} collided with {}, both having the hash {}.'.format(input, output_test_dict[hash], hash))
      has_found_collision = True

if not has_found_collision:
  print('No collisions were found.')