#tuple - defined by ()- not operations like append, remove etc.
tpl=(40,50,40,"XYZ")
print(tpl)
print(tpl[3])
print(tpl*3)
print(tpl.count(40))
print(tpl.index("XYZ"))

#list - defined by []
#convert list to tuple
lst=[67,34,"XYZ"]
print(type(lst))
tpl1=tuple(lst)
print(type(tpl1))
print(tpl1)