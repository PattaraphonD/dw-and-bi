# Analytics Engineer using dbt

## Create virtual env
``` 
python -m venv ENV
```
```
# activate ENV
source ENV/bin/activate
```

## Install packages from requirement.txt
```
pip install -r requirement.txt (already created all updated package version)
```

## initiate project
```
dbt init
```
### Setup project
```
name project -ds525
```

> setup profile for collect information to connect to data warehouse
show information

```
code | profile directory
```
> create profile.yml to collect all information

## Check connection
```
dbt debug
```
All checks passed!

## read all models and show in destination

- create model 

> run automate test
```
dbt test
```

- create layer
> staging
create model in staging

> marts

- materization
> by staging and marts

# Documentation

- Create file .sql to contain SQL script to run on dbt

in staging folder contain data which was prepared in staging layer 
to wait for transforming and fload in data warehouse 

- On dbt, we can use like SQL client to query

- The pros of dbt is making the SQL script reproducable