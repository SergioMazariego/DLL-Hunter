# DLL Hunter

DLL Hunter is a Python script that scans running processes on a Windows host and identifies instances of specific processes executing DLLs. It helps in the detection and analysis of potentially malicious or suspicious activities by monitoring processes commonly associated with DLL injection or other security-related concerns.

## Features

- Scans running processes and identifies instances of specific processes executing DLLs.
- Supports detection of the following processes: `rundll32.exe`, `regsvr32.exe`, `regsvcs.exe`, `regasm.exe`, `certoc.exe`, `dnscmd.exe`, `installutil.exe`, `mavinject32.exe`, `msiexec.exe`, `netsh.exe`, `pcalua.exe`, `rasautou.exe`, `register-cimprovider.exe`, `acccheckconsole.exe`, `coregen.exe`, `dotnet.exe`, `procdump.exe`, `tracker.exe`, `vsls-agent.exe`, and `wuauclt.exe`.
- Provides the process name, process ID (PID), and the DLL path for further investigation.
- Requires administrative privileges for accurate results.

## Prerequisites

- Python 3.x
- `psutil` library

## Installation

1. Clone or download this repository.

2. Install the required `psutil` library by running the following command: `pip install psutil`

## Usage

1. Open a command prompt or terminal.

2. Navigate to the project directory.

3. Run the script using the following command: `python dll_hunter.py`

4. The script will scan the running processes and display the processes with DLLs, including their names, PIDs, and DLL paths.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or improvements, please create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

The DLL Hunter script is provided for educational and informational purposes only. The author and contributors are not responsible for any misuse or damage caused by this script. Use it at your own risk.

## References

- [Hunting Lazarus Group’s TTPs](https://montysecurity.medium.com/hunting-lazarus-groups-ttps-925c17469077)