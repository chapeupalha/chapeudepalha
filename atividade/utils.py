from datetime import date
import random


def generate_protocolo():
    num_data = date.today()
    protocolo_data = str(num_data.year)+str(num_data.month).rjust(2, '0')+str(num_data.day).rjust(2, '0')
    num_protocolo_start = random.randint(100000, 999999)
    num_protocolo_end = random.randint(1000, 9999)

    protocolo_gerado = str(protocolo_data)+'.'+str(num_protocolo_start)+'.'+str(num_protocolo_end)

    return protocolo_gerado