# -*- coding: utf-8 -*-
"""
Created on Tue May  4 21:32:59 2021

@author: mamh4s
"""

import pandas as pd
import numpy as np

class opexcost:
     def __init__(self,costinput,contractinfo):
         self.setupcost = costinput['setupcost']
         self.baseoperationcost = costinput['baseoperationcost']
         self.CapexCost = costinput['CapexCost']
         self.DpsYear = costinput['DpsYear']
         self.payble_period = costinput['payble_period']
         
         self.start_year = contractinfo['start_year']
         self.years_of_operation = contractinfo['years_of_operation']
         
         
     def OpexCal(self):
         datelist = [*range(self.start_year, self.start_year + self.years_of_operation , 1)]
         OpexDf = pd.DataFrame({'dates': datelist})
         
         OpexDf['fixedcost'] = self.baseoperationcost 
         OpexDf['setupcost'] = OpexDf['dates'].apply(lambda x:self.setupcost if x == self.start_year else 0)
         OpexDf['dpscost'] = self.CapexCost/self.DpsYear
         OpexDf['totalcost'] = OpexDf['fixedcost'] + OpexDf['setupcost'] + OpexDf['dpscost'] 
         OpexDf['paybels']= OpexDf['totalcost']*self.payble_period/365
         OpexDf['Chgpaybels']= -1* OpexDf['paybels'].diff().fillna(0)
         
         
         return OpexDf
     
    
    
         

    