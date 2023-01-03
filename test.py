
import ABB as abb

root = abb.BST(5)
root.Insert(3)
root.Insert(6)

print(root.Size)
print(root.High)
print(root.left.High)
print(root.Min)
print(root.Max)
