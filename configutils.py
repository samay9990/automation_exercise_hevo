# config_utils.py
import os
import yaml


class ConfigUtils:

    def __init__(self, file_path="config.yml"):
        self.config = self.load_config(file_path)

    def load_config(self, file_path):
        """
        Reading values from config.yml file
        :param file_path:
        :return:
        """
        with open(file_path, "r") as file:
            return yaml.safe_load(file)

    def get_env(self):
        """
        Get env from config.yml file
        :return: {str}
        """
        return os.getenv("ENV", self.config.get("ENV", "dev")).upper()

    def get_url(self):
        """
        Get url from config.yml file
        :return: {str}
        """
        return os.getenv("URL", self.config[self.get_env()].get("URL", ""))

    def get_fullname(self):
        """
        Get username from config.yml file
        :return: {str}
        """
        return os.getenv("FULLNAME", self.config[self.get_env()].get("FULLNAME", ""))

    def get_username(self):
        """
        Get username from config.yml file
        :return: {str}
        """
        return os.getenv("USEREMAIL", self.config[self.get_env()].get("USEREMAIL", ""))

    def get_password(self):
        """
        Get password from config.yml file
        :return: {str}
        """
        return os.getenv("PASSWORD", self.config[self.get_env()].get("PASSWORD", ""))


    def get_headless_mode(self):
        """
        Get headless mode from config.yml file
        :return: {str}
        """
        return os.getenv("HEADLESS_MODE", self.config[self.get_env()].get("HEADLESS_MODE", True))

    def get_default_wait(self):
        """
        Get default wait from config.yml file
        :return: {str}
        """
        return int(os.getenv("DEFAULT_WAIT", self.config[self.get_env()].get("DEFAULT_WAIT", 10)))
