# -*- coding: utf-8 -*-
"""
Created on Tue May  4 18:51:38 2021

@author: mamh4s
"""

import pandas as pd
import numpy as np
class turnover:
     def __init__(self,rev_input_dict,contractinfo):
         self.InstalledCapacity = rev_input_dict['InstalledCapacity']
         self.Turbines = rev_input_dict['Turbines']
         self.CapacityFactor =  rev_input_dict['CapacityFactor']
         self.ppaprice = rev_input_dict['ppaprice']
         self.PriceInflation = rev_input_dict['PriceInflation']
         self.receivable_period = rev_input_dict['receivable_period']
         self.start_year = contractinfo['start_year']
         self.years_of_operation = contractinfo['years_of_operation']
         
         
         
     def RevenueCal(self):
         EnergyGeneration = self.InstalledCapacity*self.CapacityFactor*self.Turbines*24*365
         datelist = [*range(self.start_year, self.start_year + self.years_of_operation , 1)]
         DateDf = pd.DataFrame({'dates': datelist})
         DateDf['EnergyGeneration'] = EnergyGeneration
         DateDf['NfYear'] = DateDf['dates'].apply(lambda x:x-self.start_year )
         DateDf['InflationFactor'] = (1+self.PriceInflation)**DateDf['NfYear']
         DateDf['Revenue'] = self.ppaprice * DateDf['InflationFactor'] * DateDf['EnergyGeneration']
         DateDf['Receivables']= DateDf['Revenue']*self.receivable_period/365
         DateDf['ChgReceivables']= -1* DateDf['Receivables'].diff().fillna(0)
         
         return DateDf
         
         
         
