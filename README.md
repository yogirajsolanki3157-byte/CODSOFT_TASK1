# CodSoft DevOps Internship - Task 1: Dockerized Web Application

**Intern Name:** Yogiraj Solanki  
**Batch:** October - November 2026

## Completed Objectives:
1. Created a Python Flask web application (`app.py`).
2. Wrote a `Dockerfile` to package the application and its dependencies into a lightweight container image.
3. Built and executed the Docker container on port `5000`.
4. **Bonus Completed:** Configured `docker-compose.yml` for multi-container orchestration (Flask Web App + Redis service).

## Commands Used:
- Build Image: `docker build -t yogiraj-docker-app:v1 .`
- Run Container: `docker run -d -p 5000:5000 yogiraj-docker-app:v1`
- Run Multi-Container: `docker compose up -d`# CODSOFT_TASK1
