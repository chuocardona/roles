# AT_SYN_OS

Este repositorio almacena artefactos relacionados con la gestión y configuración de funciones del sistema operativo mediante Ansible. Contiene roles, playbooks y un archivo requirements.yml para la instalación de dependencias.



## 📁 Estructura del Repositorio

```
📦 AT_SYN_OS   
┣ 📂 roles/                              # Carpeta donde se almacenan los roles Ansible   
┃ ┣ 📂 role1/                            # Ejemplo de un rol específico    
┃ ┃ ┣ 📜 README.md                       # Documentación detallada del rol    
┃ ┃ ┣ 📂 tasks/                          # Definición de tareas del rol    
┃ ┃ ┣ 📂 handlers/                       # Definición de handlers (si aplica)    
┃ ┃ ┣ 📂 templates/                      # Archivos Jinja2 para configuración dinámica    
┃ ┃ ┣ 📂 files/                          # Archivos estáticos necesarios para el rol    
┃ ┃ ┣ 📂 vars/                           # Variables predefinidas del rol   
┃ ┃ ┣ 📂 defaults/                       # Valores predeterminados de las variables   
┃ ┃ ┗ 📂 meta/                           # Dependencias y metadatos del rol   
┣ 📜 requirements.yml                    # Lista de roles externos o dependencias necesarias   
┣ 📜 playbook1.yml                       # Playbook Ansible con documentación en cabecera   
┣ 📜 playbook2.yml                       # Otro playbook documentado   
┗ 📜 README.md                           # Este archivo con la descripción del repositorio   
```




## 📌 Nota: Todos los playbooks incluirán el siguiente encabezado:

```
---

#   OBJETIVO: resumen de acciones que realiza el playbook.
#  ESCENARIO: condiciones generales en la infraestructura/hosts a las que aplica el playbook.
# REQUISITOS: configuración detallada requerida en Ansible o los hosts que no encaje en INVENTARIO-CONFIGs, CREDENCIALES-REQ-s o INPUT-VARs.
#
# INVENTARIO-CONFIG: grupos y variables que se deben incluir en el inventario preferentemente (y no como input-vars). 
#                  Las variables opcionales se incluirán en el inventario, comentadas y con su valor por defecto. Indicar el tipo de cada variable.
#     Grupos: grupos requeridos en el inventario.
#     Group_vars: variables requeridas/opcionales. Indicar en cada caso de que tipo es (requerida/opcional), en que grupo debe ir (ALL u otros) y el tipo (integer, text, boolean, lista, diccionario). <Descripción>
#        ALL:
#          all_var1:
#          ...
#        <GRUPO_XXX>:
#          group_var1:
#            ...
#     Host_vars:
#        host_var1:
#        ...
#
# CREDENCIALES-REQs: credenciales necesarias para conectarse al/los servicio/s (NAgios, Vcenter, Foreman...) sobre los que ser realizarán acciones. Se pasará en ansible core como extra-var y en AWX como credencial que inyecta como extra-var. No se incluyen las credenciales de conexión a máquinas que se dan por supuestas. Indicar el tipo de cada variable.
#     SERVICIO1:
#        var_user
#        var_pass
#     ...
#
# INPUT-VARs-REQs: variables de entrada cuyo valor se establece en **tiempo de ejecución** (downtime name, tipo de acción entre las posibles...). Si no se establece su valor en tiempo de ejecución porque su valor es estandard y no depende de la ejecución, deberían definirse en el inventario y por tanto incluirse en el apdo. INVENTARIO-CONFIG. Indicar el tipo de cada variable.
# Requeridas: obligatorias, si no se pasan el playbook fallaría (no hay establecidos valores default para ellas). 
#     var1: <TIPO (integer, text, boolean, lista, diccionario)>. <Descripción>
#     ...
#
# INPUT-VARs-OPTs: variables de entrada cuyo valor se establece en **tiempo de ejecución** (downtime name, tipo de acción entre las posibles...). Si no se establece su valor en tiempo de ejecución porque su valor es estandard y no depende de la ejecución, deberían definirse en el inventario y por tanto incluirse en el apdo. INVENTARIO-CONFIG. Indicar el tipo de cada variable.
# Opcionales, pueden proporcionar al playbook para particularizar su funcionamiento por defecto. Si no se pasan el playbook emplearía los valores default para ellas.
#     var1: <TIPO (integer, text, boolean, lista, diccionario)>. <Descripción>
#     ...
#
#
```


## 📖 Documentación de Roles

Cada rol dentro de roles/ contiene un archivo README.md donde se explica:  

📌 Descripción del rol y su propósito.  

🔧 Variables disponibles y su configuración.  

▶️ Ejemplo de uso en un playbook.  

🔄 Dependencias si las hubiera.  


## 📌 Contribución

Crea un fork del repositorio.

Crea una nueva rama para tu cambio (git checkout -b feature/nueva-funcionalidad).

Realiza los cambios y documenta correctamente.

Sube los cambios (git push origin feature/nueva-funcionalidad).

Abre un Pull Request para revisión.


## Support

This asset was developed by the [Automation Enterprise CU Team](mailto:automation_enterprisecu@kyndryl.com)

If you want to submit an enhancement request, send us an email.



## 📜 Licencia

[Kyndryl Intellectual Property](https://github.kyndryl.net/Continuous-Engineering/CE-Documentation/blob/master/files/LICENSE.md)



