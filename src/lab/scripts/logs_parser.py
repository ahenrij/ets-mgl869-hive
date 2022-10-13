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