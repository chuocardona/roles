## Role Name

- OS-LINUX-ansible-role.CSV.Dashboard

Rol encargado de la escritura del fichero csv con la salida de las diferentes tareas de las checklists que se mostraran en el dashboard.


## Requirements

N/A

Role Variables (case sensitive)
-------------------------------

| Variable          | Required | Default                              | Choices       | Comments                                                                                       |
|-------------------|----------|--------------------------------------|---------------|------------------------------------------------------------------------------------------------|
| job_id            | yes      | 1                                    |               | Esta variable la define Ansible Tower                                                          |
| checklist_code    | yes      | 'CHK_NO_ESP'                         |               | Código de la checklist.                                                                        |
| task_name         | yes      | "Nombre_tarea_no_espscificado"       |               | Nombre descriptivo de la tarea que se ejecuta. Ejemplo: "Revisionficheros"                      |
| task_code         | yes      |                                      |               | Posición de la tarea dentro del playbook [1 para la primera tarea, 2 para la segunda ...]       |
| task_description  | yes      | "Descripcion_tarea_no_especificada"  |               | Descripción de la tarea que se ejecuta. Ejemplo: "Revisa que los ficheros de mdm diarios se haya procesado" |
| task_result       | yes      | "Pass"                               | Pass, NoPass  | Código de salida de la tarea.                                                                  |
| client_code       | yes      | 'NaN'                                |               | Código del cliente de 3 letras.                                                                |
| output_file_dir   | no       | "/tmp/dashboard_out/{{ job_id }}"    |               | Directorio donde se crean los ficheros de salida.                                              |
| output_file_name  | no       | "{{ client_code }}_{{ checklist_code }}_{{ task_code }}_{{ current_timestamp }}.csv" | | Nombre del fichero CSV que se genera.                                                          |
| execution_result  | no       | "OK"                                 |  OK,NOOK             | resultado global de la ejecucion de la tarea |

--------------

Dependencies
------------

N/A

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - name: Write CSV
      ansible.builtin.include_role:
        name: OS-LINUX-ansible-role.CSV.Dashboard
      vars:
        checklist_code: CHK-0018
        fase: "create"
        task_code: 1
        task_name: "Check MDM files"
        task_description: "Revisa presencia ficheros en directorio de MDM"
        task_result_description: "Ficheros existentes"
        task_result: 'Pass' # Cambiar variable con el return_code de la tarea
        client_code: "SYN"

License
-------

BSD

Author Information
------------------

kyndryl 
