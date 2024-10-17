import check50
import re

@check50.check()
def exists():
    """Проверка наличия файла StudentSort.java"""
    check50.exists("StudentSort.java")

@check50.check(exists)
def compiles():
    """Проверка, что StudentSort.java компилируется"""
    check50.run("javac StudentSort.java").exit(0)

@check50.check(compiles)
def test_output():
    """Проверка сортировки и фильтрации студентов"""
    # Для теста вводим значение через stdin
    output = check50.run("java StudentSort").stdin("3.5").stdout()
    
    # Проверка правильной сортировки
    assert "Alice" in output, "Программа должна включать Alice"
    assert "Bob" in output, "Программа должна включать Bob"
    assert re.search(r"Alice.*Bob", output), "Alice должен быть перед Bob"

    # Проверка фильтрации
    assert "Charlie" not in output, "Charlie не должен появляться в выводе с баллом ниже 3.5"

@check50.check(test_output)
def additional_test():
    """Дополнительная проверка на фильтрацию с другим значением"""
    # Проверяем, что программа выводит корректный список
    output = check50.run("java StudentSort").stdin("4.0").stdout()
    
    # Проверяем, что отфильтрованы студенты с низким баллом
    assert "Alice" in output, "Alice должна быть в выводе"
    assert "Bob" not in output, "Bob не должен появляться в выводе при фильтрации выше 4.0"
