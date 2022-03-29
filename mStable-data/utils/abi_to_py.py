import json
import re

from black import format_str, format_file_contents, FileMode

ABIS_PATH = "./mStable-data/abis/"


def camel_to_snake(name):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def abi_to_python(filepath: str):
    new_name = camel_to_snake(filepath[:-5])
    with open(f"{ABIS_PATH}{filepath}", "r+") as abi:
        abi_json = json.loads(abi.read())
        data = {obj["name"]: obj for obj in abi_json if obj["type"] == "event"}
        with open(f"{ABIS_PATH}{new_name}.py", "w+") as abi_python:
            abi_python.write(
                format_file_contents(
                    f"{new_name}_events = {data}",
                    fast=True,
                    mode=FileMode(),
                )
            )


if __name__ == "__main__":
    abi_to_python("FeederPool.json")
    abi_to_python("Masset.json")
    abi_to_python("StakedToken.json")
    abi_to_python("StakedTokenBPT.json")
    abi_to_python("StakedTokenMTA.json")
    abi_to_python("StakedTokenMTA.json")
    
    abi_to_python("EmissionsControllerLogic.json")
