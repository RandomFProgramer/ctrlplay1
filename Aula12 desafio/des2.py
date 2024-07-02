# # conversor de segundos para minutos e horas
# class horario ():
#     def __init__(self, segundos, minutos, horas) :
#         self.segundos = segundos
#         self.minutos = minutos
#         self.horas = horas

s = float(input())
# segundosRestantes = s%60
minutosRestantes = s/60
horasRestantes = minutosRestantes/60

print(horasRestantes, ":", minutosRestantes, ":", s%60)