#Basic Server manager mini project
servers = {
	"web1" : "195.70.58.51",
	"web2" : "88.116.173.6",
	"web3" : "244.47.153.49",
	"db1" : "65.123.182.180",
	"db2" : "101.16.60.148",
	"cache1" : "121.13.25.128"
}

print("=== Server Manager ===\n")
name = input("Enter Server name to search : ")

#Check if server is present
if name in servers:
	ip = servers[name]
	print("Server found!")
	print("Name : ",name)
	print("IP : ", ip)

	#Check server type
	if "db" in name:
		print("Type => Database Server.")
	elif "web" in name :
		print("Type => Web Server.")
	elif "cache" in name:
		print("Type => Cache Server.")
else:
	print("Server Not Found!")

#Print all the servers and their IP
for s , ip in servers.items():
	print("Name : ",s,"IP : ",ip) 
