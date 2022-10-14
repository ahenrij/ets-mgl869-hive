"""Git logs parser.

This script aims at converting the input hive logs file into a 
csv file formatted as follow:

BugID,File
HIVE-26619,Jenkinsfile
...
HIVE-26471,standalone-metastore/metastore-server/src/main/java/org/apache/hadoop/hive/metastore/metrics/AcidMetricService.java
...

Author: Henri Aidasso <ahenrij@gmail.com>
"""
import re

input_file = "src/data/input/hive-git-logs.txt"
output_file = "src/data/output/parsed-logs.csv"

with open(input_file, "r") as f:

    current_bug_id = None
    
    for line in f:
        # Capture new bug id
        if "HIVE-" in line:
            results = re.findall("HIVE-\d+", line) # should return array of 1

            if len(results) == 0:
                print("EMPY", results)

            current_bug_id = results[0] 
            print(current_bug_id)
