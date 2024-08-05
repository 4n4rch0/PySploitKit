import platform
import psutil
from prettytable import PrettyTable

def gather_local_host_info():
    table = PrettyTable(["Attribute", "Value"])

    table.add_row(["System", platform.system()])
    table.add_row(["Node Name", platform.node()])
    table.add_row(["Release", platform.release()])
    table.add_row(["Processor", platform.processor()])
    table.add_row(["CPU Count", psutil.cpu_count(logical=False)])
    table.add_row(["Memory (GB)", round(psutil.virtual_memory().total / (1024**3), 2)])
    table.add_row(["Disk Usage (GB)", round(psutil.disk_usage('/').total / (1024**3), 2)])

    print(table)