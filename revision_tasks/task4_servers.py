servers = {
	"web1" : "226.71.116.227",
	"web2" : "172.63.105.33",
	"db1" : "227.143.180.118",
	"db2" : "208.156.62.179",
	"db3" : "237.249.189.7",
	"cache1" : "143.85.194.190"
}

print ("Server details:\n")
for name, ip in servers.items():
	print("Server : ",name ,"IP : ",ip)
