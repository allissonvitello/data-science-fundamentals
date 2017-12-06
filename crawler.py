# -*- coding: utf-8 -*-
"""
Created on Tue Dec 05 21:39:48 2017

@author: allisson

------Not finished yet.------
"""

url = "http://www4.tjrj.jus.br/consultaProcessoWebV2/consultaProc.do?v=2&FLAGNOME=&back=1&tipoConsulta=publica&numProcesso="

number_process = str(raw_input("Por gentileza, informe o número de processo que deseja capturar: "))

print(url[-1:]+number_process)