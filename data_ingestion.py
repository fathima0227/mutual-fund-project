#!/usr/bin/env python3
import os
import glob
import pandas as pd


def summarize_file(path):
    print("=" * 80)
    print(f"File: {os.path.basename(path)}")
    try:
        df = pd.read_csv(path, low_memory=False)
    except Exception as e:
        print(f"ERROR reading file: {e}")
        return None

    print("Shape:", df.shape)
    print("Dtypes:")
    print(df.dtypes)
    print("Missing/Null counts:")
    missing = df.isna().sum()
    print(missing)
    print("Head:")
    try:
        print(df.head().to_string(index=False))
    except Exception:
        print(df.head())
    print()

    return {
        "file_name": os.path.basename(path),
        "row_count": df.shape[0],
        "column_count": df.shape[1],
        "missing_count": int(missing.sum()),
        "missing_by_column": "; ".join(
            [f"{col}:{count}" for col, count in missing.items() if count > 0]
        ),
    }


def main():
    base = os.path.join(os.path.dirname(__file__), "data", "raw")
    pattern = os.path.join(base, "*.csv")
    files = sorted(glob.glob(pattern))
    if not files:
        print(f"No CSV files found in {pattern}")
        return

    summaries = []
    for path in files:
        summary = summarize_file(path)
        if summary:
            summaries.append(summary)

    processed_dir = os.path.join(os.path.dirname(__file__), "data", "processed")
    os.makedirs(processed_dir, exist_ok=True)
    output_path = os.path.join(processed_dir, "ingestion_summary.csv")
    pd.DataFrame(summaries).to_csv(output_path, index=False)
    print("Saved ingestion summary to", output_path)


if __name__ == "__main__":
    main()
