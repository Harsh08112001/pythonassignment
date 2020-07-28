dict = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}
print(dict)

dict = {value:key for key, value in dict.items()}
print(dict)