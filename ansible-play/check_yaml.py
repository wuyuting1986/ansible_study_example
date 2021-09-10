# -*- coding: utf-8 -*-
import yaml
file_path = 'playbook.yml'
file = open(file_path, 'r', encoding='utf-8')
ys = yaml.load(file.read(), Loader=yaml.Loader)
print(ys)
