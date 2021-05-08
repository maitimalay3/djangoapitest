# -*- coding: utf-8 -*-
"""
Created on Wed May  5 14:04:15 2021

@author: mamh4s
"""
import revenue.revenue as rev
import operationcost.costcalc as opex

class wrkcapital(rev.turnover):
    def __init__(self,revinputdata, contractinfo):
        super().__init__(revinputdata, contractinfo)
