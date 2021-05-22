#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import difflib
import os
import glob
import yaml


def merge_dicts(a, b, path=None):
    "merges b into a"
    if path is None: path = []
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge_dicts(a[key], b[key], path + [str(key)])
            elif a[key] == b[key]:
                pass # same leaf value
            else:
                if isinstance(a[key], list) and isinstance(b[key], list):
                    for i in b[key]:
                        a[key].append(i)
                else:
                    raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
        else:
            a[key] = b[key]
    return a


class YamlMerger:
    data = {}

    def add(self, file: str):
        with open(file, 'r') as stream:
            d = yaml.safe_load(stream)
            self.data = merge_dicts(self.data, d)

    def content(self) -> str:
        return yaml.dump(self.data)


class Input:
    sources: list[str]
    target: str

    def __init__(self, data):
        self.sources = data['sources']
        self.target = data['target']


def merge_yamls(inp: Input) -> tuple[bool, dict]:
    has_changed = False
    diff = None
    existed = file_exists(inp.target)
    sources = collect_sources(inp.sources)
    m = YamlMerger()
    for s in sources:
        m.add(s)
    new_content = m.content()
    if existed:
        old_content = open(inp.target, 'r').read()
        if old_content != new_content:
            has_changed = True
        diff = list(difflib.unified_diff(
            old_content.splitlines(True),
            new_content.splitlines(True)
        ))
    else:
        has_changed = True
    f = open(inp.target, "w")
    f.write(new_content)
    f.close()

    meta = {
        "sources": inp.sources,
        "target": inp.target,
        "existed": existed,
        "diff": diff,
        "cwd": os.getcwd()
    }
    return (has_changed, meta)


def collect_sources(sources: list[str]) -> list[str]:
    collected = set()
    for g in sources:
        files = glob.glob(g)
        for f in files:
            collected.add(f)
    return sorted(list(collected))


def delete(inp: Input) -> tuple[bool, dict]:
    has_changed = False
    existed = file_exists(inp.target)
    if existed:
        os.remove(inp.target)
        has_changed = True

    meta = {
        "target": inp.target,
        "existed": existed,
        "cwd": os.getcwd()
    }
    return (has_changed, meta)


def file_exists(file: str) -> bool:
    try:
        f = open(file)
        f.close()
        return True
    except IOError:
        return False


def main():
    fields = {
        "sources": {"required": True, "type": "list"},
        "target": {"required": True, "type": "str"},
        "state": {
            "default": "present",
            "choices": ['present', 'absent'],
            "type": 'str'
        },
    }
    operations = {
        "present": merge_yamls,
        "absent": delete,
    }

    module = AnsibleModule(argument_spec=fields)
    state = module.params['state']
    inp = Input(module.params)
    op = operations.get(state)
    has_changed, result = op(inp)
    module.exit_json(changed=has_changed, meta=result)


if __name__ == '__main__':
    main()
