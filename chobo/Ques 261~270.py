# 261번
class Stock():
    pass
    
# 262번
class Stock():
    def __init__(self, name, code):
        self.name = name
        self.code = code

samsumg = Stock('삼성전자', '005930')
print(samsumg.name)
print(samsumg.code)

# 263번
class Stock():
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def set_name(self, name):
        self.name = name
        
a = Stock(None, None)
a.set_name("삼성전자")
print(a.name)

# 264번
class Stock():
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
        
a = Stock(None, None)
a.set_code("005930")
print(a.code)
print()

# 265번
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code
    
samsumg = Stock('삼성전자', '005930')
print(samsumg.name)
print(samsumg.code)
print(samsumg.get_name())
print(samsumg.get_code(),'\n')


# 266번
class Stock():
    def __init__(self, name, code, PER, PBR, price):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.price = price

# 267번
samsung = Stock('삼성전자', '005930', 15.79, 1.33, 2.83)

# 268번
class Stock():
    def __init__(self, name, code, per, pbr, devidend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.devidend = devidend
        
    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code
        
    def set_per(self, per):
        self.per = per
        
    def set_pbr(self, pbr):
        self.pbr = pbr
        
    def set_devidend(self, devidend):
        self.devidend = devidend

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

# 269번
samsung = Stock('삼성전자', '005930', 15.79, 1.33, 2.83)
samsung.set_per(12.75)
print(samsung.per)

# 270번
a = []
samsung = Stock('삼성전자', '005930', 15.79, 1.33, 2.83)
hyundae = Stock('현대차', '005380', 8.70, 0.35, 4.47)
lg = Stock('LG전자', '066570', 317.34, 0.69, 1.37)

a.append(samsung)
a.append(hyundae)
a.append(lg)

for i in a:
    print(i.name, i.code, i.per)