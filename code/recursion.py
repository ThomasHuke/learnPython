#!/usr/bin/env Python3
# -*- coding: utf-8 -*-

def file(n):
    if n == 1:
        return 1
    return file(n - 1) * n

print(file(100))

#9332621544394415268169923885626670049071596826438162146859296389521759999322991560# 8941463976156518286253697920827223758251185210916864000000000000000000000000
