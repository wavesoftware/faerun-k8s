.PHONY: all deploy deploy-masters clean clean-masters

all: deploy

deploy: deploy-masters

deploy-masters:
	ansible-playbook -v -i ansible/inventory ansible/masters.yml

clean: clean-masters

clean-masters:
	for vm in $(shell virsh -c qemu:///system list --name | grep k8s); do \
		virsh -c qemu:///system shutdown $$vm && sleep 1 && \
		virsh -c qemu:///system undefine $$vm && \
		rm -fv /var/lib/libvirt/images/$$vm.qcow2 \
	; done
