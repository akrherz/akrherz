#!/bin/bash
#
# `conda update --all` is not working well with conda-forge and I want
# to use conda-forge, so we need to be able to reproduce the conda env
# on demand, maybe life will be better this way
. /opt/miniconda3/etc/profile.d/conda.sh
set -x

# switch back to root env, so we can delete the prod env
conda activate root
# save a backup
conda create --name prod.$(date -u +%Y%m%d%H%M%S) --clone prod
# delete, gasp
conda remove -n prod --all -y
# create the env
conda create -n prod python=3.6 pip -y
# switch to it
conda activate prod

# do project needs
for project in iem iembot pyIEM weather.im dep
do
  conda install -y --file /home/akrherz/projects/$project/conda_requirements.txt
  pip install --upgrade -r /home/akrherz/projects/$project/pip_requirements.txt
done

pip install cdsapi

# extra stuff
conda install -y flake8 pep8 wrf-python geopy twisted jupyterhub \
 notebook twine eccodes jupyterlab sphinx siphon

# adds jupyterhub stuff to lab
jupyter labextension install @jupyterlab/hub-extension

# manual stuff to do before uploading to servers
echo " + ensure pint<0.9 is installed due to metpy + units issues"
echo " + need MANUAL edit of cartopy for 3 point polygon issue"
echo " + need to add 102100 900913 codes into share/proj/epsg"
echo " + make install in mapserver/build, not just python there"
echo " + metpy 0.8 PR #887 mased_array needed"
echo " + hard code TEST_DATA_DIR in pooch/core.py"
