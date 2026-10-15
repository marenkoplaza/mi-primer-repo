import platform
import subprocess

sistema = platform.system()

if sistema == "Windows":
    subprocess.Popen(["start", "excel"], shell=True)
elif sistema == "Darwin":  # Mac
    subprocess.run(["open", "-a", "Microsoft Excel"])
else:
    print("Este sistema no está configurado en el ejemplo.")
