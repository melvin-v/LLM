# Usa una imagen base con Python 3.11
FROM python:3.11

# Configura el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos
COPY requirements.txt requirements.txt

# Instala las dependencias del sistema
RUN apt-get update && apt-get install -y \
    git ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Instala las dependencias de Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expone el puerto si más adelante se usa algo como Flask o FastAPI (opcional)
EXPOSE 8000

# Comando por defecto: inicia un intérprete interactivo de Python
CMD ["sleep", "infinity"]

