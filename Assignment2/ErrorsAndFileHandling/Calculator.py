class FormulaError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(self.value)

inp = input().split()
if(len(inp) != 3):
    raise FormulaError("Please enter operator and operands correctly")

val1, op, val2 = inp
try:
    val1 = float(val1)
    val2 = float(val2)
except ValueError:
    raise FormulaError("The operands value should be of number type")
if(op == "+"):
    print(val1 + val2)
elif(op == "-"):
    print(val1 - val2)
elif(op == "*"):
    print(val1 * val2)
elif(op == "/"):
    print(val1 / val2)
else:
    raise FormulaError(f'{op} is not a valid operator')

