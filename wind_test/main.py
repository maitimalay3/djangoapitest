# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:58:16 2021

@author: mamh4s
"""

import datetime
import pandas as pd
import revenue.revenue as rev
import operationcost.costcalc as opex
import  financial.balancesheet as fin

#----------------------revenue Input------------------------------------
InstalledCapacity = 50
Turbines = 6
CapacityFactor = 0.36
Curtailment = 0.05
ppaprice = 41
PriceInflation = 0.02
start_year = 2021
years_of_operation = 50
receivable_period = 30

ppaprice = 45
#-----------------------------------------Cost Input------------
setupcost = 700000
baseoperationcost = 255000
CapexCost = 200000000
DpsYear = 50
payble_period = 30
#--------------------------Tax Input--------------------------------
tax_rate= 0.23
#------------------------------------------------------------------

revinputdata = {'InstalledCapacity':InstalledCapacity,'Turbines':Turbines,'CapacityFactor':CapacityFactor, 'PriceInflation':PriceInflation,'ppaprice':ppaprice, 'receivable_period' : receivable_period }
contractinfo = {'start_year':start_year, 'years_of_operation':years_of_operation}
costinput = {'setupcost':setupcost,'baseoperationcost':baseoperationcost, 'CapexCost':CapexCost, 'DpsYear':DpsYear, 'payble_period': payble_period}


RevObject = rev.turnover(revinputdata, contractinfo)
Revdf = RevObject.RevenueCal()

CostObject = opex.opexcost(costinput,contractinfo)
Costdf = CostObject.OpexCal()

#--------------------------Tax Input--------------------------------
unlcashflow = pd.merge(Revdf, Costdf , left_on="dates", right_on="dates")
print(unlcashflow)




