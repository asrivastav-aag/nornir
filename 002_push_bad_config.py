from nornir import InitNornir
from nornir_scrapli.tasks import send_configs_from_file
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file = "config.yaml")

def random_configs(task):
    task.run(task = send_configs_from_file, file = "002_bad_config.txt")

results = nr.run(task = random_configs)
print_result(results)

"""
Since NORNIR wraps all the exit codes in an aggregated object/results which completes execution with OK, regardless of any errors during the config push to devices.
If there is an error during the config push, NORNIR will save the error in data.failed_hosts.
Following code block will raise Error explicitly if the config push detects a failure, which Jenkins will detect, and mark the build as FAILED.
"""

failures = nr.data.failed_hosts
if failures:
    # print("FAILURE")
    raise NornirExecutionError("Nornir Failure Detected")