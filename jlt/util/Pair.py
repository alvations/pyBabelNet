#!/usr/bin/env python -*- coding: utf-8 -*-

import md5

class Pair:
    serialVersionUID = 4496923633090911746L
    def __init__(self, f, s):
        self.f = f
        self.s = s
    
    # Java-like functions similar to the BabelNetAPI v2.5
    def getFirst(self):
        return self.f
    
    def getSecond(self):
        return self.s
    
    def toString(self):
        return "(" + this.first + "," + this.second + ")"
    
    def hashCode(self):    
        hashFirst = 0 if self.f else self.f.__hash__()
        hashSecond = 0 if self.f else self.s.__hash__()
        return (hashFirst + hashSecond) * hashSecond + hashFirst
    
    def reverse(self):
        return Pair(self.s, self.f)
    
    def equals(self, other):
        if isinstance(Pair, other):
            first_is_same_object = self.f is other.f
            second_is_same_object = self.s is other.s 
            
            first_is_same_value = self.f == other.f 
            second_is_same_value = self.s == other.s
            
            no_none_value = None not in [self.f, other.f, self.s, other.s]
            
            same_value = no_none_value and second_is_same_value and first_is_same_value
            same_object = first_is_same_object and second_is_same_object
        
            return same_value or same_object
        else:
            return False
        
    # Pythonic duck functions.
    def __str__(self):
        return self.toString 

