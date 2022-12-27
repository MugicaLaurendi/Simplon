import os
l = ["ab", "df"]
os.system(f"echo {l}")

a = input("project name :")
os.system(f"echo {a}")

os.system(f"mkdir {a}")
os.system(f"mkdir {a}/scripts")
os.system(f"touch {a}/bob.py")
