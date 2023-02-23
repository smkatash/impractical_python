import cProfile
from palingrams import get_palingrams
import time

# cProfile.run('get_palingrams()')

start_time = time.time()
palingrams = get_palingrams()
end_time = time.time()
print("Runtime for this program was {} seconds.".format(end_time - start_time))