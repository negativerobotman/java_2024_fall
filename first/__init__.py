import check50

@check50.check()
def exists():
	"""Are hello.py exist?"""
	check50.exists("Hello.java")

@check50.check(exists)
def compiles():
	"""Compiles 'Hello.java'"""
	check50.run("javac Hello.java").exit(0)

@check50.check(compiles)
def prints_hello():
	"""prints "hello, world\n" """
	check50.run("./Hello").stdout("[Hh]ello, world!?\n", regex=True).exit(0)

