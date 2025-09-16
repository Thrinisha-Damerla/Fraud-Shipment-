import subprocess

scripts = [
    "DATA_PROCESSING..PY",
    "MODEL_TRAINING.PY",
    "blockchain.py",
    "APP.PY"
]

for script in scripts:
    print(f"\n--- Running {script} ---")
    subprocess.run(["python", script], check=True)
