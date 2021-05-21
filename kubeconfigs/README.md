# Faerun K8s kubeconfigs

## Worker nodes

```bash
for i in $(seq 1 6); do
  instance="worker-${i}"
  kubectl config set-cluster k8s.suszynski.org \
    --certificate-authority=../certs/root/certs/root.crt \
    --embed-certs=true \
    --server=https://k8s.suszynski.org:6443 \
    --kubeconfig=${instance}.kubeconfig

  kubectl config set-credentials system:node:${instance} \
    --client-certificate=../certs/root/certs/${instance}.crt \
    --client-key=../certs/root/keys/${instance}.key \
    --embed-certs=true \
    --kubeconfig=${instance}.kubeconfig

  kubectl config set-context default \
    --cluster=k8s.suszynski.org \
    --user=system:node:${instance} \
    --kubeconfig=${instance}.kubeconfig

  kubectl config use-context default --kubeconfig=${instance}.kubeconfig
done
```

## kube-proxy

```bash
{
  kubectl config set-cluster k8s.suszynski.org \
    --certificate-authority=../certs/root/certs/root.crt \
    --embed-certs=true \
    --server=https://k8s.suszynski.org:6443 \
    --kubeconfig=kube-proxy.kubeconfig

  kubectl config set-credentials system:kube-proxy \
    --client-certificate=../certs/root/certs/kube-proxy.crt \
    --client-key=../certs/root/keys/kube-proxy.key \
    --embed-certs=true \
    --kubeconfig=kube-proxy.kubeconfig

  kubectl config set-context default \
    --cluster=k8s.suszynski.org \
    --user=system:kube-proxy \
    --kubeconfig=kube-proxy.kubeconfig

  kubectl config use-context default --kubeconfig=kube-proxy.kubeconfig
}
```

## kube-controller-manager

```bash
{
  kubectl config set-cluster k8s.suszynski.org \
    --certificate-authority=../certs/root/certs/root.crt \
    --embed-certs=true \
    --server=https://127.0.0.1:6443 \
    --kubeconfig=kube-controller-manager.kubeconfig

  kubectl config set-credentials system:kube-controller-manager \
    --client-certificate=../certs/root/certs/kube-controller-manager.crt \
    --client-key=../certs/root/keys/kube-controller-manager.key \
    --embed-certs=true \
    --kubeconfig=kube-controller-manager.kubeconfig

  kubectl config set-context default \
    --cluster=k8s.suszynski.org \
    --user=system:kube-controller-manager \
    --kubeconfig=kube-controller-manager.kubeconfig

  kubectl config use-context default --kubeconfig=kube-controller-manager.kubeconfig
}
```

## kube-scheduler

```bash
{
  kubectl config set-cluster k8s.suszynski.org \
    --certificate-authority=../certs/root/certs/root.crt \
    --embed-certs=true \
    --server=https://127.0.0.1:6443 \
    --kubeconfig=kube-scheduler.kubeconfig

  kubectl config set-credentials system:kube-scheduler \
    --client-certificate=../certs/root/certs/kube-scheduler.crt \
    --client-key=../certs/root/keys/kube-scheduler.key \
    --embed-certs=true \
    --kubeconfig=kube-scheduler.kubeconfig

  kubectl config set-context default \
    --cluster=k8s.suszynski.org \
    --user=system:kube-scheduler \
    --kubeconfig=kube-scheduler.kubeconfig

  kubectl config use-context default --kubeconfig=kube-scheduler.kubeconfig
}
```

## admin

```bash
{
  kubectl config set-cluster k8s.suszynski.org \
    --certificate-authority=../certs/root/certs/root.crt \
    --embed-certs=true \
    --server=https://127.0.0.1:6443 \
    --kubeconfig=admin.kubeconfig

  kubectl config set-credentials admin \
    --client-certificate=../certs/root/certs/admin.crt \
    --client-key=../certs/root/keys/admin.key \
    --embed-certs=true \
    --kubeconfig=admin.kubeconfig

  kubectl config set-context default \
    --cluster=k8s.suszynski.org \
    --user=admin \
    --kubeconfig=admin.kubeconfig

  kubectl config use-context default --kubeconfig=admin.kubeconfig
}
```

## Remote kubeadmin

```bash
{
  kubectl config set-cluster k8s.suszynski.org \
    --certificate-authority=../certs/root/certs/root.crt \
    --embed-certs=true \
    --server=https://k8s.suszynski.org:6443 \
    --kubeconfig=kubeadmin.kubeconfig

  kubectl config set-credentials admin \
    --client-certificate=../certs/root/certs/admin.crt \
    --client-key=../certs/root/keys/admin.key \
    --embed-certs=true \
    --kubeconfig=kubeadmin.kubeconfig

  kubectl config set-context default \
    --cluster=k8s.suszynski.org \
    --user=admin \
    --kubeconfig=kubeadmin.kubeconfig

  kubectl config use-context default --kubeconfig=kubeadmin.kubeconfig
}
```
