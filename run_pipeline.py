"""
Bluestock Fintech — Mutual Fund Analytics Pipeline
Run all scripts in order
"""

import subprocess
import sys

scripts = [
    "scripts/var_cvar.py",
    "scripts/rolling_sharpe.py", 
    "scripts/cohort_analysis.py",
    "scripts/sip_continuity.py",
    "scripts/recommender.py",
    "scripts/sector_hhi.py",
]

print("🚀 Starting Bluestock MF Analytics Pipeline...")
print("="*50)

for script in scripts:
    print(f"\n▶ Running {script}...")
    result = subprocess.run([sys.executable, script])
    if result.returncode == 0:
        print(f"✅ {script} done!")
    else:
        print(f"❌ {script} failed!")

print("="*50)
print("🏆 Pipeline Complete!")