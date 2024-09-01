FROM python:3.12

#USER root
# Expose port you want your app on
EXPOSE 8501

# Upgrade pip and install requirements
COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

# Copy app code and set working directory
COPY . .

#WORKDIR /app
#HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run
ENTRYPOINT ["streamlit", "run", "app_p2.py", "--server.port=8501", "--server.address=0.0.0.0"]

#USER jenkins