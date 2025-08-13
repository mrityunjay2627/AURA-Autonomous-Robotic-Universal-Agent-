FROM python:3.12-slim-bookworm

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the dependency file and install dependencies first
# This leverages Docker's layer caching. The dependencies are only re-installed
# if the requirements.txt file changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the application source code and config into the container
COPY src/ ./src/
# COPY .env .

# 5. Specify the command to run when the container starts
CMD ["python", "src/aura/main.py"]