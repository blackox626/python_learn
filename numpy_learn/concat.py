import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

np.concatenate([arr1, arr2], axis=0)
np.concatenate([arr1, arr2], axis=1)

# [[ 1 2 3]
#  [ 4 5 6]
#  [ 7 8 9]
#  [10 11 12]]
#
# [[ 1 2 3 7 8 9]
#  [ 4 5 6 10 11 12]]


print(np.vstack((arr1, arr2)))
print(np.hstack((arr1, arr2)))

print(np.dstack((arr1, arr2)))  # (2,3,2)

print(np.r_['0,2,0', [1, 2, 3], [4, 5, 6]])
print(np.r_['0,2,1', [1, 2, 3], [4, 5, 6]])
print(np.r_['1,2,0', [1, 2, 3], [4, 5, 6]])
print(np.r_['1,2,1', [1, 2, 3], [4, 5, 6]])
