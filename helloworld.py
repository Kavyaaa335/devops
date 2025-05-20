#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
def run_module():
    module_args = dict(
        name=dict(type="str", required=True)
    )
    module = AnsibleModule(argument_spec=module_args)
    result = {
        "changed": False,
        "message": f"Hello, {module.params['name']}!"
    }
    module.exit_json(**result)

if __name__ == "__main__":
    run_module()
