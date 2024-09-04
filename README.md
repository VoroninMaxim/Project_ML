#  Описание проекта
В рамках проекта использовалась модель (diabetes_model.sav) которая использует различные
медицинские параметры для прогнозирования вероятности развития диабета у пациентов.

# Запуск проекта в Jenkins
+ Создать задачу со свободной конфигурацией
+ Выполнить команду shell
+ pip install dvc
+ pip install dvc-gdrive
+ git clone https://github.com/VoroninMaxim/Project_ML.git
+ cd Project_ML
+ sudo -u jenkins dvc remote list
+ sudo -u jenkins dvc remote modify project_ml gdrive_acknowledge_abuse true
+ sudo -u jenkins dvc remote modify project_ml url gdrive://1jbdk1d9QgxQQfVvTBvXqNEOn6dXLGc4E
+ sudo -u jenkins dvc remote default project_ml
+ sudo -u jenkins dvc pull
+ sudo -u jenkins docker run -d -p 8505:8502 -P strim_app

# Приложение будет развернуто по адресу:
http://localhost:8501