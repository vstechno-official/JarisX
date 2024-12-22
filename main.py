import cmd
import sys
import os
import datetime
import shutil
import math
import json
import colorama
from colorama import Fore, Style
import platform
import psutil
import re
from tabulate import tabulate
import random
import hashlib
import base64
import zipfile

# Use the JarisX class from the uploaded main.py
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
        return datetime.date.today()

    def current_time(self):
        return datetime.datetime.now().time()

    def day_of_week(self):
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
        os.remove(filename)
        return f"File '{filename}' deleted."

    def list_files(self, directory):
        return os.listdir(directory)

    def make_directory(self, directory_name):
        os.mkdir(directory_name)
        return f"Directory '{directory_name}' created."

    def remove_directory(self, directory_name):
        shutil.rmtree(directory_name)
        return f"Directory '{directory_name}' removed."

    def search_files(self, directory, filename_searched):
        matches = []
        for root, dirnames, filenames in os.walk(directory):
            for filename in filenames:
                if filename == filename_searched:
                    matches.append(os.path.join(root, filename))
        return matches

class JarisXCLI(cmd.Cmd):
    intro = f"""{Fore.CYAN}
    ╔════════════════════════════════════════╗
    ║             Welcome to JarisX          ║
    ║      Type 'assist' for quick help      ║
    ║      Type 'exit' to quit              ║
    ╚════════════════════════════════════════╝
    {Style.RESET_ALL}"""

    prompt = f'{Fore.GREEN}JarisX> {Style.RESET_ALL}'

    def __init__(self):
        super().__init__()
        self.jarisx = JarisX()
        self.notes = []
        self.todos = []
        self.settings = self.load_settings()

    def load_settings(self):
        try:
            with open('jarisx_settings.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                'theme': 'default', 
                'debug_mode': False,
                'max_notes': 10,
                'max_todos': 20
            }

    def save_settings(self):
        with open('jarisx_settings.json', 'w') as f:
            json.dump(self.settings, f, indent=4)

    def do_assist(self, arg):
        """Show comprehensive help and usage examples"""
        help_sections = [
            ['Mathematical Operations', 
             '- add(a, b): Add two numbers\n'
             '- subtract(a, b): Subtract two numbers\n'
             '- multiply(a, b): Multiply two numbers\n'
             '- divide(a, b): Divide two numbers\n'
             '- power(a, b): Raise a to power b\n'
             '- square_root(a): Calculate square root\n'
             '- factorial(n): Calculate factorial\n'
             '- fibonacci(n): Generate Fibonacci sequence'],

            ['String Operations', 
             '- palindrome_check(word): Check if word is palindrome\n'
             '- reverse_string(text): Reverse a string\n'
             '- length_of_string(text): Get string length\n'
             '- convert_to_uppercase(text): Convert to uppercase'],

            ['File Operations', 
             '- create_file(filename): Create a new file\n'
             '- write_to_file(filename, content): Write to file\n'
             '- read_file(filename): Read file contents\n'
             '- delete_file(filename): Delete a file\n'
             '- list_files(directory): List files in directory\n'
             '- search_files(directory, filename): Search for files'],

            ['Date and Time', 
             '- current_date(): Get current date\n'
             '- current_time(): Get current time\n'
             '- day_of_week(): Get current day']
        ]

        print(f"\n{Fore.CYAN}JarisX Comprehensive Help:{Style.RESET_ALL}")
        for section, examples in help_sections:
            print(f"\n{Fore.YELLOW}{section}:{Style.RESET_ALL}")
            print(examples)

    def do_math(self, arg):
        """Perform mathematical operations"""
        args = arg.split()
        if len(args) < 3:
            print(f"{Fore.RED}Usage: math [operation] [num1] [num2]{Style.RESET_ALL}")
            return

        operation = args[0].lower()
        try:
            if operation == 'sqrt':
                result = self.jarisx.square_root(float(args[1]))
            elif operation == 'factorial':
                result = self.jarisx.factorial(int(args[1]))
            elif operation == 'fibonacci':
                result = self.jarisx.fibonacci(int(args[1]))
            elif operation == 'prime':
                result = self.jarisx.prime_check(int(args[1]))
            else:
                num1, num2 = float(args[1]), float(args[2])
                if operation == 'add':
                    result = self.jarisx.add(num1, num2)
                elif operation == 'subtract':
                    result = self.jarisx.subtract(num1, num2)
                elif operation == 'multiply':
                    result = self.jarisx.multiply(num1, num2)
                elif operation == 'divide':
                    result = self.jarisx.divide(num1, num2)
                elif operation == 'power':
                    result = self.jarisx.power(num1, num2)
                else:
                    print(f"{Fore.RED}Unknown operation{Style.RESET_ALL}")
                    return

            print(f"{Fore.CYAN}Result: {result}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

    def do_string(self, arg):
        """Perform string operations"""
        args = arg.split(maxsplit=1)
        if len(args) < 2:
            print(f"{Fore.RED}Usage: string [operation] [text]{Style.RESET_ALL}")
            return

        operation = args[0].lower()
        text = args[1]

        try:
            if operation == 'reverse':
                result = self.jarisx.reverse_string(text)
            elif operation == 'length':
                result = self.jarisx.length_of_string(text)
            elif operation == 'upper':
                result = self.jarisx.convert_to_uppercase(text)
            elif operation == 'palindrome':
                result = "Palindrome" if self.jarisx.palindrome_check(text) else "Not Palindrome"
            else:
                print(f"{Fore.RED}Unknown operation{Style.RESET_ALL}")
                return

            print(f"{Fore.CYAN}Result: {result}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

    def do_file(self, arg):
        """Perform file operations"""
        args = arg.split(maxsplit=2)
        if not args:
            print(f"{Fore.RED}Usage: file [operation] [filename] [content]{Style.RESET_ALL}")
            return

        operation = args[0].lower()
        try:
            if operation == 'list':
                directory = args[1] if len(args) > 1 else '.'
                files = self.jarisx.list_files(directory)
                print(tabulate([[f] for f in files], headers=['Files'], tablefmt='grid'))
            elif operation == 'search':
                if len(args) < 2:
                    print(f"{Fore.RED}Please specify filename to search{Style.RESET_ALL}")
                    return
                directory = '.'
                filename = args[1]
                matches = self.jarisx.search_files(directory, filename)
                if matches:
                    print(tabulate([[m] for m in matches], headers=['Matches'], tablefmt='grid'))
                else:
                    print(f"{Fore.YELLOW}No matches found{Style.RESET_ALL}")
            elif len(args) < 2:
                print(f"{Fore.RED}Please specify filename{Style.RESET_ALL}")
            else:
                filename = args[1]
                if operation == 'create':
                    result = self.jarisx.create_file(filename)
                elif operation == 'write':
                    content = args[2] if len(args) > 2 else ''
                    result = self.jarisx.write_to_file(filename, content)
                elif operation == 'read':
                    result = self.jarisx.read_file(filename)
                elif operation == 'delete':
                    result = self.jarisx.delete_file(filename)
                else:
                    print(f"{Fore.RED}Unknown operation{Style.RESET_ALL}")
                    return
                print(f"{Fore.CYAN}{result}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

    def do_exit(self, arg):
        """Exit JarisX"""
        print(f"{Fore.YELLOW}Goodbye! Have a great day!{Style.RESET_ALL}")
        return True

def main():
    try:
        colorama.init(autoreset=True)
        JarisXCLI().cmdloop()
    except KeyboardInterrupt:
        print("\nExiting JarisX...")
        sys.exit(0)

if __name__ == '__main__':
    main()
