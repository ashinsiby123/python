d={'a':20,'d':15,'c':5}
print("Orginal dictionary", d)

#ascending order
sd = sorted(d.items(), key=lambda x:x[0],)
csd=dict(sd)
print("Dictionary in ascending order : ",csd)
print(type(csd))

#descending order
sd = sorted(d.items(), key=lambda x:x[0], reverse=True)
csd=dict(sd)
print("Dictionary in descending order : ",csd)
print(type(csd))
