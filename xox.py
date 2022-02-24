import os
import platform

#indexes
a = {"X": [], "O": []}
b = {"X": [], "O": []}
c = {"X": [], "O": []}

letter = ["X", "O"]
anun = ["a", "b", "c"]


def get_user(string):
	try:
		x = list(input("\n\nPLAYING WITH {0},PLAY INDEX for {1}:".format(string, string)))
		if len(x) > 2 or len(x) < 2:
			print("INVALID INPUT range")
			x = get_user(string)
			return x
		elif x[0] != "a" and x[0].lower() != "b" and x[0].lower() != "c":
			print("INVALID INPUT letter")
			x = get_user(string)
			return x
		elif int(x[1]) > 3 or int(x[1]) == 0 or int(x[1]) < 0:
			print("INVALID INPUT num")
			x = get_user(string)
			return x
		else:
			return x
	except KeyboardInterrupt:
		print("\nexiting...")
		return None


def output():
	#gives the output indexed xox board
	whole = []
	w = []
	t = 0
	nerga = []
	for i in range(0, 3):
		for m in list(globals()[anun[i]].values()):
			for g in m:
				nerga.append(int(g))
				if t == 1:
					if int(g) >= 1:
						w.insert(int(g)-1, "O")
				elif t == 0:
					if int(g) >= 1:
						w.insert(int(g), "X")
			t += 1
		for z in range(1, 4):
			if z not in nerga:
				w.insert(z-1, "=")
		whole.append(w)
		t = 0
		nerga = []
		w = []
	print("(a)  {0}\n\n(b)  {1}\n\n(c)  {2}\n\n    (1) (2) (3)".format("   ".join(whole[0]), "   ".join(whole[1]), "   ".join(whole[2])))


def check_win():
	for let in letter:	    
		combin = []
		for i in a[let]:
			for e in b[let]:
				for y in c[let]:
					combin.append(i+e+y)
		for i in combin:
			if i == '111' or i == '222' or i == '333' or i == '123' or i == '321':
				print("\n\n#########{0} you have Won!!#########".format(let))
				return True
		for i in anun:
			t = globals()[i]
			if len(t[let]) == 3:
				print("\n\n#########{0} you have Won!!#########".format(let))
				return True
		if sum(len(i) for i in a.values())+sum(len(i) for i in b.values())+sum(len(i) for i in c.values()) == 9:
			print("\n\n#########IT'S A TIE#########")
			return True


def check_duplicate(inp, arr, string):
	for let in letter:
		if sum(map(len, arr.values())) >= 3:
			while globals()[inp[0]] == arr:
				inp = get_user(string)
			return inp
		elif inp[1] in arr["X"] or inp[1] in arr["O"]:
			print("ALready Exists")
			while inp[1] in arr["X"] or inp[1] in arr["O"]:
				inp = get_user(string)
				arr = globals()[inp[0]]
			return inp
		else:
			return inp
		digit += 1


def game():
	try:
		x = get_user("X")
		t = globals()[x[0]]
		x = check_duplicate(x, t, "X")
		try:
			if x[0] == "a":
				a["X"].append(x[1])
			elif x[0] == "b":
				b["X"].append(x[1])
			elif x[0] == "c":
				c["X"].append(x[1])
			check_win()
		except Exception:
			pass
		if platform.system() == "Linux":
			os.system("clear")
		if platform.system() == "Windows":
			os.system("cls")
		output()
		if check_win() == True:
			return None
		try:
			o = get_user("O")
			y = globals()[o[0]]
			o = check_duplicate(o, y, "O")
		except KeyboardInterrupt:
			return None	
		try:
			if o[0] == "a":
				a["O"].append(o[1])
			elif o[0] == "b":
				b["O"].append(o[1])
			elif o[0] == "c":
				c["O"].append(o[1])
			check_win()
		except Exception:
			pass
		if platform.system() == "Linux":
			os.system("clear")
		if platform.system() == "Windows":
			os.system("cls")
		output()
		if check_win() == True:
			return None
		game()
	except KeyboardInterrupt:
		print("exciting...")
		return None
	except TypeError:
		return None
def play():
	try:
		agree_yes_no = input("DO YOU WANNA PLAY(YES or NO):")
		if agree_yes_no.lower() == "yes" or agree_yes_no == "yes":
			print("(a)  =   =   =\n\n(b)  =   =   =\n\n(c)  =   =   =\n\n    (1) (2) (3)")
			game()
		else:
			print("exiting...")
			return 0
	except KeyboardInterrupt:
		print("\n\nexiting...")
		return None

play()
