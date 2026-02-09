class Example:
    shared = "class value"
    def __init__(self, name):
        self.name = name
a = Example("A")
b = Example("B")
print("Initial state:")
print(f"a.name = {a.name}, a.shared = {a.shared}")
print(f"b.name = {b.name}, b.shared = {b.shared}")
a.shared = "instance A value"
print("After shadowing on A:")
print(f"a.shared = {a.shared}")
print(f"b.shared = {b.shared}")
Example.shared = "modified class value"
print("After modifying Example.shared:")
print(f"a.shared = {a.shared}")
print(f"b.shared = {b.shared}")
del a.shared
print("After deleting a.shared:")
print(f"a.shared = {a.shared}")
print(f"b.shared = {b.shared}")