# Building a Data Lake

## run docker compose

```sh
docker-compose up
```

## open spark on port that we already mapped on docker compose

port 8888

## take the token from terminal window after running docker compose to log in to Jupyter

We finally can configurate python files in Jupyter


# Documentation

## docker compose have mounted folder on codespace to Jupyter

```sh
volumes:
      - .:/home/jovyan/work
```
## import spark session libery to use Spark

```sh
from pyspark.sql import SparkSession
```

## create Spark instance

```sh
spark = SparkSession.builder \
    .appName("ETL") \
    .getOrCreate()
```

## using SQL on PySpark by createOrReplaceTempView

```sh
data.createOrReplaceTempView("staging_events")
```

## run sql on PySpark with this example

```sh
table = spark.sql("""
    select
        id
        , type
        , created_at
        , day(created_at) as day
        , month(created_at) as month
        , year(created_at) as year
        , date(created_at) as date
    from
        staging_events
""")
```

## create destination (folder)

```sh
destination = "events"
```

## dumping file in folder with partition (column) we saparated 

```sh
table.write.partitionBy("year", "month", "day").mode("overwrite").csv(destination)
```
