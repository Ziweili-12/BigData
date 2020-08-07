# Assignment - Spark RDD and SparkSQL

**You should thoroughly read through the entire assignment before beginning your work! Don't start the cluster until you are ready.**

### Provide the Master Node and Cluster Metadata

Provide the instance metadata. Run this command in the master node command line.

```
curl http://169.254.169.254/latest/dynamic/instance-identity/document/ > instance-metadata.json
```


## Problem 1: Working with RDDs (4 points)

Amazon maintained a list of the top 1 million Internet sites by traffic at the URL (they do not anymore). A recent copy is included in this repository which you will use for this problem. 

In this problem you will:

* Make an RDD where each record is a tuple with the (rank, site)
* Determine the number representation of top-level domains (TLDs) in the top 10,000 websites. Example TLDs are `com`, `edu` and `cn`. (Do not include the `.`). 

### Place the domains file in HDFS

* Unzip the file `top-1m.csv.zip`
* Put the file `top-1m.csv` into HDFS with the command:

```
[hadoop@ip-172-31-91-222 ~]$ hadoop fs -put top-1m.csv top-1m.csv
```

Verify that the file is there with `hadoop fs -ls`.

```
[hadoop@ip-172-31-91-222 ~]$ hadoop fs -ls
Found 2 items
drwxr-xr-x   - hadoop hadoop          0 2018-03-25 18:48 .sparkStaging
-rw-r--r--   2 hadoop hadoop   23245165 2018-03-25 18:50 top-1m.csv
```

The rest of the work will be done within the [problem-1.ipynb](problem-1.ipynb) Jupyter notebook.

After you finish working on the problem, you will commit the Jupyter notebook `.ipynb` file called `problem-1.ipynb.`

## Problem 2: Working with SparkSQL (6 points)

You will perform the work for this problem within the [problem-2.ipynb](problem-2.ipynb) Jupyter notebook.

After you finish working on the problem, you will commit the Jupyter notebook `.ipynb` file called `problem-2.ipynb.`

## Submitting the Assignment

Make sure you commit **only the files requested**, and push your repository to GitHub!

The files to be committed and pushed to the repository for this assignment are:

* `instance-metadata.json`
* `problem-1.ipynb`
* `problem-2.ipynb`
