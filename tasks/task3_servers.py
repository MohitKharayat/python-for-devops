servers = ["web1","web2","web3","db1","db2","cache1"]

for server in servers:
	if "db" in server:
		print("Database found: ",server)
	else:
		print("Normal server :",server)
