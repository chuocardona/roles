# README

## Synopsis

This Ansible role uploads file(s) from configured ansible tower path to the configured sharepoint site. It runs on the tower so, doesn't need to be executed on any specific host, playbook will fetch the required files to the local tower and after that will upload the files to your sharepoint site.

## Variables

Variable | Default| Comments
----------|-----------------|--------
**create_folder_in_sp** (bool) | true | Whether or not to create folder under `sharepoint_root_folder` (if set to false, ensure you have a folder created under `sharepoint_root_folder` and also add its name to `sp_dir_create`).
**create_custom_folder** (bool) | false | Whether or not to create folder with custom name under `sharepoint_root_folder` (if set to true, Make sure `custom_folder_name` is passed to the Job Template).
**create_subfolder_in_sp** (bool) | false | Whether or not to create a subfolder under `sharepoint_root_folder`/`(sp_dir_create) or (custom_folder_name)`.
**upload_to_subfolder** (bool) | false | Whether or not to upload files to sub folder. Make sure either `create_subfolder_in_sp` or `subfolder_name`(this should be present on SP, When `create_subfolder_in_sp` is set to false) is passed to the job template.
**sp_dir_create** (str) | <sp_dir_prefix>_<tower_job_id> | Default name of the SharePoint folder that will be created when `create_folder_in_sp` is set to true.
**custom_folder_name** (str) | '' | Name of the folder to be created under sharepoint_root_folder, This is **Mandatory** when `create_custom_folder` or `upload_to_custom_folder` is set to true.
**delete_file_from_sp** (bool) | false | Whether or not to delete file from SharePoint
**delete_file_name** (list) | [] | List of files to be deleted, This is **Mandatory** when `delete_file_from_sp`is set to true.
**delete_folder_name** (str) | '' | Name of the folder under which the to be deleted file exists
**download_folder_name** (str) | '' | Name of the SharePoint folder from which download should happen. This is **Mandatory** when `download_from_sp` is set to true.
**download_file_name** (list) | [] | List of files that needs be donwloaded from `download_folder_name`. This is **Mandatory** when `download_from_sp` is set to true.
**download_from_sp** (bool) | false | Whether or not to perform a download operation
**sharepoint_root_folder** (Str) | '' | **Mandatory** The root folder under sharepoint site/teams under which the upload happens.
**sharepoint_site_url** (Str) | '' | **Mandatory** The sharepoint site/teams URL (Ex.: `https://kyndryl.sharepoint.com/sites/<site name>`).
**sp_dir_prefix** (str) | 'upload_job' | The prefix for the directory name that will created.
**sp_teams_notification** (bool) | false | To send teams notification.
**subfolder_name** (str) | '' | Name of the sub folder to created or to which files are to be uploaded. This is mandatory when `create_subfolder_in_sp` or `upload_to_subfolder` is set to true.
**teams_notification_summary** (str) | 'Ansible Automation' | Summary in the teams message card.
**teams_notification_title** (str) | 'Ansible Automation' | Title in the teams message card.
**tower_src_path** (str) | '' | **Mandatory** The source path of files in ansible tower.
**webhook_url** (str) | 'NA' | Webhook URL for Teams notification. This is **Mandatory** when `sp_teams_notification` is set to true.

## Results from execution

Return Code Group | Return Code | Comments
----------|--------------|---------
account | 0 |  Files uploaded/downloaded/deleted successfully to/from SharePoint
account | 201 |  Mandatory variables are not/improperly configured
developer | 202 |  Failed to find files for upload under given `tower_src_path`
account | 203 |  No files found under given `tower_src_path` for upload
developer | 204 |  SharePoint upload/download/delete failed

## Procedure

### SharePoint Upload (default functionality)

1. Collects files from the tower host path configured in `tower_src_path`.
2. If the file count is above 0,
    1. It creates a folder (sp_dir_create or custom_folder_name) under the `sharepoint_root_folder` in `sharepoint_site_url`.
    2. Uploads the collected file to the newly created folder.

### SharePoint Download (download_from_sp: true)

1. Creates a `temporary_tower_dir` on tower.
2. Downloads the list of file mentioned in `download_file_name` from `download_folder_name` (sharepoint_site_url/download_folder_name/download_file_name).

## Support

Support Information is available here: `https://continuous-engineering.eu-de.mybluemix.net/cacm`

## Deployment

Deployment Information is available here: `https://continuous-engineering.eu-de.mybluemix.net/cacm`

### Preparing Sharepoint

#### **API KEY Generation**

If you don't have a client_id and secret_id, you need to generate a new API KEY for your sharepoint site, this procedure can be ONLY executed for the admins/creators/owners of the sharepoint site. You can identify the admins by entering to the your main site: e.g `https://kyndryl.sharepoint.com/sites/SITE_TESTING` and click on the top right option `members`.

**Admin Steps:**

1. In browser open following link:
    `https://kyndryl.sharepoint.com/sites/(your_site)/_layouts/15/appregnew.aspx`

    **Please change `(your_site)`

2. In form: Generate Client ID and Client Secret (save them somewhere, this values will be your `client_id` and `secret_id` Ansible Variables)
- Title: put name of your AP
- App Domain: www.kyndryl.com
- Redirect URI: `https://www.kyndryl.sharepoint.com/`

3. Click on Create

4. In browser open following link:
    `https://kyndryl.sharepoint.com/sites/(your_site)/_layouts/15/appinv.aspx`

**Please change `(your_site)`

5. In App Id copy generated Client ID and click on “Lookup”. It will automatically fill rest of form

6. In “Permission Request XML” copy following xml:

    ```
    <AppPermissionRequests AllowAppOnlyPolicy="true">
    <AppPermissionRequest Scope="http://sharepoint/content/sitecollection" Right="FullControl"/>
    <AppPermissionRequest Scope="http://sharepoint/content/sitecollection/web" Right="FullControl"/>
    </AppPermissionRequests>
    ```

7. Click on Create

8. Click on “Trust"

9. Add the generated Client ID and Secret ID to respective `api_id` and `api_secret` in the created sharepoint credential of type `credtype_sharepoint`. Refer to [credtype_sharepoint](https://pages.github.kyndryl.net/CACF/cacf_docs/credential-guidance/credtype_sharepoint/) documentation

## Known problems and limitations

NA

## Prerequisites

1. Standard Ansible prerequisites
2. Python 2(version 2.7) and Python 3(version 3.5 and higher)

## License

[Kyndryl Intellectual Property](https://github.kyndryl.net/Continuous-Engineering/CE-Documentation/blob/master/files/LICENSE.md)
