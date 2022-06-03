from re import sub
import subprocess

# Method-1 (Older approach)
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen

# Method-2 (Better approach)
# Run the program from Git Bash
try:
    completed = subprocess.run(["python", "other.py"],
                               capture_output=True, text=True, check=True)

    # This will return a 'subprocess.CompletedProcess' object
    # print(type(completed))

    print("args:", completed.args)
    print("returncode (0 = success):", completed.returncode)
    print("stderr:", completed.stderr)
    print("stdout:", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)
