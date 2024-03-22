import json
import requests
requests.packages.urllib3.disable_warnings()

# Router IP Address is 10.0.15.189
api_url = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces"

# the RESTCONF HTTP headers, including the Accept and Content-Type
# Two YANG data formats (JSON and XML) work with RESTCONF 
headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"
          }
basicauth = ("admin", "cisco")


def create(studentID):
    # print("debugger studentID")
    # print(type(studentID))
    yangConfig = {
        "ietf-interfaces:interface": {
            "name": "Loopback{}".format(studentID),
            "description": "Added by RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": "172.30.{:s}.1".format(studentID[5:8]),
                        "netmask": "255.255.255.0"
                    }
                ]
            }
        }
    }

    resp = requests.post(api_url, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )
    # print("debugger create")

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback {} is created successfully".format(studentID)
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        # return "Error. Status Code: {}".format(resp.status_code)
        return "Cannot create: Interface loopback {}".format(studentID)
        
# print(create("64070215"))


def delete(studentID):
    api_url_delete = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces/interface=Loopback{}".format(studentID)
    resp = requests.delete(
        api_url_delete, 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback {} is deleted successfully".format(studentID)
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        return "Cannot delete: Interface loopback {}".format(studentID)

print(delete("64070215"))


def enable(studentID):
    api_url_put = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces/interface=Loopback{}".format(studentID)
    yangConfig = {
    "ietf-interfaces:interface": {
            "name": "Loopback64070215",
            "description": "Added by RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True
        }
    }

    resp = requests.put(
        api_url_put, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback {} is enabled successfully".format(studentID)
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        
# print(enable("64070215"))


def disable(studentID):
    api_url_put = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces/interface=Loopback{}".format(studentID)
    yangConfig = {
    "ietf-interfaces:interface": {
            "name": "Loopback64070215",
            "description": "Added by RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": False
        }
    }

    resp = requests.put(
        api_url_put, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        return "Interface loopback 66070123 is shutdowned successfully"
    else:
        print('Error. Status Code: {}'.format(resp.status_code))

# print(disable("64070215"))


def status(studentID):
    api_url_status = "https://10.0.15.189/restconf/data/ietf-interfaces:interfaces/interface=Loopback{}".format(studentID)
    yangConfig = {
    "ietf-interfaces:interface": {
            "name": "Loopback64070215",
            "description": "Added by RESTCONF",
            "type": "iana-if-type:softwareLoopback",
            "enabled": False
        }
    }

    resp = requests.get(
        api_url_status, 
        data=json.dumps(yangConfig), 
        auth=basicauth, 
        headers=headers, 
        verify=False
        )

    if(resp.status_code >= 200 and resp.status_code <= 299):
        print("STATUS OK: {}".format(resp.status_code))
        response_json = resp.json()
        admin_status = response_json['ietf-interfaces:interface']['enabled']
        oper_status = response_json['ietf-interfaces:interface']['enabled']
        if admin_status == 'up' and oper_status == 'up':
            return "Interface loopback {} is enabled".format(studentID)
        elif admin_status == 'down' and oper_status == 'down':
            return "<!!!REPLACEME with proper message!!!>"
    elif(resp.status_code == 404):
        print("STATUS NOT FOUND: {}".format(resp.status_code))
        return "No Interface loopback {}".format(studentID)
    else:
        print('Error. Status Code: {}'.format(resp.status_code))
        

