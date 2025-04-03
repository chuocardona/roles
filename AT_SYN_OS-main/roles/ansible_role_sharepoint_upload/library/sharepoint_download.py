#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
import os
from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.client_context import ClientContext

def download_report(clientId,secretId,file_url,filename,site_url):
    
    result = dict()

    # site_url = "https://<your tenant prefix>.sharepoint.com"
    credentials = ClientCredential(clientId, secretId)

    ctx = ClientContext(site_url).with_credentials(credentials)
    
    # file_url is the relative url of the file in sharepoint
    file_path = os.path.abspath(filename)
    with open(file_path, "wb") as local_file:
        file = ctx.web.get_file_by_server_relative_url(file_url)
        file.download(local_file)
        ctx.execute_query()
        
    result["msg"] = "File has been downloaded Successfully"
    result["download_path"] = file_path
    
def main():
    module_args = dict(
        clientId=dict(type='str', required=True),
        secretId=dict(type='str', required=True),
        file_url=dict(type='str', required=True),
        filename=dict(type='str', required=True),
        site_url=dict(type='str', required=True),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    clientId=module.params['clientId']
    secretId=module.params['secretId']
    file_url=module.params['file_url']
    filename=module.params['filename']
    site_url=module.params['site_url']

    try:
        result = download_report(clientId,secretId,file_url,filename,site_url)
        module.exit_json(changed=True, result=result)

    except Exception as e:
        module.fail_json(msg=str(e))

if __name__ == '__main__':
    main()
