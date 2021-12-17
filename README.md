
## Environment and requirements
This env was built with and managed by miniconda. There is an environments.yaml that is maintained for this project. The assumption is that users will have miniconda installed on the development machine.

You can download from here: https://docs.conda.io/en/latest/miniconda.html
`wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh`

**NOTE:**
- For mac and linux installs, I recommend downloading the bash instance. Then it can be installed by running as a bash script. Also, I recommend not adding the initialization to your bash profile and sourcing it manually.

`echo "source /local/path/to/miniconda3/etc/profile.d/conda.sh" >> ~/.bash_profile`

Then, conda envs can be activated with `conda activate <env name>`


### create env with all dependencies
1. cd into ./env
2. run `conda env create -f env.yaml`


### restore pg database
1. ensure postgres is already installed and running on your machine
  - visit https://postgresapp.com/documentation/ for how to easy install on MacOS
2. instsall postgresql if now already isntalled with `brew install postgresql`
2. from the pqsl prompt run `psql>create database capdash_django`
3. run bash prompt `psql dbname < ./env/pg/capdash_django.dump`
