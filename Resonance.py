#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:25:23 2021

@author: ai5924
"""
import matplotlib.pyplot as plt
from math import *
import numpy as np
from sympy.solvers import solve
from sympy import symbols
from sympy.abc import   beta, x



class Resonance:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    
    def compute(self):
        # computation
        solut=[]
        sol=[]
        for beta in np.linspace(self.a, self.b, self.c):
            sol=solve((1/(x*beta))**3-8*(1/(x*beta))**2+8*(3-2*(beta))*(1/(x*beta))-16*(1-(beta)),x)
            sol= [complex(item) for item in sol]
            solut.append(sol)

        # assign 
        #self.d = ...
        
        solut=np.array(solut)
        return solut
        
reson = Resonance(0.1,0.32,10)
print(reson.compute())
