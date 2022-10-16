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
output_file = "src/data/output/hive-issues-files.csv"

with open(input_file, "r") as f:
    bug_id = None
    output_content = "BugId,Filename\n"
    
    for line in f:
        line = line.strip()
        # Capture new bug id
        if results := re.findall("HIVE-\d+", line):
            bug_id = results[0]
            continue
        # Add new line of "bugId,filename" for Java and C++ files
        if line.endswith((".java", ".cpp", ".h")):
            output_content += f"{bug_id},{line}\n"

    # write output file
    with open(output_file, "w") as of:
        of.write(output_content)

    print("Logs successfully parsed!")