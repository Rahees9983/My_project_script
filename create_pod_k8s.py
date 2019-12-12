from kubernetes import client, config
from os import path

import yaml
def create_my_service():
    config.load_kube_config()

    with open(path.join(path.dirname(__file__), "service_con1.yaml")) as f:
            dep = yaml.safe_load(f)
            k8s_apps_v1 = client.CoreV1Api()
            # resp = k8s_apps_v1.create_namespaced_deployment(body=dep, namespace="default")
            resp = k8s_apps_v1.create_namespaced_service(namespace="namespaec-3", body=dep)
            print("Deployment created. status='%s'" % resp.metadata.name)

def create_my_delploy():
    config.load_kube_config()

    with open(path.join(path.dirname(__file__), "con1_img_deploy.yaml")) as f:
        dep = yaml.safe_load(f)
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(
            body=dep, namespace="namespaec-3")
        print("Deployment created. status='%s'" % resp.metadata.name)


def create_mongo_service():
    config.load_kube_config()

    with open(path.join(path.dirname(__file__), "service_con1.yaml")) as f:
            dep = yaml.safe_load(f)
            k8s_apps_v1 = client.CoreV1Api()
            # resp = k8s_apps_v1.create_namespaced_deployment(body=dep, namespace="default")
            resp = k8s_apps_v1.create_namespaced_service(namespace="namespaec-3", body=dep)
            print("Deployment created. status='%s'" % resp.metadata.name)


def create_mongo_delploy():
    config.load_kube_config()

    with open(path.join(path.dirname(__file__), "con1_img_deploy.yaml")) as f:
        dep = yaml.safe_load(f)
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(
            body=dep, namespace="namespaec-3")
        print("Deployment created. status='%s'" % resp.metadata.name)

if __name__ == '__main__':
    create_my_delploy()
    create_my_service()
    
    
