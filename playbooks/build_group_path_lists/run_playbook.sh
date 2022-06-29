#!/usr/bin/env bash
ansible-playbook -i ../../local_inventory --vault-password-file ../../volt_piss main.yml