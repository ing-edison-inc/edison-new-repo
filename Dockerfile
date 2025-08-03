FROM python:3.9-slim

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY . .

# Instalar dependencias si las hubiera
# RUN pip install -r requirements.txt

# Exponer puerto si es necesario
# EXPOSE 8000

# Comando por defecto
CMD ["python", "app.py"] 