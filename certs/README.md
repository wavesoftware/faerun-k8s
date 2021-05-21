# k8s Root CA

## Tooling

See: https://github.com/cardil/easypki/tree/feature/go-modules

```bash
export PKI_ROOT=$(pwd)
export PKI_ORGANIZATION="Kubernetes @ Suszynski.org"
export PKI_ORGANIZATIONAL_UNIT=IT
export PKI_COUNTRY=PL
export PKI_LOCALITY="Warsaw"
export PKI_PROVINCE="mazowieckie"
```

## CA

```bash
easypki create --ca \
  --expire 7300 \
  --filename root \
  'K8S Suszynski.org Certificate Authority'
```

## Certs

### Kubernetes masters

```bash
easypki create --ca-name root \
  --expire 1825 \
  --dns k8s.suszynski.org \
  --dns kubernetes.suszynski.org \
  --dns kubernetes \
  --dns kubernetes.default \
  --dns kubernetes.default.svc \
  --dns kubernetes.default.svc.cluster \
  --dns kubernetes.default.svc.cluster.local \
  --dns 10.32.0.1 \
  --dns 127.0.0.1 \
  --dns master-1.k8s.suszynski.org \
  --dns master-2.k8s.suszynski.org \
  --dns master-3.k8s.suszynski.org \
  --organization Kubernetes \
  --organizational-unit Kubernetes \
  kubernetes
```

### Admin

```bash
easypki create --ca-name root \
  --expire 1825 \
  --organization system:masters \
  --organizational-unit Kubernetes \
  admin
```

### Kube-Controller-Manager

```bash
easypki create --ca-name root \
  --expire 1825 \
  --organization system:kube-controller-manager \
  --organizational-unit Kubernetes \
  --filename kube-controller-manager \
  system:kube-controller-manager
```

### Kube-Proxy

```bash
easypki create --ca-name root \
  --expire 1825 \
  --organization system:kube-proxier \
  --organizational-unit Kubernetes \
  --filename kube-proxy \
  system:kube-proxy
```

### Kube-Scheduler

```bash
easypki create --ca-name root \
  --expire 1825 \
  --organization system:kube-scheduler \
  --organizational-unit Kubernetes \
  --filename kube-scheduler \
  system:kube-scheduler
```

### Service Account

```bash
easypki create --ca-name root \
  --expire 1825 \
  --organization Kubernetes \
  --organizational-unit Kubernetes \
  --filename service-account \
  service-accounts
```

### Worker nodes

```bash
for i in $(seq 1 6); do
  easypki create --ca-name root \
    --expire 1825 \
    --organization system:nodes \
    --organizational-unit Kubernetes \
    --filename "worker-${i}" \
    --dns "worker-${i}" \
    --dns "worker-${i}.k8s.suszynski.org" \
    "system:node:worker-${i}"
done
```
