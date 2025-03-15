#! /usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Filename: main.py
Author: Delsan Anthony Soliva
Created: 2025-03-15
Version: v0.1.0
Description: A hello world API
'''

from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def home():
    return {'message': 'Hello World'}

@app.get('/items')
async def items():
    items = ['bags','shoes','shirts']
    return {'items': items}