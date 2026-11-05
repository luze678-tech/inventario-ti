# Usar una imagen oficial y ligera de Python
FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias e instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente y la carpeta public
COPY . .

# Exponer el puerto en el que corre Flask
EXPOSE 3000

# Comando para iniciar la aplicación Flask
CMD ["python", "app.py"]