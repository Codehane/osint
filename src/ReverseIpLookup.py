import requests
import json

class Reverse_Ip_Check:
    @staticmethod
    def get_domains(domain_or_ip):
        req_dict = {
            'status' : '',
            'domains' : [],
            'host_ip' : ''
        }

        req = requests.get('http://reverseip.logontube.com/?url={}&output=json'.format(domain_or_ip))

        if req.status_code != 200:
            req_dict['status'] = 'Fail - ' + str(req.status_code)
            return req_dict

        if 'hostip' not in req.json().keys():
            req_dict['status'] = 'Fail - Invalid remote adress'
            return req_dict
       
        req_dict['domains'] = req.json()['response']['domains']
        req_dict['status'] = 'Success'
        req_dict['host_ip'] = req.json()['hostip']
        return req_dict