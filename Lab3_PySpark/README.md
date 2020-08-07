# Lab: Getting Started with Spark and PySpark

The purpose of this lab is for you to become familiar with Spark and use Python as a means to work with Spark. 

## Start your cluster

In order to work with Spark going forward, you will start the cluster with special configuration files and using what is called a bootstrap action.

You must follow the instructions in the [Using Bootstrap Actions Guide](https://github.com/bigdatateaching/using-bootstrap-actions). 

Follow the instructions there to start the cluster.

## Using Jupyter Notebooks as the front end to the Spark Cluster

You will be using [Jupyter Notebooks](https://jupyter.org/) as the main interface to Spark using Pyspark. You can use Jupyter for standard Python code, and you can create your SparkSession manually when needed.

### Manually creating the `SparkSession` in Jupyter


You will see the first cells in the lab notebook contain the following code:

```{python}
import findspark
findspark.init()
from pyspark import SparkContext
sc = SparkContext()
sc
```
Running this cell will find the Spark environment variables in the cluster and create the `SparkContext` and/or `SparkSession` objects inside your notebook. Please read this notebook to familiarize yourself with `SparkContext` and `SparkSession`

**This works on clusters created in class with the bootstrap action. It may not work on other kind of clusters.**

You can read more on `SparkSession` and `SparkContext` in this notebook: [creating-sparkcontext-and-sparksession.ipynb](creating-sparkcontext-and-sparksession.ipynb)

## Lab Exercises

There are two notebooks with lab exercises and instructions:
1. Learning about RDDs in the [1-basic-rdd-operations.ipynb](1-basic-rdd-operations.ipynb) notebook. 
2. Working with Spark DataFrames in the [2-dataframe-api-sparksql.ipynb](2-dataframe-api-sparksql.ipynb) notebook.

Click on the links to open the notebooks.

### Submitting the Lab

Do all the work in the Jupyter Notebooks. You must save the notebooks when you finish your work. After you save the notebook, you must commit your changes and push to GitHub. 

## Other Ways to Connect to Spark

There are several other ways to work with spark. We did not talk about them in class and they are here for reference.

### Spark shell (using Scala)

We didn't discuss this much in class. One of the ways to have an interactive session with Spark is by using the spark-shell. This starts an interactive, text based environment where you interact with the cluster using Scala.

Try it out! Type `spark-shell` in the command line. You'll know its Scala because you will see a Scala prompt. You can exit the spark-shell by using the `Ctrl-D` key combination.

```
[hadoop@ip-172-31-62-160 ~]$ spark-shell
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
17/06/27 21:18:02 WARN Utils: Service 'SparkUI' could not bind on port 4040. Attempting port 4041.
17/06/27 21:18:03 WARN Client: Neither spark.yarn.jars nor spark.yarn.archive is set, falling back to uploading libraries under SPARK_HOME.
Spark context Web UI available at http://172.31.62.160:4041
Spark context available as 'sc' (master = yarn, app id = application_1498593832174_0002).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.1.0
      /_/

Using Scala version 2.11.8 (OpenJDK 64-Bit Server VM, Java 1.8.0_121)
Type in expressions to have them evaluated.
Type :help for more information.

scala>
```

### PySpark shell (regular Python shell)

You can connect to Spark using PySpark, which runs a copy of the Python interpreter that's connected to the Spark runtime. As you can see, you see the Python version. You can exit this shell by typing quit(). If you had not run the scripts you ran after you started the cluster, this is what you would have to use Python with PySpark and Spark. 

```
[hadoop@ip-172-31-30-120 ~]$ pyspark
Python 2.7.13 (default, Jan 31 2018, 00:17:36)
[GCC 4.8.5 20150623 (Red Hat 4.8.5-11)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
18/03/12 14:43:52 WARN Client: Neither spark.yarn.jars nor spark.yarn.archive is set, falling back to uploading libraries under SPARK_HOME.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.2.1
      /_/

Using Python version 2.7.13 (default, Jan 31 2018 00:17:36)
SparkSession available as 'spark'.
>>>
```

### PySpark shell (using iPython - Text Based)

Another way to use PySpark is by telling PySpark to use the iPython shell. Since we installed iPython on this cluster (not installed by default), you need to setup an environment variable before starting PySpark and you will see the difference:

```
[hadoop@ip-172-31-30-120 ~]$ PYSPARK_DRIVER_PYTHON=ipython pyspark
Python 2.7.13 (default, Jan 31 2018, 00:17:36)
Type "copyright", "credits" or "license" for more information.

IPython 5.4.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
18/03/12 14:58:56 WARN Utils: Service 'SparkUI' could not bind on port 4040. Attempting port 4041.
18/03/12 14:58:59 WARN Client: Neither spark.yarn.jars nor spark.yarn.archive is set, falling back to uploading libraries under SPARK_HOME.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.2.1
      /_/

Using Python version 2.7.13 (default, Jan 31 2018 00:17:36)
SparkSession available as 'spark'.

In [1]: spark
Out[1]: <pyspark.sql.session.SparkSession at 0x7ff289c25bd0>

In [2]: sc
Out[2]: <SparkContext master=yarn appName=PySparkShell>

In [3]:
```

