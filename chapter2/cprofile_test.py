import cProfile
from palingrams import get_palingrams
from palingrams_optimized import find_palingrams
import time

#cProfile.run('get_palingrams()')
#cProfile.run('find_palingrams()')

start_time = time.time()
palingrams = find_palingrams()
end_time = time.time()
print("Runtime for this program was {} seconds.".format(end_time - start_time))