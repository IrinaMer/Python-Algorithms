

string = "world job may!"
print("Исходная строка: " + string)


class Super_tree:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def child_of_tree(self):
        return self.left, self.right


def tree(key1, z=""):
    if type(key1) is str:
        return {
            key1: z
        }

    x, y = key1.child_of_tree()

    res = {}
    res.update(tree(x, z + "0"))
    res.update(tree(y, z + "1"))

    return res


n = {}
for li in string:
    if li not in n:
        n[li] = 0

    n[li] += 1

tree_1 = n.items()

while len(tree_1) > 1:
    tree_1 = sorted(tree_1, reverse=True, key=lambda x: x[1])
    c1, t1 = tree_1[-1]
    c2, t2 = tree_1[-2]
    tree_1 = tree_1[:-2]
    tree_1.append(
        (Super_tree(c1, c2), t1 + t2)
    )

code_0 = tree(tree_1[0][0])

code_1 = []
for li in string:
    code_1.append(code_0[li])

print("Закодированная строка: %s" % "".join(code_1))






