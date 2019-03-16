# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:33:10 2018

@author: Ben
"""

import numpy

WAR0=5.2
ExpiryYears=3
Age0=28
OptionValue=32.8
TenorYears=5
FrontYearCost=32
OptionlessWAR=0.0
OptionlessSalary=0.0
SumWAR=0.0
SalaryPaid=0.0
DidHeOptOut=0
LeaveWAR=0.0
StayWAR=0.0
DeclineYears=0.0

for i in range (1000000):
    WARCount=WAR0
    YearCount=0
    SumWARIter=0.0
    AgeCount=Age0
    WinCost=8
    SalaryPaid+=ExpiryYears*FrontYearCost
    while YearCount < ExpiryYears:
        SumWARIter+=WARCount
        OptionlessWAR+=WARCount
        SkillChange=numpy.random.normal()*1.4
        WARCount+=SkillChange
        AgeCount+=1
        YearCount+=1
        if AgeCount>29:
            WARCount-=.5
        CostChange=numpy.random.normal()*.8+0.25
        WinCost+=CostChange
        
    AgeFinal=AgeCount+TenorYears-1
    DeclineYears=(max(AgeFinal,29)-max(AgeCount,29))
    AgePenalty = DeclineYears*(DeclineYears+1)/4
    OptionlessWAR+=WARCount*TenorYears-AgePenalty
    OptionlessSalary+=ExpiryYears*FrontYearCost+TenorYears*OptionValue
    if WARCount*WinCost*TenorYears-AgePenalty*WinCost<OptionValue*TenorYears:
        SumWAR+=SumWARIter+WARCount*TenorYears-AgePenalty
        SalaryPaid+=TenorYears*OptionValue
        StayWAR+=SumWARIter+WARCount*TenorYears-AgePenalty
    else:
        DidHeOptOut+=1
        SumWAR+=SumWARIter
        LeaveWAR+=SumWARIter
        


print ("Odds of opt out are "+ str(DidHeOptOut/1000000))
print ("Dollars per win were "+ str(round(SalaryPaid/SumWAR,2)))
print ("Dollars per win without option would have been "+str(round(OptionlessSalary/OptionlessWAR,2)))
print ("Optionless Salary= "+str(OptionlessSalary))
print ("Optionless WAR= "+str(OptionlessWAR))
print ("WAR when opting out is "+str(round(LeaveWAR/DidHeOptOut,2)))
print ("Dollars per win when opting out are "+str(round(FrontYearCost*ExpiryYears/(LeaveWAR/DidHeOptOut),2)))
print ("WAR when staying is "+str(round(StayWAR/(1000000-DidHeOptOut),2)))
print ("Dollars per win when staying are "+str(round((FrontYearCost*ExpiryYears+TenorYears*OptionValue)/(StayWAR/(1000000-DidHeOptOut)),2)))