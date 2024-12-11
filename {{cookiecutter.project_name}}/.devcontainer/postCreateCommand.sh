#! /usr/bin/env bash

# Install fish terminal
sudo apt update -y
sudo apt-get install fish -y
pip install dvc

# Install Dependencies
make install
