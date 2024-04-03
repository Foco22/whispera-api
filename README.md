# Whisper Api

Para iniciar el docker se debe seguir los siguientes pasos:

 1. Se debe tener instalado docker en el computador o VM. Si no lo tiene instalado, por favor seguir los siguiente pasos (esta instalación aplica para Linux). Si esta usando Windows, te recomiendo ver este enlance: https://docs.docker.com/desktop/install/windows-install/
    
    A. Actualizar el sistema usando;
    ```cmd
    sudo apt-get update
    ```
    B. Instalar adicionales paquetes:
    ```cmd
    sudo apt-get install \
      ca-certificates \
      curl \
      gnupg \
      lsb-release
    ```
    C. Añadir Docker’s official GPG key:
    ```cmd
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    ```    
    D. Instalar Docker Engine, aplicando los siguiente comandos:
    ```cmd
    sudo apt-get update
    ```   
    Adicionalmente:
    ```cmd
    sudo apt-get install docker-ce docker-ce-cli containerd.io
    ``` 

  2. Si quieres verificar la instalacion, puedes usar el siguiente comando:
    ```cmd
    sudo docker run hello-world
    ``` 

  3. Se debe ejecutar el siguiente comando para construir la imagen del docker. 
    ```cmd
    docker build -t whisper .
    ``` 
  4. Luego de construir la image, se debe ejecutar la imagen, usando lo siguiente:
    ```cmd
    docker run -p 8000:80 whisper
    ``` 
# Whisper Api

Este proyecto tiene principalmente un servicio, el cual se accede a traves de api/whisper desde el puerto localhost:8000 o del puerto de la VM, donde se despliegue el docker. 

Si se quiere probar usando python, se puede probar con el siguiente script:
    ```cmd
      import sys
      import requests

      hostname_or_ip = 'port' # tipicamente localhost si es de un computador personal.
      url = 'http://{}:8000/api/whisper'.format(hostname_or_ip)

      files = {'files': ('filename.mp3', open('audio.mp3', 'rb'), 'audio/mpeg')}

      response = requests.post(url, files=files)

      print(response.text)
    ``` 


