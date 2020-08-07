# Lab: Machine Learning with Spark

## Start your cluster

Start EMR Cluster with cluster configuration and bootstrap actions as described in the [reference for starting a cluster using bootstrap actions and software customization for Spark.](https://github.com/bigdatateaching/using-bootstrap-actions)

**Recommended setup:** 1 master and 2 core of m5.xlarge


## Connect to the cluster

* Once the cluster is in "Waiting" mode (should only take a few minutes), ssh into the master **with local port forwarding (-L)**, and with **agent forwarding (-A) if necessary**:

```
ssh-add
ssh -A -L 8765:localhost:8765 hadoop@...
```
* Run your `git-config` commands
* Clone your repository to the master node


## Lab Exercises

There is one notebook with lab exercises and instructions:

* Machine Learning with Spark: [lab-machine-learning-with-spark.ipynb](lab-machine-learning-with-spark.ipynb) 

Click on the link to open the notebook.

## Submitting the Lab

Do all the work in the Jupyter Notebook. You must save the notebooks when you finish your work. After you save the notebook, you must commit your changes and push to GitHub. 

