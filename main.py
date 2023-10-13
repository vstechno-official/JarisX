class JarisX:

  def __init__(self):
    pass

  def greet(self):
    return "Hello, how can I assist you today?"

  def add(self, a, b):
    return a + b

  def subtract(self, a, b):
    return a - b

  def multiply(self, a, b):
    return a * b

  def divide(self, a, b):
    if b != 0:
      return a / b
    else:
      return "Error: Division by zero is not allowed."

  def power(self, a, b):
    return a**b

  def square_root(self, a):
    return a**0.5

  def factorial(self, n):
    if n == 0:
      return 1
    else:
      return n * self.factorial(n - 1)

  def fibonacci(self, n):
    if n <= 0:
      return "Input should be positive."
    elif n == 1:
      return [0]
    elif n == 2:
      return [0, 1]
    else:
      fib_list = [0, 1]
      while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
      return fib_list

  def prime_check(self, n):
    if n > 1:
      for i in range(2, int(n / 2) + 1):
        if (n % i) == 0:
          return False
          break
      else:
        return True
    else:
      return False

  def palindrome_check(self, word):
    return word == word[::-1]

  def sort_list(self, list_to_sort):
    return sorted(list_to_sort)

  def reverse_string(self, string_to_reverse):
    return string_to_reverse[::-1]

  def length_of_string(self, string_to_measure):
    return len(string_to_measure)

  def convert_to_uppercase(self, string_to_convert):
    return string_to_convert.upper()

  def current_date(self):
    from datetime import date
    return date.today()

  def current_time(self):
    from datetime import datetime
    return datetime.now().time()

  def day_of_week(self):
    import datetime
    return datetime.date.today().strftime("%A")

  def create_file(self, filename):
    with open(filename, 'w') as file:
      file.write("")
    return f"File '{filename}' created."

  def write_to_file(self, filename, content):
    with open(filename, 'a') as file:
      file.write(content)
    return f"Content added to '{filename}'."

  def read_file(self, filename):
    with open(filename, 'r') as file:
      return file.read()

  def delete_file(self, filename):
    import os
    os.remove(filename)
    return f"File '{filename}' deleted."

  def list_files(self, directory):
    import os
    return os.listdir(directory)

  def make_directory(self, directory_name):
    import os
    os.mkdir(directory_name)
    return f"Directory '{directory_name}' created."

  def remove_directory(self, directory_name):
    import shutil
    shutil.rmtree(directory_name)
    return f"Directory '{directory_name}' removed."

  def search_files(self, directory, filename_searched):
    import os

    matches = []

    for root, dirnames, filenames in os.walk(directory):
      for filename in filenames:
        if filename == filename_searched:
          matches.append(os.path.join(root, filename))

    return matches


jarisx = JarisX()
print(jarisx.current_date())
# print(jarisx.current_time())
# print(jarisx.day_of_week())
# print(jarisx.create_file("test.txt"))
# print(jarisx.write_to_file("test.txt", "Hello World!"))
# print(jarisx.read_file("test.txt"))
# print(jarisx.delete_file("test.txt"))
# print(jarisx.list_files("."))
# print(jarisx.make_directory("test_dir"))
# print(jarisx.remove_directory("test_dir"))
# print(jarisx.search_files(".", "test.txt"))


# Copyrigth@VedantSalaskar