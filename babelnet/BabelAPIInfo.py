#!/usr/bin/env python -*- coding: utf-8 -*-

"""
Information about the BabelNet API
"""

version = "2.5"
authors = "Roberto Navigli, Simone Ponzetto and Daniele Vannella";
contributors = "Francesco Cecconi";

def getHeader():
    return " ".join(["BabelNet API v", version, 
                     "written by", authors, 
                     "with additional contributions by", contributors])

def getPyHeader():
    return " ".join(["pybabel wrapper v", "o.1",
                    "written by", "@alvations"])