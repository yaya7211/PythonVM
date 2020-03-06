from sys import argv
import abc

f = open(argv[1], "r").read().split("\n")
line = 0
mem = []
var = {}




def goDeepestIn(liste):
	global mem
	if liste == mem:
		memou = mem
	else: memou = liste
	while len(memou) > 0 and type(memou[-1]) == list:
		memou = memou[-1]
	return memou 

def typer(iterable):
	typ, value = iterable.split(":")
	if typ == "num": 
		return float(value)
	elif typ == "str": 
		return value
	elif typ == "var": 
		return var[value]

def parent():
	global memou
	global mem
	x = memou.copy()
	memou = mem
	while not x in memou:
		memou = memou[-1]
    
def ADD(iterable):  
    return 0 if not iterable else iterable[0] + ADD(iterable[1:])

def STRC(iterable):   
    return 0 if not iterable else iterable[0] - STRC(iterable[1:])

    
def CONC(iterable):  
    return "" if not iterable else iterable[0] + CONC(iterable[1:])

def MULT(iterable):  
	return 1 if not iterable else iterable[0] * MULT(iterable[1:])


def DIV(iterable):  
	return 1 if not iterable else iterable[0] / DIV(iterable[1:])

    
def EXP(iterable):  
    return 1 if not iterable else iterable[0] ** EXP(iterable[1:])

    
def INP(iterable):
    return types(iterable[1])(input(iterable[0]))


def OUT(*_):
    print("".join(str(memou[-1])))

    
def LOAD(iterable):
	return typer(iterable)

    
def SET(iterable):
    typ, name = iterable.split(":")
    if typ == "var": 
    	var.update({name:goDeepestIn(mem)[-1]})

    
def JMP(l):
    line = int(l)


def NEXT(*_):
	global memou
	global mem
	if memou == mem:
		mem = []
		memou = goDeepestIn(mem)
	else:
		parent()
		del memou[-1]
		memou.append([])
		memou = goDeepestIn(mem)

def openNewBloc(*_):
	global mem
	global memou
	memou = goDeepestIn(mem)
	memou.append([])
	memou = goDeepestIn(mem)

def closeBloc(*_):
	global mem
	global memou
	m = memou.copy()
	parent()
	del memou[-1]
	memou.append(m[-1])





stockOutputInMem = {"ADD":ADD,
                    "STRC":STRC,
                    "CONC":CONC,
                    "MULT":MULT,
                    "EXP":EXP,
                    "DIV":DIV,
                    "INP":INP,
                    "LOAD":LOAD}
checkStockOUtputInMem = ["ADD", "STRC", "CONC", "MULT", "EXP", "DIV", "INP", "LOAD"]
usesMemAsArg = ["ADD", "STRC", "CONC", "MULT", "EXP", "DIV", "OUT"]

independantInstructions = {"SET":SET,
						   "JMP":JMP,
						   "NEXT":NEXT,
						   "OUT":OUT,
						   "{":openNewBloc,
						   "}":closeBloc}

memou = mem				                     
while line < len(f):
	instruction = f[line].split(" ")
	instruction, args = instruction[0], " ".join(instruction[1:])
	if instruction in checkStockOUtputInMem and instruction in usesMemAsArg: 
		memou.append(stockOutputInMem[instruction](memou))
	elif instruction in checkStockOUtputInMem: 
		memou.append(stockOutputInMem[instruction](args)) 
	else: 
		independantInstructions[instruction](args)
	line += 1
	print(line, mem, memou, memou is goDeepestIn(mem), var)

        
                    

       

    


#Calcules basiques et io
#Instructions dans instructions
#Créations de variables

