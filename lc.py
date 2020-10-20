from keyword import kwlist
from inspect import getsource

reserved = kwlist
kwlist.append("id")
kwlist.remove("lambda")

def parse(characters):
	for old, new in {"\\": " lambda ", ".": ":"}.items():
		characters = characters.replace(old, new)

	calling_function = False
	iterations_to_skip = 0
	for i, token in enumerate(tokens := characters.split()):
		print("Token:", token)
		if token in reserved:
			print("In reserved:", token)
			tokens[i] = "_" + token

		if iterations_to_skip > 0:
			iterations_to_skip -= 1
			continue
		elif token == "=":
			calling_function = False
		elif token == ":":
			calling_function = True
			iterations_to_skip = 1
		elif i == 0:
			calling_function = True
			continue
		elif calling_function and tokens[i - 1] != "lambda":
			tokens[i] = f"({tokens[i]})"

	return " ".join(tokens)

def main():
	#####
	_id = lambda x: x
	true = lambda x: lambda y: x
	false = lambda x: lambda y: y
	_if = lambda state: lambda x: lambda y: state(x)(y)
	_and = lambda a: lambda b: _if(a)(b)(false)
	_or = lambda a: lambda b: _if(a)(true)(b)
	_not = lambda a: _if(a)(false)(true)
	#####
	print("λ")
	while True:
		as_python = parse(input("> "))
		try:
			result = eval(f"{as_python}")
			try:
				if callable(result):
					name_fetcher = lambda l: getsource(l).split('=')[0].strip()
					print(f"<{name_fetcher(result)}>")
				else:
					print(result)
			except OSError:
				raise SyntaxError

		except SyntaxError:  # can't assign anything if eval evaluates a declaration
			exec(as_python)

if __name__ == "__main__":
	main()