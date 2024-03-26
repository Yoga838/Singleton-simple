class CalculatorSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.result = 0  # Inisialisasi hasil perhitungan
        return cls._instance

    def add(self, value1):
        self.result += value1
        
    def reset(self):
        self.result = 0

    def subtract(self, value):
        self.result -= value

    def get_result(self):
        return self.result

# Contoh penggunaan

calculator = CalculatorSingleton()

calculator.add(5)
calculator.add(3)

print("Hasil penambahan:", calculator.get_result())  # Output: 8

calculator.subtract(4)
print("Hasil pengurangan:", calculator.get_result())  # Output: 4

# Membuat instance baru, namun tetap menggunakan instance yang sama
calculator2 = CalculatorSingleton()
print("Hasil pengurangan dengan instance baru:", calculator2.get_result())  # Output: 4
