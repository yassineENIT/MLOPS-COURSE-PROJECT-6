From python:3.9

WORKDIR /app
COPY . /app
# l'extension de --no-cache-dir permet de ne pas stocker les fichiers temporaires
# lors de l'installation des paquets, ce qui réduit la taille de l'image Docker finale
RUN pip install --no-cache-dir e .
EXPOSE 5000
ENV FLASK_APP=application.py

CMD ["python","application.py"]

