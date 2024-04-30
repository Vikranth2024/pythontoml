import tomllib
f1=open("dets.toml","rb")
data=tomllib.load(f1)
print(data["age"])
