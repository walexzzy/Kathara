from abc import ABC, abstractmethod


class IManager(ABC):
    @abstractmethod
    def deploy_lab(self, lab):
        raise NotImplementedError("You must implement `deploy_lab` method.")

    @abstractmethod
    def undeploy_lab(self, lab_hash, selected_machines=None):
        raise NotImplementedError("You must implement `undeploy_lab` method.")

    @abstractmethod
    def wipe(self):
        raise NotImplementedError("You must implement `wipe` method.")

    @abstractmethod
    def connect_tty(self, lab_hash, machine_name, shell):
        raise NotImplementedError("You must implement `connect_tty` method.")

    @abstractmethod
    def get_lab_info(self, lab_hash=None, machine_name=None):
        raise NotImplementedError("You must implement `get_lab_info` method.")

    @abstractmethod
    def get_machine_info(self, machine_name, lab_hash=None):
        raise NotImplementedError("You must implement `get_machine_info` method.")

    @abstractmethod
    def check_image(self, image_name):
        raise NotImplementedError("You must implement `check` method.")

    @abstractmethod
    def check_updates(self, settings):
        raise NotImplementedError("You must implement `check_updates` method.")

    @abstractmethod
    def get_release_version(self):
        raise NotImplementedError("You must implement `get_release_version` method.")

    @abstractmethod
    def attach_links_to_machine(self, lab, machine_name, link_names):
        raise NotImplementedError("You must implement `attach_links_to_machine` method.")
