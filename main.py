class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def info(self):
        print(f"Ism: {self.ism}, Yosh: {self.yosh}")

class ITTalaba(Talaba):
    def __init__(self, ism, yosh, til):
        super().__init__(ism, yosh)
        self.til = til

    def info(self):
        super().info()
        print(f"Dasturlash tili: {self.til}")

t = ITTalaba("Ali", 20, "Python")
t.info()
