# Usar una imagen oficial de Python como imagen base (Python 3.8)
FROM python:3.8-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar los archivos de requisitos al contenedor
COPY requirements.txt requirements.txt

# Instalar las dependencias
RUN pip install -r requirements.txt

# Copiar el resto del código de la aplicación al contenedor
COPY . .

# Exponer el puerto que se va a usar para el servidor de desarrollo
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]