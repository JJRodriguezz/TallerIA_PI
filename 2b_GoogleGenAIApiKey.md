## Creación de la API key de Gemini

**Nota**: La creación de la API key de gemini es opcional, sin embargo puede ser bastante útil para el desarrollo de sus proyectos.

Para crear la API key en openAI, debe ingresar con su cuenta de google a la página de [GoogleAI](https://ai.google.dev/gemini-api/docs/api-key?hl=es-419) e ingresa a ``Obtén una clave de API`` 

 <div align="center">
  <a>
    <img src="imgs/keyGoogle1.png">
  </a>
  </div>

  En esta nueva pantalla debe hacer clic en ``Crear clave de API`` 

   <div align="center">
  <a>
    <img src="imgs/keyGoogle6.png">
  </a>
  </div>


   <div align="center">
  <a>
    <img src="imgs/keyGoogle3.png">
  </a>
  </div>

  Copiar la API y almacenarla en el archivo `api_keys.env`
  
   <div align="center">
  <a>
    <img src="imgs/keyGoogle5.png">
  </a>
  </div>

   <div align="center">
  <a>
    <img src="imgs/keyGoogle4.png">
  </a>
  </div>

  
Almacene este archivo en la carpeta raíz del proyecto

   <div align="center">
  <a>
    <img src="imgs/keyGoogle7.png">
  </a>
  </div>

Verifique que el archivo ``.gitignore`` está en la raíz del proyecto (__si el archivo ya está creado, puede omitir este paso__). Si no está creado, debe ubicarse en la raíz del proyecto y escribir la instrucción ``echo. > .gitignore``

 <div align="center">
  <a>
    <img src="imgs/key7_5.PNG">
  </a>
 </div>

Abra con un editor de texto el archivo ``.gitignore`` que se encuentra en la raíz del proyecto. En este archivo se deben poner los nombres de los archivos que no queremos que se compartan en el repositorio en GitHub

   <div align="center">
  <a>
    <img src="imgs/keyGoogle8.png">
  </a>
  </div>

  De esta forma su API key estará segura y no tendrá que compartirla ni escribirla en ningún otro documento.
