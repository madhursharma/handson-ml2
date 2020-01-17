# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 00:27:30 2020

@author: ms_sh
"""

def func_kwargs(pos1, first, second, third):
    print(second, first, third, pos1)

def func_order_args(*args):
    for i in args:
        print (i)
        

        
func_order_args(1, 'test', 3)

val = {'first':1, 'third':2, 'second':3}
func_kwargs(11, **val)
