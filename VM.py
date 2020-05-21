from sys import argv

f = open(argv[1], "r").read().replace("\n", "").split(";")
stack = [None, None]
sett = {}

def STR(*_):
	strs = "0123456789ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\\/(()[]{ }-_'\"<>?!;:,.^%$£€"
	final = []
	for x in stack.pop(): final.append(strs[x])
	stack.append(final)

def OUT(*_): print(stack.pop())

def LOAD(x):
	try:
		x = int(x) if not "/" in x else [int(y) for y in x.split("/")]
	except TypeError:
		x = parse
	stack.append(x)

def CONC(*_): stack.append(stack.pop()+stack.pop())

def SUP(*_):
	if stack.pop() < stack.pop(): stack.append(1)
	else: stack.append(0)

def INF(*_):
	if stack.pop() > stack.pop(): stack.append(1)
	else: stack.append(0)

def EQL(*_):
	if stack.pop() == stack.pop(): stack.append(1)
	else: stack.append(0)

def DIF(*_):
	if stack.pop() != stack.pop(): stack.append(1)
	else: stack.append(0)

def EVAL(x):
	comparaisons = {"SUP":SUP,
					"INF":INF,
					"EQL":EQL,
					"DIF":DIF}
	comparaisons[x]()

def ADD(*_): stack.append(stack.pop()+stack.pop())

def SUB(*_): stack.append(-stack.pop() + stack.pop())

def MUL(*_): stack.append(stack.pop() * stack.pop())

def DIV(*_): stack.append(1 / stack.pop() * stack.pop())

def EXP(*_):
	a, b = stack.pop(), stack.pop()
	stack.append(b ** a)

def IF(z):
	if stack.pop(): return
	else: 
		global l
		l += int(z)

def LABEL(*a):
	sett.update({a[0]:a[1]})

instructions = {"LOAD":LOAD,
				"ADD":ADD,
				"SUB":SUB,
				"MUL":MUL,
				"DIV":DIV,
				"EXP":EXP,
				"OUT":OUT,
				"CONC":CONC,
				"EVAL":EVAL,
				"STR":STR,
				"IF":IF,
				"LABEL":LABEL,
				"#":lambda *_: 0,
				"CLOAD":CLOAD
}

def parse(e):
	l = 0
	while l < e-1:
		x = f[l] 
		x = x.replace("\n", "")
		x = x.split(" ")
		instructions[x[0]](" ".join(x[1:]))
		print(stack, l)
		l += 1
