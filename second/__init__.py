import check50
import subprocess
import os

@check50.check()
def exists():
	"""Book.java exists"""
	if not os.path.exists("Book.java"):
		raise check50.Failure("File Book.java don't exists.")


@check50.check(exists)
def compiles():
	"""Book.java can compile"""
	try:
		subprocess.run(["javac", "Book.java"], check=True)
	except subprocess.CalledProcessError:
		raise check50.Failure("Code can't compile.")

@check50.check(compiles)
def check_class_book():
	"""Class Book exists"""
	output = subprocess.run(
		["javap", "-p", "Book"],
		capture_output=True, text=True
	).stdout
	if "class Book" not in output:
		raise check50.Failure("Class book don't exists.")

@check50.check(compiles)
def check_abstract_class_price():
	"""Abstract class Price exists"""
	output = subprocess.run(
		["javap", "-p", "Price"],
		capture_output=True, text=True
	).stdout
	if "abstract class Price" not in output:
		raise check50.Failure("Abstract class Price don't exists.")

@check50.check(compiles)
def check_for_loop():
	"""Loop for uses"""
	with open("Book.java") as f:
		code = f.read()
		if "for (" not in code:
			raise check50.Failure("Loop for don't exists")
