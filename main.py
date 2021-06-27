import os
from subprocess import call

from colorama import init, Fore

init(autoreset = True)

def err(string):
	print(Fore.RED + 'Error: ' + string)

def err_no_args(command):
	err(f'Command `{command}` can\'t have 0 arguments')

def interpret_command(cmd):
	cmd = cmd.split(' ')

	command = cmd[0]
	args = cmd
	del args[0] #~ Remove command from args

	if command == 'cd':
		if len(args) < 1:
			err_no_args('cd')

		else:
			try:
				os.chdir(args[0])
			except FileNotFoundError:
				err(f'File or directory, `{args[0]}`, not found!')

	elif command == 'del':
		if len(args) < 1:
			err_no_args('del')

		else:
			try:
				os.remove(args[0])
			except FileNotFoundError:
				err(f'File or directory, `{args[0]}`, not found!')
			except IsADirectoryError:
				os.rmdir(args[0])

	elif command == 'mkdir':
		try:
			os.mkdir(args[0])
		except FileExistsError:
			err(f'File or directory, `{args[0]}`, already exists!')

	elif command == 'touch':
		if os.path.exists(args[0]):
			err(f'File or directory, `{args[0]}`, already exists!')
		else:
			file = open(args[0], 'w')
			file.close()

	elif command == 'dir':
		print(os.listdir())

	elif command == 'echo':
		print(' '.join(args))

	else:
		call(' '.join(cmd))

while True:
	try:
		try:
			input_cmd = input(os.getcwd() + '> ')
			if input_cmd == 'quit':
				break
			interpret_command(input_cmd)

		except Exception as e:
			print(e)
		
	except KeyboardInterrupt:
		print('\n')
