# Hive Bugs Prediction

## Resources

### Data inputs

- [Hive bugs](https://issues.apache.org/jira/browse/HIVE-4413?jql=project%20%3D%20HIVE%20AND%20issuetype%20%3D%20Bug%20AND%20status%20%3D%20Resolved%20AND%20affectedVersion%20in%20(2.0.0%2C%202.0.1%2C%202.1.0%2C%202.1.1%2C%202.2.0%2C%202.3.0%2C%202.3.1%2C%202.3.2%2C%202.3.3%2C%202.3.4%2C%202.3.5%2C%202.3.6%2C%202.3.7%2C%202.3.8%2C%202.4.0%2C%203.0.0%2C%203.1.0%2C%203.1.1%2C%203.1.2%2C%203.1.3)%20ORDER%20BY%20affectedVersion%20ASC%2C%20priority%20DESC%2C%20updated%20DESC) affecting released version > 2.0.0
- [Hive github](https://github.com/apache/hive) project commits history using following command:

```bash
git log --name-only --pretty=oneline > hive-git-logs.txt
```

- [Released versions dates](https://hive.apache.org/downloads.html) used to get the latest commit before releasing each version.

- [Understand metrics](https://support.scitools.com/support/solutions/articles/70000582223-what-metrics-does-understand-have-) explanations.
