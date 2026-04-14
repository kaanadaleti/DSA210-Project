#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:08:54 2026

@author: kaanadaleti
"""

import pandas as pd
import matplotlib.pyplot as plt

# CSV oku
df = pd.read_csv("SydneyAmerican.csv")

# Time sütununu datetime yap
df['Time'] = pd.to_datetime(df['Time'])

# Plot
plt.figure(figsize=(12,6))

plt.plot(df['Time'], df['Sydney Sweeney'], label='Sydney Sweeney')
plt.plot(df['Time'], df['American Eagle'], label='American Eagle')

# Event window (sen May–Sept yaptın)
plt.axvline(pd.to_datetime("2025-05-01"), linestyle='--', color='green')
plt.axvline(pd.to_datetime("2025-08-31"), linestyle='--', color='red')

plt.title("Google Trends: Sydney Sweeney vs American Eagle")
plt.xlabel("Time")
plt.ylabel("Search Interest")
plt.legend()

plt.tight_layout()
plt.show()

start = "2025-05-01"
end = "2025-08-31"

before = df[df['Time'] < start]
during = df[(df['Time'] >= start) & (df['Time'] <= end)]

print("BEFORE MEAN")
print(before[['Sydney Sweeney','American Eagle']].mean())

print("\nDURING MEAN")
print(during[['Sydney Sweeney','American Eagle']].mean())