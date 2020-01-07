import psutil

Name = 'mycroft'
processes = []
for proc in psutil.process_iter():
    try:
        pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline'])
        cmd = ' '.join(pinfo['cmdline'])
        if Name in cmd:
            print(cmd)
            processes.append(pinfo['pid'])
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
if not processes:
    print("false ....")
else:
    print("true...." + str(processes))
    