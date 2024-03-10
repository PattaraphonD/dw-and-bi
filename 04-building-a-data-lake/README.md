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
การ mount folder from codespace จะสามารถทำให้เรา connect กับข้อมูลที่อยู่ในโฟลเดอร์ที่ถูกสร้างนอก Jupyter ได้

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
ฟังก์ชันนี้จะทำให้สามารถเขียน SQL บน PySpark ได้ รวมถึงทำการ transform data ผ่าน SQL ได้

```sh
data.createOrReplaceTempView("staging_events")
```

## run sql on PySpark with this example
ทดสอบด้วยการ run ด้วย SQL 

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
ต้องทำการสร้าง Folder เพื่อที่จะ dump file ที่เราทำการ transform มาเก็บที่นี่

```sh
destination = "events"
```

## dumping file in folder with partition (column) we saparated 
save files ที่ทำการ transformed ลงใน folder ที่สร้างไว้
รวมถึงมีการแบ่ง partition หรือ column ตามที่เราได้ transform บน SQL ข้างต้น

```sh
table.write.partitionBy("year", "month", "day").mode("overwrite").csv(destination)
```