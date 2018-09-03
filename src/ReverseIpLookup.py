import requests
from http import HTTPStatus
from pprint import pprint

class Reverse_Ip_Check:
    @staticmethod
    def get_domains(domain_or_ip):
        req = requests.get("http://reverseip.logontube.com/?url={}&output=json".format(domain_or_ip))
        req_dict = {
            "status" : "",
            "message": "",
            "domains" : [],
            "host_ip" : ""
        }

        if req.status_code != 200:
            req_dict["status"] = "Fail"
            req_dict["message"] = HTTPStatus(req.status_code).name
            return req_dict

        if "hostip" not in req.json().keys():
            req_dict["message"] = 'Invalid remote adress'
            req_dict["status"] = 'Fail'
            return req_dict
       
        req_dict["domains"] = req.json()['response']['domains']
        req_dict['status'] = 'Success'
        req_dict['message'] = HTTPStatus(req.status_code).name
        req_dict['host_ip'] = req.json()['hostip']
        return req_dict

