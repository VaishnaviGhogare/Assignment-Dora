# Assignment-Dora
# PoCRA Mini Simulator for Point-wise Daily Soil Water Balance

This project simulates a daily soil water balance at an imaginary location based on rainfall data, soil type, and crop uptake characteristics. It's designed as part of the PoCRA assignment to model water distribution across various processes like runoff, infiltration, soil moisture, crop uptake, and groundwater recharge.

---

## Objective

The simulator processes daily rainfall data from **June 1 to October 10, 2022** and computes:

- Daily **runoff**
- **Excess runoff**
- **Soil moisture**
- **Crop uptake**
- **Groundwater recharge**

Based on the **soil type** input: `"deep"` or `"shallow"`.

---


## Soil Types

| Type     | Moisture Holding Capacity (C) | Groundwater Fraction (γ) |
|----------|-------------------------------|---------------------------|
| Deep     | 100 mm                        | 0.2                       |
| Shallow  | 42 mm                         | 0.4                       |

---

## Water Balance Formula

For each day `n`:

rain(n) = Δsm(n) + runoff(n) + excess(n) + uptake(n) + gw(n)



Where:

- `Δsm(n) = sm(n) - sm(n-1)`
- `uptake(n)` = min(4mm, sm(n-1))
- `runoff(n)` based on α depending on rain(n)
- `gw(n)` = γ × sm(n)
- `excess(n)` = max(0, infiltration + sm(n-1) - C)

---

##  How to Run

1.Ensure you have Python 3.10+ and `pandas` installed:
   pip install pandas

2.Download the rainfall CSV:
Place it in the same folder as dora.py.

3.Run the simulator with your desired soil type:
python dora.py

4.Enter soil type ('deep' or 'shallow'):
Check the output CSV in the output/ folder.

5.Output Format
Day	Rainfall (mm)	Runoff + Excess (mm)	Crop Uptake (mm)	Soil Moisture (mm)	Groundwater Recharge (mm)
01/06/22	13.4	2.68	4.0	38.6	7.72
...	...	...	...	...	...


Result Analysis
The simulator follows mass conservation — ensuring that rainfall input equals the total of all outflows and storage changes.

-Deep Soil retains more moisture, leading to lower runoff and higher crop uptake, which is ideal for sustainable agriculture.
-Shallow Soil shows higher runoff and groundwater loss, indicating reduced crop availability and lower efficiency.

Demo Video:
Watch at: [https://drive.google.com/file/d/1JWzvIHJus_0flLn1mo3164eErgxlAdHu/view?usp=drive_link]


Author:
Vaishnavi Ghogare
B.Tech CSE | IIT Bombay Internship | PoCRA Assignment
ghogarevaishnavi8@gmil.com

