import os
import subprocess

from kubernetes import client, config
from os import path

import yaml
import logging
logging.basicConfig

logging.basicConfig(filename='MyscriptLog.log', filemode='w+', format='%(asctime)s- %(levelname)s - %(message)s',
                    level=logging.DEBUG)



def check_Oracle_virtualBox():
    """
    This method will check the existance of the Oracle Virtual Box and it's version
    """
    if os.system("vboxmanage --version") != 0:
        logging.debug("ORACLE virtual box not found and installing now")
        install_Oracle_virtualBox()
        logging.info("Oracel virtual Box installed successfully and version is "+str(os.system("vboxmanage --version")))
    else:
        vBox_version = subprocess.getoutput("vboxmanage --version")
        print("the version of the our oracle virtual box is ",vBox_version)
    # if vBox_version



def install_Oracle_virtualBox():
    pass
    os.system("echo '''gslab@123''' | sudo -S -v")
    os.system("sudo add-apt-repository multiverse && sudo apt-get update")
    os.system("sudo apt install -y virtualbox")





# def check_virtualization_support():
#     """
#     This method will check whether the virtualiztion is supported by the vm or not
#     If not supported then abort the entire installion
#     """
#     a = subprocess.getoutput("grep -E --color 'vmx|svm' /proc/cpuinfo")
#     if len(a) > 0:
#         pass
#     else:
#         print("Your vm does not support virtualization we can't proceed further")
#         exit(0)


def install_kubectl():
    """
    this method will install kubectl on the host machine
    """
    os.system("curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl")
    os.system("chmod +x ./kubectl")

    os.system("echo '''gslab@123''' | sudo -S -v")
    os.system("sudo mv ./kubectl /usr/local/bin/kubectl")


def check_kubectl_installation():
    """
    this method will check the installation  of kubectl on the host machine
    If it is not installed then it will again install the kubectl
    """
    kubectl_version = subprocess.getoutput("kubectl version")
    if len(kubectl_version) > 1:
        pass # write your logic ahead
    else:
        print("Again installing kubectl prevoius one was not installed ")
        install_kubectl()

def install_minikube():
    """
    This method will install the minikube 
    """
    os.system("curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube")
    os.system("echo '''gslab@123''' | sudo -S -v")
    os.system("sudo mkdir -p /usr/local/bin/")
    print("directory created ")
    status = os.system("sudo install minikube /usr/local/bin/")
    print("Installtion of binary of minikube ................... ",status)
    print("At the end of the isntall minikube function bin is used ")

def check_minikube_installation():
    """ 
    This method will check the installation of the minikube 
    If it is not installed then it will install the minikube again and delete the old installation
    """
    minikube_status_var = """host: Running
    kubelet: Running
    apiserver: Running
    kubeconfig: Configured"""
    minikube_status = subprocess.getoutput("minikube status")
    if minikube_status == minikube_status_var:
        print("Minikube instalation successfull")
    else:
        print("Installation of minikube failed")


def create_namespaces():
    """
    This method will create namespaces inside the minikube environment
    """
    pass
        
if __name__ == '__main__':
    install_kubectl()
    print("installation of kubectl done")
    check_kubectl_installation()
    print("check_kubectl_instaallation done ")
    install_minikube()
    print("installation of minikube done ")
    check_minikube_installation()
    print("Inside the check installation of the check the minikube installation")
    

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

def create_mongo_delploy():
    config.load_kube_config()

    with open(path.join(path.dirname(__file__), "mongo_deploy.yaml")) as f:
        dep = yaml.safe_load(f)
        k8s_apps_v1 = client.AppsV1Api()
        resp = k8s_apps_v1.create_namespaced_deployment(
            body=dep, namespace="mongo-namespace")
        print("Deployment created. status='%s'" % resp.metadata.name)


if __name__ == '__main__':
    # create_my_delploy()
    # create_my_service()
    pass