import subprocess

with open('output.txt','w') as f_obj:
    command = subprocess.run("ag --numbers ola test.txt", stdout=f_obj, shell=True)
    a = command.stdout
    print(a)
