from kubernetes import client, config
from os import path

import yaml
def create_my_service():
    config.load_kube_config()
    # api_instance = client.CoreV1Api()
    # service = client.V1Service()

    # service.api_version = "v1"
    # service.kind = "Service"
    # service.metadata = client.V1ObjectMeta(name="my-service-con1")

    # spec = client.V1ServiceSpec()
    # spec.selector = {"app": "con1_img"}
    # spec.ports = [client.V1ServicePort(protocol="TCP", port=80, target_port=9376)]
    # service.spec = spec

    # api_instance.create_namespaced_service(namespace="default", body=service)


    with open(path.join(path.dirname(__file__), "service_con1.yaml")) as f:
            dep = yaml.safe_load(f)
            k8s_apps_v1 = client.CoreV1Api()
            # resp = k8s_apps_v1.create_namespaced_deployment(body=dep, namespace="default")
            resp = k8s_apps_v1.create_namespaced_service(namespace="default", body=dep)
            print("Deployment created. status='%s'" % resp.metadata.name)


# if __name__ == '__main__':
#     create_my_service()