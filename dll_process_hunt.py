import psutil
import sys

def get_processes_with_dlls(process_names):
    processes_with_dlls = []

    for proc in psutil.process_iter(['name', 'pid', 'cmdline']):
        try:
            if proc.name() in process_names:
                cmdline = proc.cmdline()
                if len(cmdline) > 1:
                    args = ' '.join(cmdline[1:])
                    processes_with_dlls.append((proc.name(), proc.pid, args))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return processes_with_dlls

def main():
    process_names = [
        'rundll32.exe', 'regsvr32.exe', 'regsvcs.exe', 'regasm.exe',
        'certoc.exe', 'dnscmd.exe', 'installutil.exe', 'mavinject32.exe',
        'msiexec.exe', 'netsh.exe', 'pcalua.exe', 'rasautou.exe',
        'register-cimprovider.exe', 'acccheckconsole.exe', 'coregen.exe',
        'dotnet.exe', 'procdump.exe', 'tracker.exe', 'vsls-agent.exe',
        'wuauclt.exe'
    ]

    processes_with_dlls = get_processes_with_dlls(process_names)

    if len(processes_with_dlls) > 0:
        print("Processes with DLLs:")
        for process in processes_with_dlls:
            print(f"Name: {process[0]}\tPID: {process[1]}\tCommand Line Arguments: {process[2]}")
    else:
        print("No processes with DLLs found.")

if __name__ == '__main__':
    main()
