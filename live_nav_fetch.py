#!/usr/bin/env python3
import csv
import os
import time
import requests

SCHEMES = [
    {"scheme_name": "HDFC Top 100", "amfi_code": "125497"},
    {"scheme_name": "SBI Bluechip", "amfi_code": "119551"},
    {"scheme_name": "ICICI Bluechip", "amfi_code": "120503"},
    {"scheme_name": "Nippon Large Cap", "amfi_code": "118632"},
    {"scheme_name": "Axis Bluechip", "amfi_code": "119092"},
    {"scheme_name": "Kotak Bluechip", "amfi_code": "120841"},
]

API_URL = "https://api.mfapi.in/mf/{}"
MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 3


def fetch_nav(amfi_code):
    last_exception = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(API_URL.format(amfi_code), timeout=20)
            response.raise_for_status()
            data = response.json()
            if "data" not in data or not data["data"]:
                raise ValueError(f"No NAV data returned for AMFI code {amfi_code}")
            latest = data["data"][0]
            return {
                "amfi_code": amfi_code,
                "scheme_name": data.get("meta", {}).get("scheme_name", ""),
                "date": latest.get("date", ""),
                "nav": latest.get("nav", ""),
            }
        except Exception as exc:
            last_exception = exc
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY_SECONDS)
            else:
                raise
    raise last_exception


def main():
    output_dir = os.path.join(os.path.dirname(__file__), "data", "raw")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "live_nav.csv")

    rows = []
    for scheme in SCHEMES:
        try:
            row = fetch_nav(scheme["amfi_code"])
            # Use the provided scheme name as a stable label when API returns a name.
            row["scheme_name"] = scheme["scheme_name"]
            rows.append(row)
            print(f"Fetched {scheme['scheme_name']} ({scheme['amfi_code']}) -> {row['date']} {row['nav']}")
        except Exception as exc:
            print(f"ERROR fetching {scheme['scheme_name']} ({scheme['amfi_code']}): {exc}")

    if not rows:
        print("No NAV data fetched. Exiting without writing file.")
        return

    fieldnames = ["scheme_name", "amfi_code", "date", "nav"]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved live NAV data to {output_path}")


if __name__ == "__main__":
    main()
