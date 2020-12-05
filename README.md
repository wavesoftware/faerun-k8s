# Faerun Kubernetes cluster

Cluster is running in premises of WaveSoftware servers as a libvirt 
virtual machines. DNS service is handled outside.

## TODO

### Required

 * [x] Running masters
   * [x] apiserver
   * [x] sheduler
   * [x] controller
   * [x] etcd
   * [x] Certs & Kubeconfigs
 * [ ] Common k8s things
   * [x] container engine
   * [x] kubelet
   * [ ] kube-proxy & cni
   * [ ] dns addon - coredns
 * [ ] Running workers
 * [ ] Storage - Rook & Ceph?!?

### Good to have

 * [ ] Ingress?!?
 * [ ] Migrate project to Terraform
 * [ ] Replace kube-proxy with Cilium

## Resources:

 * https://github.com/kelseyhightower/kubernetes-the-hard-way
 * https://medium.com/containerum/4-ways-to-bootstrap-a-kubernetes-cluster-de0d5150a1e4
 * https://github.com/poseidon/typhoon
 