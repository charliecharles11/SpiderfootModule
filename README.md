# Spiderfoot Module

SpiderFoot es una herramienta OSINT que facilita enormemente el proceso de Footprinting, al actuar como agregador de multitud de fuentes, sobre las que permite realizar una búsqueda sencilla y rápida al contar con su propia interface web.

Entre la multitud de módulos y fuentes de información  a utilizar por Spiderfoot, podemos citar entre otros:

* Shodan.
* Bing.
* Pastebin.
* Google.
* GeoIP.
* Escáner de puertos.
* Información sobre SSL.
* Ahmia.
* Spidering.
* Búsqueda en VirusTotal y listas negras/reputación.

### Instalación 🔧

Deberemos tener descargada la herramienta spiderfoot, puede ser desde su [página oficial](https://www.spiderfoot.net) o de repositorios de [Github](https://github.com/smicallef/spiderfoot).

Descomprimimos el archivo descargado y nos dirigimos a la carpeta spiderfoot-master. En este momento abrimos la carpeta modules y añadimos el módulo creado.

En ese momento tenemos que introducir el siguiente comando dentro de la carpeta:

```
cd Escritorio/spiderfoot-master/

python3 sf.py -l <IP_Address>:<Port>
```

En ese momento, si todo está correcto, nos aparece en el terminal una dirección URL donde estará la herramienta en funcionamiento.

Ya en este momento podemos realizar el escaneo de cualquier lugar que nosotros queramos para poder obtener información.

## Autor ✒️

* **Carlos Díaz** - *Actividad y Documentación* - [charliecharles11](https://github.com/charliecharles11)


## Licencia 📄

Este proyecto está bajo la Licencia GNU GENERAL PUBLIC LICENSE v3
