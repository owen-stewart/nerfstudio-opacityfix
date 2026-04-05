"""
inject_fix.py
Copies splatfacto_edited.py over the nerfstudio installed version.
Run this after pip install nerfstudio.

Usage:
    python3 code/inject_fix.py
"""

import subprocess, sys, shutil, os

# Find where nerfstudio installed splatfacto.py
result = subprocess.run(
    [sys.executable, "-c",
     "import nerfstudio, os; print(os.path.join(os.path.dirname(nerfstudio.__file__), 'models', 'splatfacto.py'))"],
    capture_output=True, text=True
)

target = result.stdout.strip()
source = os.path.join(os.path.dirname(os.path.abspath(__file__)), "splatfacto_edited.py")

print(f"Nerfstudio splatfacto: {target}")
print(f"Our edited version:    {source}")

# Check already patched
if "SPHERE GLASS FIX START" in open(target).read():
    print("Already patched!")
    sys.exit(0)

# Backup original
backup = target.replace("splatfacto.py", "splatfacto_original.py")
shutil.copy2(target, backup)
print(f"Backup saved: {backup}")

# Replace with our version
shutil.copy2(source, target)
print("SUCCESS — fix applied!")
