import yaml

def read_yaml(path_to_yaml: str) -> dict:
    """
    This function accepts yaml file path and returns content as a dictionary
    parameters : yaml file path -> str
    return : dictionary -> dict
    """
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content
