cases = int(input())
for i in range(cases):
	characters = input()
	expressions = []
	ok = True
	for character in characters:
		if character == "{" or character == "[" or character == "(":
			expressions.append(character)
		else:
			if len(expressions) > 0 and expressions[-1] == "{" and character == "}":
				expressions.pop()
			elif len(expressions) > 0 and expressions[-1] == "[" and character == "]":
				expressions.pop()
			elif len(expressions) > 0 and expressions[-1] == "(" and character == ")":
				expressions.pop()
			else:
				ok = False
				break
	if len(expressions) > 0:
		ok = False
	print("S" if ok else "N")