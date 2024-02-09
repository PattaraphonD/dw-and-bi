# Instruction
1. Install CQL package > $ pip install cqlsh
2. run docker compose file > $ docker compose up
3. check the cassandra port 9042, It should be available (green icon)
4. run etl.py file to apply the ETL process
5. open CQL to run query > $ cqlsh
6. test the database by query > select * from github.events.events limit 10

# Documentation
- ติดตั้ง package CQL of cassandra
- สร้างตาราง One-Big table that contains :
    - id text,
    - type text,
    - actor_id text,
    - actor_login text,
    - repo_id text,
    - repo_name text,
    - repo_url text,
    - created_at timestamp,
    - is_public boolean
โดยมี Composite primary key เป็น id และ type
- ทำการทดสอบด้วยการ query cql บน $ cqlsh ด้วยคำสั่ง
    - select * from github.events.events limit 10
    - select repo_url from github.events.events limit 10