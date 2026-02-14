# sys module import kar rahe hain taaki command line arguments use kar saken
import sys 

# Ye function given log file ko analyze karega
def analyze_log(file_path):

	# ERROR aur WARNING lines count karne ke liye counters
	error_count = 0
	warning_count = 0

	try:
		# File ko read mode me open kar rahe hain
                # "with open" use karne se file automatically close ho jati hai
		with open(file_path, "r") as file:
			# File ko line-by-line read kar rahe hain
                        # Ye memory efficient hota hai (large log files ke liye best)
			for line in file:

				# Line ko lowercase me convert kar rahe hain
                                # Taaki ERROR, error, Error sab detect ho jaye 
				line = line.lower()
				# Agar line me "error" hai to error counter badhao
				if "error" in line:
					error_count += 1
				# Agar line me "warning" hai to warning counter badhao
				if "warning" in line:
					warning_count += 1
		# Final result print kar rahe hain using f-string (modern Python style)
		print(f"Errors = {error_count}")
		print(f"Warnings = {warning_count}")
        # Agar file exist nahi karti to ye exception handle hoga
	except FileNotFoundError:
		print("File not found check file name!")

# ---- Script execution yahan se start hoti hai ----

# Check kar rahe hain ki user ne command line se file name diya hai ya nahi
if len(sys.argv)<2:
	# Agar file name nahi diya to correct usage print karo
	print("To run the script : python3 optimized_log_analyzer.py <logfile>")
else:
	# Agar file name diya hai to analyze_log function call karo
	analyze_log(sys.argv[1])
        
