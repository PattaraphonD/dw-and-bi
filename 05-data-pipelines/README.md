# Instruction 

docker compose up

add data to dags folder

open airflow from port 8080

open elt.py 
to config script and automate with airflow

run docker compose exec postgres bash
to access postgres and be able to query with bash

# Documentation

in etl.py file

create function
- get files
- create tables
- process

create connection with hook and apply on create tables and process function
```
# connect to postgres
    hook = PostgresHook(postgres_conn_id="my_postgres_conn")
    conn = hook.get_conn()
    cur = conn.cursor()
```

create DAG to begin with Airflow 
start >> [get_files, create_tables] >> process >> end
@daily