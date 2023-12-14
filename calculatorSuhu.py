print("\n ==== CALCULATOR SUHU ==== \n")

#START CELSIUS
print("\n CELSIUS \n")

input_celsius = float(input("Masukkan Suhu(°C) :"))
print("Suhu anda adalah  ", input_celsius, "°C")

#to Reamur
reamur = (4 / 5) * input_celsius
print("Suhu anda adalah  ", reamur, "°R")

#to fahrenhaet
fahrenhaet = (9 / 5) * input_celsius + 32
print("Suhu anda adalah  ", fahrenhaet, "°F")

#to kelvin
kelvin = input_celsius + 273
print("Suhu anda adalah  ", kelvin, "°K")
#END CELSIUS

#START REAMUR
print("\n REAMUR \n")

input_reamur = float(input("Masukkan Suhu(°R) :"))

#to celsius
celsius = (5 / 4) * input_reamur
print("Suhu anda adalah ", celsius, "°C")

#to reamur
print("Suhu anda adalah ", input_reamur, "°R")

#to fahrenhaet
fahrenhaet = (9 / 4) * input_reamur + 32
print("Suhu anda adalah ", fahrenhaet, "°F")

#to kelvin
kelvin = (5 / 4) * input_reamur + 273
print("Suhu anda adalah ", kelvin, "°K")
#END REAMUR

#START FAHRENHAET
print("\n FAHRENHAET \n")

input_fahrenhaet = float(input("Masukkan Suhu(°F) :"))

#to celsius
celsius = (5 / 9) * (input_fahrenhaet - 32)
print("Suhu anda adalah ", celsius, "°C")

#to reamur
reamur = (4 / 9) * (input_fahrenhaet - 32)
print("Suhu anda adalah ", input_reamur, "°R")

#to fahrenhaet
print("Suhu anda adalah ", input_fahrenhaet, "°F")

#to kelvin
kelvin = celsius + 273
print("Suhu anda adalah ", kelvin, "°K")
#END FAHRENHAET

#START KELVIN
print("\n KELVIN \n")

input_kelvin = float(input("Masukkan Suhu(°K) :"))

#to celsius
celsius = input_kelvin - 273
print("Suhu anda adalah ", celsius, "°C")

#to reamur
reamur = (4 / 5) * celsius
print("Suhu anda adalah ", reamur, "°R")

#to fahrenhaet
fahrenhaet = (9 / 5) * celsius + 32
print("Suhu anda adalah ", fahrenhaet, "°F")

#to kelvin
print("Suhu anda adalah ", input_kelvin, "°K")
#END FAHRENHAET
