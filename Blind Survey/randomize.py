from itertools import combinations
import random
import os
import shutil

# Use a prime number for no reason
random.seed(7)

types = ["GAN", "REAL", "LCC"]

c_types = [ c for c in combinations(types, 2) ]

test_pairs = []
for t0,t1 in c_types:
    i0 = list(range(0, 11))
    i1 = list(range(0, 11))
    for i in range(0,10):
        c0 = random.choice(i0)
        c1 = random.choice(i1)
        i0.remove(c0)
        i1.remove(c1)
        f0 = "{}_{}.png".format(t0, c0)
        f1 = "{}_{}.png".format(t1, c1)
        f = [f0, f1]
        random.shuffle(f)
        test_pairs.append(f)

random.shuffle(test_pairs)

TEST_PAIRS_PATH = "test_pairs/{}"

# Create all the test pairs
for i, t_p in zip(range(30), test_pairs):
    print(t_p)
    test_pair_path = TEST_PAIRS_PATH.format(i)
    if not os.path.exists(test_pair_path):
        os.mkdir(test_pair_path)
    shutil.copy(t_p[0], test_pair_path)
    shutil.copy(t_p[1], test_pair_path)

'''
python3
['REAL_2.png', 'LCC_5.png']
['REAL_6.png', 'GAN_4.png']
['LCC_0.png', 'REAL_3.png']
['LCC_10.png', 'GAN_0.png']
['REAL_3.png', 'GAN_6.png']
['LCC_8.png', 'GAN_2.png']
['LCC_2.png', 'REAL_8.png']
['REAL_6.png', 'LCC_3.png']
['LCC_6.png', 'GAN_6.png']
['GAN_8.png', 'REAL_5.png']
['LCC_1.png', 'GAN_3.png']
['GAN_5.png', 'LCC_7.png']
['REAL_5.png', 'LCC_7.png']
['LCC_6.png', 'REAL_1.png']
['REAL_0.png', 'GAN_7.png']
['REAL_0.png', 'LCC_10.png']
['REAL_10.png', 'GAN_3.png']
['REAL_1.png', 'GAN_0.png']
['GAN_9.png', 'LCC_9.png']
['GAN_1.png', 'REAL_4.png']
['GAN_4.png', 'LCC_5.png']
['GAN_2.png', 'REAL_9.png']
['REAL_7.png', 'LCC_9.png']
['GAN_7.png', 'LCC_2.png']
['GAN_5.png', 'REAL_2.png']
['LCC_4.png', 'GAN_10.png']
['LCC_1.png', 'REAL_10.png']
['GAN_1.png', 'LCC_3.png']
['LCC_8.png', 'REAL_9.png']
['GAN_9.png', 'REAL_8.png']
'''
