#!/bin/bash

# Запуск в сборке Jenkens
git clone https://github.com/VoroninMaxim/Project_ML.git
cd Project_ML
pip install dvc
pip install dvc-gdrive
sudo -u jenkins dvc remote list
sudo -u jenkins dvc remote modify project_ml gdrive_acknowledge_abuse true
sudo -u jenkins dvc remote modify project_ml url gdrive://1jbdk1d9QgxQQfVvTBvXqNEOn6dXLGc4E
sudo -u jenkins dvc remote default project_ml
sudo -u jenkins dvc pull
sudo -u jenkins docker run -d -p 8505:8501 -P strim_app