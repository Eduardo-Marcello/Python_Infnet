"""""Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de memória principal e quanto de 
memória de paginação (swap) existem no computador."""""
import psutil

swap_mem = psutil.swap_memory().total
main_mem = psutil.virtual_memory().total
print(f"Main memory: {round(main_mem / (1024 * 1024 * 1024), 2)} GB")
print(f"Swap memory: {round(swap_mem / (1024 * 1024 * 1024), 2)} GB")
