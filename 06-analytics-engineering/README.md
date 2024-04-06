create virtual env 
python -m venv ENV

--
activate ENV
source ENV/bin/activate

install packages
pip install -r requirement.txt (already created all updated package version)

cd ds525

dbt debug

initiate project
dbt init

---
name project -ds525
---

setup profile for collect information to connect to data warehouse

show information
code profile directory

create profile.yml to collect all information

---
check connection
dbt debug

All checks passed!

read all models and show in destination

run automate test
dbt test

create layer
> staging
> marts