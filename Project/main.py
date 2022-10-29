from opening_menu import *
import subprocess
import sys
from sql_username_password import *

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

with open('requirements.txt') as file:
    for line in file.readlines():
        install(line)
def run(runfile):
    with open(runfile, "r") as rnf:
        exec(rnf.read())

run("create_stats_file.py")

def get_sql_creds():
    sql_credentials()


if __name__ == "__main__":
    opening_menu()
