import check50
import re

GREETING_REGEX = re.compile(r"(hello|сәлем|hi|hey|)", re.IGNORECASE)

@check50.check()
def exists():
	"""Hello.java exist?"""
	check50.exists("Hello.java")

@check50.check(exists)
def compiles():
	"""Compiles 'Hello.java'"""
	check50.run("javac Hello.java").exit(0)

@check50.check(compiles)
def prints_hello():
	"""prints "hello, world\n" """
	output = check50.run("./Hello").stdout().strip()
	
	#Removing punctuation marks
	cleaned_output = re.sub(r"[^\w\s]", "", output)

	#Check are output have hello world text
	if not GREETING_REGEX.search(cleaned_output):
		raise check50.Failure("A greeting was expected for ecample: 'Hello', 'Привет', 'Сәлем'")

