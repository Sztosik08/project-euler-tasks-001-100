# Problem 19 — Counting Sundays

You are given the following information, but you may be able to figure it out yourself:

- 1 Jan 1900 was a Monday.
- Thirty days has September, April, June and November. All the rest have thirty-one, saving February alone, which has twenty-eight, rain or shine. And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

## Notes

![alt text](<Zrzut ekranu 2026-07-14 o 11.55.06.png>)

0: Saturday ; 1 = Sunday, 2 = Monday; etc.

h - day of the week; q - day of the month

m - month; K - year of the century; J - zero based century (eg. 19 for 1995)


January and February are treated as the 13th and 14th month each year

## Result

```
171
```
