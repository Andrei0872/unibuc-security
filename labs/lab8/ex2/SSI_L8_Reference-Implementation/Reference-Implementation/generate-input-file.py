INPUT_FILE_NAME = 'input.txt'
GENERATED_ROWS_COUNT = int(10e5)
BASE_WORD = 'andrei'

with open(INPUT_FILE_NAME, 'w') as f:
  for i in range(GENERATED_ROWS_COUNT):
    f.write(BASE_WORD + str(i) + '\n')

# for i in range(GENERATED_ROWS_COUNT):
#   print(BASE_WORD + str(i))