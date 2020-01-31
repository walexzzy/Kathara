from .KubernetesConfig import KubernetesConfig
from .KubernetesLink import KubernetesLink
from .KubernetesMachine import KubernetesMachine
from .KubernetesNamespace import KubernetesNamespace
from ...decorators import privileged
from ...exceptions import NotSupportedError
from ...foundation.manager.IManager import IManager
from kubernetes import client


class KubernetesManager(IManager):
    __slots__ = ['client', 'k8s_namespace', 'k8s_link', 'k8s_machine']

    # @check_k8s_status
    def __init__(self):
        KubernetesConfig.load_kube_config()

        self.k8s_namespace = KubernetesNamespace()
        self.k8s_link = KubernetesLink()
        self.k8s_machine = KubernetesMachine()

    def deploy_lab(self, lab, privileged_mode=False):
        # Kubernetes needs only lowercase letters for resources.
        # We force the folder_hash to be lowercase
        lab.folder_hash = lab.folder_hash.lower()

        self.k8s_namespace.create(lab)
        self.k8s_link.deploy_links(lab)

        # TODO: Scheduler
        self.k8s_machine.deploy_machines(lab, privileged_mode)

    @privileged
    def update_lab(self, lab_diff):
        raise NotSupportedError("Unable to update a running lab.")

    @privileged
    def undeploy_lab(self, lab_hash, selected_machines=None):
        if selected_machines:
            raise NotSupportedError("Cannot delete specific devices from running lab.")

        lab_hash = lab_hash.lower()

        self.k8s_machine.undeploy(lab_hash, selected_machines=selected_machines)
        self.k8s_link.undeploy(lab_hash)

    @privileged
    def wipe(self, all_users=False):
        if all_users:
            raise NotSupportedError("Cannot use `--all` flag.")

        self.k8s_machine.wipe()
        self.k8s_link.wipe()

    @privileged
    def connect_tty(self, lab_hash, machine_name, shell, logs=False):
        pass

    @privileged
    def exec(self, machine, command):
        pass

    @privileged
    def copy_files(self, machine, path, tar_data):
        pass

    @privileged
    def get_lab_info(self, lab_hash=None, machine_name=None, all_users=False):
        pass

    @privileged
    def get_machine_info(self, machine_name, lab_hash=None, all_users=False):
        pass

    @privileged
    def check_image(self, image_name):
        pass

    @privileged
    def check_updates(self, settings):
        pass

    @privileged
    def get_release_version(self):
        core_client = client.CoreApi()
        versions = core_client.get_api_versions()

        print(versions)

        return 1

    @staticmethod
    def get_manager_name():
        return "kubernetes"

    @staticmethod
    def get_formatted_manager_name():
        return "Kubernetes (Megalos)"