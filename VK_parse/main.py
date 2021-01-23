from config import *


print("===========================================")
print("              Start VK parse               ")
print("===========================================")
print("")

print("- - - - - - - - - - - - - - - - - - - - - -")
print("              configurations               ")
print("- - - - - - - - - - - - - - - - - - - - - -")
print("")

print("scanner parameters")
print(f"  | start:  {conf_sc_start}")
print(f"  | amount: {conf_sc_amount}")
print("")

print("data parameters")
print(f"  | use log:  {conf_fn_log}")
print(f"  | use file: {conf_fn_file}")
print(f"  | use db:   {conf_fn_db}")
print("")

if conf_fn_file:
	print("file parameters")
	print(f"  | file dir:     {conf_fl_dir}")
	print(f"  | file group:   {conf_fl_group}")
	print(f"  | file format:  {conf_fl_format}")
	print("")

if conf_fn_db:
	print("database parameters")
	print(f"  | db type:  {conf_db_type}")
	print(f"  | db host:  {conf_db_host}")
	print(f"  | db user:  {conf_db_user}")
	print(f"  | db pass:  {conf_db_pass}")
	print(f"  | db name:  {conf_db_database}")
	print("")

if conf_check:
	answer = input("Config is correct? ( y/n ): ")

	if ( answer.lower() == "y" ):
		print()
	elif ( answer.lower() == "n" ):
		exit(0)
	else:
		print("error: false input")
		exit(-1)

print("===========================================")
print("              Work VK parse                ")
print("===========================================")
print("")
