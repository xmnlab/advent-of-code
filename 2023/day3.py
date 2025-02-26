""" """

test_set = ()

# test
for v in test_set:
    ...

with open("day{}-input.txt".format(), "r") as f:
    data_input = [int(d) for d in f.read().split("\n") if d != ""]

results = []
for v in data_input:
    ...
print("Result:", sum(results))
