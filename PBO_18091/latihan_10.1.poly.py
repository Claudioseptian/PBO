class burung:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"saya seekor burung bernama {self.name}. dan umur {self.age}")

    def gerak_cepat(self):
        print("terbang")

class singa:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(f"saya seekor singa bernama {self.name}. dan umur {self.age}")

    def gerak_cepat(self):
        print("berlari")

burung1 = burung("leo", 2.5)
singa1 = singa("sipu", 4)

for animal in (burung1, singa1):
    animal.gerak_cepat()
    animal.info()
    animal.gerak_cepat()
