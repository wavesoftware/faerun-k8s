.PHONY: all deploy deploy-masters clean clean-masters

all: deploy

deploy: deploy-masters

deploy-masters:
	ansible-playbook -v -i ansible/inventory ansible/masters.yml

clean: clean-masters

clean-masters:
	for vm in $(shell virsh list --name | grep k8s); do \
		virsh shutdown $$vm && sleep 1 && \
		virsh undefine $$vm && \
		rm -fv /var/lib/libvirt/images/$$vm.qcow2 \
	; done
