# pipeline_airflow
Тестовый пайплайн для запуска Docker-контейнеров в Apache Airflow

Для повторения:
1. В текущей папке создать виртуальное окружение и активировать его

```bash
python3 -m venv airflow_venv 
source airflow_venv/bin/activate 
```

2. Установить Apache Airflow и провайдер для работы с докером

```bash
pip install apache-airflow apache-airflow-providers-docker[common.compat]
```

3. Инициализация базы данных для Airflow

```bash
airflow db init 
```

4. Создайть администратора для Airflow

```bash
airflow users create --username admin --password admin --firstname Firstname --lastname Lastname --role Admin --email admin@example.com
```

5. Собрать оба контейнера:

```bash
cd sample-run
docker build -t reader:v1 -f Dockerfile.reader .
docker build -t writer:v1 -f Dockerfile.writer . 
```

Можно проверить работу:

```bash
docker run --rm -v $(pwd)/data:/data writer:v1
docker run --rm -v $(pwd)/data:/data reader:v1
```

6. Для запуска веб-сервера:

```bash
airflow webserver --port 8080
```

7. В другом терминале запустить планировщик:

```bash
airflow scheduler
```
8. Перейти на [http://localhost:8080](http://localhost:8080)
