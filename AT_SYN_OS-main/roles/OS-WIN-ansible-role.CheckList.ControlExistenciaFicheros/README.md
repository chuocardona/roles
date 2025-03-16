Role Name
=========

Role para realziar la checklist de Aigues de Barcelona comprobacion de existencia de ficheros 

Requirements
------------

- Roles:
   - OS-LINUX-ansible-role.CSV.Dashboard
   - role_sharepoint_upload
 
Role Variables (case sensitive)
-------------------------------

| Variable          | Required | Default                              | Choices       | Comments                                                                                       |
| :------------------: | :----------: |:--------------------------------------: | :---------------: | :------------------------------------------------------------------------------------------------: |
| azure_url         | no      |    https://mdmabpro01sa.file.core.windows.net/sicab/MDMAB/Lectures/                              |               | Url al container de azure donde se alberga el fichero de Lectures|
| sas_url           | yes      | None                                 |               | QueryString de la cadena SAS (Desde el "?" hasta el final http://google.es?image=123.png seria ?image=123.png|
| checklist_code    | no      | CHK-0044                                 |               | Codigo checklist|
| file_path         | no      |   \\srvdfs01\APLICACIONES\BIG_DATA_MDMB_PRO\MDMAB\Lectures\                               |               | Share del servidor local donde buscar el fichero inicialmente|



Dependencies
------------



Example Playbook
----------------

```yaml
- name: PLAYBOOK CONTROL EXISTENCIA FICHEROS
  hosts: all
  gather_facts: true
  become: true
  become_method: ansible.builtin.runas
  var:
    sas_url="?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2026-04-04T13:18:05Z&st=2024-04-04T05:18:05Z&spr=https&sig=SIGNATURE"
  tasks:
    - name: CHECKLIST
      ansible.builtin.include_role:
        name: AT_SYN_WINDOWS-ansible-role.CHECKLIST.COMPROBACION-FICHEROS
```

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
