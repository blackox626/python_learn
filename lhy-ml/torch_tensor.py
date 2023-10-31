import torch

# permute()和view() 区别
# https://zhuanlan.zhihu.com/p/88311093

x = torch.empty(5, 4, dtype=torch.int)
print(x, len(x))

t = torch.tensor([1, 2, 3, 4])
print(len(t))
print(t.shape)  # print(t.size())

p = torch.tensor([[1], [2], [3], [4]])
print(len(p))
print(p.shape)  # print(p.size())

print(p.size(0), p.size(1))

x[0:1, :] = torch.tensor([1, 2, 3, 4])
print(x)

print(x[-1])

print(x[-5].repeat(3, 1))

x = x.repeat(1, 5)
print(x)
print(x.shape)

x = x.view(5, 5, 4)

print(x)
print(x.shape)

x = x.permute(1, 0, 2)

print(x)
print(x.shape)

print(x[0])
print(x[0][0])

a = torch.tensor([[[1,2,3],[4,5,6],[7,8,9]],[[17,18,19],[27,28,29],[10,11,12]]])
print(a)
b = a.permute(1,0,2)
print(b)

c = a.permute(2,1,0) # 3 * 3 * 2
print(c)

