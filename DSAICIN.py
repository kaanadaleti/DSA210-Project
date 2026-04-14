#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 12:39:15 2026

@author: kaanadaleti
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data:adidas_kanye_yeezy_trends.csv")


df['Time'] = pd.to_datetime(df['Time'])

# Grafik için
plt.figure(figsize=(12,6))

plt.plot(df['Time'], df['Kanye West'], label='Kanye West')
plt.plot(df['Time'], df['ADIDAS'], label='ADIDAS')
plt.plot(df['Time'], df['Yeezy'], label='Yeezy')

# Event line düzxenlmesi
plt.axvline(pd.to_datetime("2022-10-25"), linestyle='--', color='red')

plt.title("Google Trends: ADIDAS vs Kanye West vs Yeezy")
plt.xlabel("Time")
plt.ylabel("Search Interest")
plt.legend()

plt.tight_layout()
plt.show()

event_date = "2022-10-25"

before = df[df['Time'] < event_date]
after = df[df['Time'] >= event_date]

print("BEFORE means:")
print(before[['Kanye West','ADIDAS','Yeezy']].mean())

print("\nAFTER means:")
print(after[['Kanye West','ADIDAS','Yeezy']].mean())