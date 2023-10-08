import os
import subprocess
print("\n=====Using os.system=====")
""" Python has several modules to allow you to run Bash commands from Python. \
one of them is the  os.system() which is use to run the Bash command ls, and it will shows the directory contents.
"""
os.system("ls")
""" =====Using subprocess.run=====
You can use the subprocess module to spawn new processes, \
connect to input/output/error pipes, and obtain error codes. The subprocess.run() \
function can take many new arguments, but those additional arguments are optional."""

print("\n=====Using subprocess.run===== \n")
subprocess.run(["ls"])

#  Using subprocess.run with two arguments
""" In Python, the square brackets are list data types, which means that run() can take a list of arguments."""
print("\n=====Using subprocess.run with two arguments=====\n")
subprocess.run(["ls","-l"])
print("\n=====Using subprocess.run with three arguments=====\n")
#  call subprocess.run() with three arguments. The third argument will be a directory name.
subprocess.run(["ls","-l","README.md"])
print("\n=====Retrieving system information=====\n")
""" The subprocess.run() function is powerful because you can use it to run any Bash command.\
In this exercise, you will call the uname command to get system information."""
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
print("\n=====Retrieving information about disk space=====\n")
# To emphasize that subprocess.run() allows you to run any command, you will run the df command to get disk information.
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])