## Role Name

- AT_SYN_WINDOWS-ansible-role.CHECKLIST.AVERIAS

Rol encargado de revisar y solucionar las tareas de la checklist CHK-0018


## Requirements

N/A

Role Variables
--------------

| Variable          | Required | Default                              | Choices       | Comments                                                                                       |
|-------------------|----------|--------------------------------------|---------------|------------------------------------------------------------------------------------------------|
| OPTION            | yes      | none                                 | externes, internes, sistematics              | Tipo de proceso a revisar                                       |
| scheduled_task_name    | no      | VerificarServicio                |               | Nombre de la scheduled task del proceso (Normalmente no se debe cambiar)                       |
| procs_ok         | no      | no                                     |               | Estado de los procesos del aplicativo (Normalmente no se debe cambiar)                         |


--------------

Dependencies
------------

N/A

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - name: TEST UPLOAD FILES
      hosts: all
      tasks:
        - name: "Include role"
          ansible.builtin.include_role:
            name: AT_SYN_WINDOWS-ansible-role.CHECKLIST.AVERIAS
          vars:
            OPTION: 'externes'
            scheduled_task_name: 'VerificarServicio'
            procs_ok: no

License
-------

BSD

Author Information
------------------

kyndryl 
