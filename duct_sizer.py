#!/usr/bin/env python3
"""Duct sizer: airflow + velocity -> round and rectangular duct sizes."""
import argparse, math

def sizes(cfm, fpm):
    area_ft2 = cfm / fpm
    area_in2 = area_ft2 * 144
    d = 2 * math.sqrt(area_in2 / math.pi)
    out = [f"Airflow {cfm:g} CFM at {fpm:g} FPM needs {area_in2:.1f} in2 of free area",
           f"Round duct: {d:.1f} in diameter (use the next standard size up)"]
    for w in (6, 8, 10, 12, 14, 16, 18, 20, 24):
        h = area_in2 / w
        de = 1.30 * (w * h) ** 0.625 / (w + h) ** 0.25
        out.append(f"Rectangular {w} in wide -> {h:.1f} in deep (equivalent diameter {de:.1f} in)")
    return "\n".join(out)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--cfm", type=float, required=True)
    p.add_argument("--fpm", type=float, default=1000)
    a = p.parse_args()
    print(sizes(a.cfm, a.fpm))

if __name__ == "__main__":
    main()
