# Grandma´s Cookbook

Proyecto para Web de Datos

<div align="center">
  <img src="/assets/logo.jpg" alt="Cookbook logo" width="300"/>
</div>

## Prerequisitos

Para ejecutar el proyecto únicamente es necesario tener instalado Docker y Docker-compose.

## Ejecución

Para poner en marcha el proyecto tan solo es necesario ejecutar el siguiente comando desde el directorio raíz que contiene el archivo `docker-compose.yml`.

```
docker compose up -d
```

Para ver la interfaz del gateway basta con acceder al puerto `50002`. En caso de querer acceder a la interfaz web, el puerto es el `4200`.

## Estructura del proyecto

El proyecto está organizado con un archivo [docker-compose](/docker-compose.yml) que se encarga del despliegue del mismo.

Además, cada carpeta corresponde a un contenedor.

### Back-end

| **Contenedor** | **Función** |
|:---:|:---:|
| [recipes-api](/recipes-api/) | ... |
| [load-balancer-recipes](/load-balancer-recipes/) | ... |
| [database-api](/database-api/) | ... |
| [cookbook-gateway](/cookbook-gateway/) | ... |

### Front-end

| **Contenedor** | **Función** |
|:---:|:---:|
| [cookbook-web](/cookbook-web/) | ... |