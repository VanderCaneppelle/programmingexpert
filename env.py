import os

test = os.environ.get("TEST")
print(test)

os.environ['VANDER'] = "CANEPPELLE"
print(os.environ.get("VANDER"))

os.environ['SOBRENOME'] = "CANEPPELLE"
print(os.environ.get("VANDER"))
