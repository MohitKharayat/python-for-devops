error_count=0
warning_count=0
file_path = 'dummy_server.log'

with open(file_path, 'r') as file:
	content = file.readlines()
	for line in content:
		if "ERROR" in line:
			error_count+=1
		elif "WARNING" in line:
			warning_count+=1

print("Errors = ", error_count, " Warnings = ",warning_count)	
