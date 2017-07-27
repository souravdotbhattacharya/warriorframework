import json


class WfConfigFileClass():

    def __init__(self, config_file_path, config_details_dict=None):
        """
        This is the constructor for WfConfigFileClass()

        Args:
            config_file_path: Absolute path to the wf_config file
            config_details_dict: details to be obtained from the wf_config file
        """
        self.config_file_path = config_file_path

        self.config_file_data = self._get_config_file_data()
        self.config_details_dict = config_details_dict

    def set_config_details_dict(self, config_details_dict):
        self.config_details_dict = config_details_dict

    def get_details_from_file(self):
        """
        This function loops through the self.config_details_dict to get the value for the keys in
        it from the self.config_file_data dict
        Returns:
            self.config_details_dict

        """
        if self.config_details_dict is not None:
            for key in self.config_details_dict:
                if key in self.config_file_data:
                    self.config_details_dict[key] = self.config_file_data[key]
        else:
            self.config_details_dict = self.config_file_data.copy()
        return self.config_details_dict

    def _get_config_file_data(self):
        """
        This function reads the wf_config file contenets and converts the string type to JSON (dict)

        Returns:
            data (dict): Contents of the config file

        """
        with open(self.config_file_path) as data_file:
            data = json.load(data_file)
        return data