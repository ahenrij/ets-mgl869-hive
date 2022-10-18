"""This script aims at retrieving the latest commit for each 
identified release version of hive.

Run this script in the parent folder of the cloned hive project.

python releases_last_commits.py > releases-last-commits.csv

The output file is put in the data/output folder of the current project.

Author: Henri Aidasso <ahenrij@gmail.com>
"""

import subprocess


releases_dates = {
    "2.0.0": "2016-02-15",
    "2.0.1": "2016-05-25",
    "2.1.0": "2016-06-20",
    "2.1.1": "2016-12-08",
    "2.3.0": "2017-07-17",
    "2.2.0": "2017-07-25",
    "2.3.1": "2017-10-24",
    "2.3.2": "2017-11-18",
    "2.3.3": "2018-04-08",
    "3.0.0": "2018-05-21",
    "3.1.0": "2018-07-30",
    "3.1.1": "2018-11-01",
    "2.3.4": "2018-11-07",
    "2.3.5": "2019-05-14",
    "2.3.6": "2019-08-23",
    "3.1.2": "2019-08-26",
    "2.3.7": "2020-04-18",
    "2.3.8": "2021-01-17",
    "2.3.9": "2021-06-09",
    "4.0.0": "2022-03-30",
    "3.1.3": "2022-04-08"
}

releases_dates = dict(sorted(releases_dates.items()))

for k in releases_dates:
    last_commit = subprocess.run(["git", "log", f"--before='{releases_dates[k]}'", "--pretty=oneline", "-1"], capture_output=True, text=True).stdout
    last_commit_hash = last_commit.split(" ")[0]
    print(f"{k},{last_commit_hash}")
