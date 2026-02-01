# NVIDIA container on Kubernetes

Create a RuntimeClass for nvidia
```bash
kubectl apply -f nvidia-runtimeclass.yaml
```

Deploy the NVIDIA Device Plugin (v0.17.1) as a DaemonSet
```bash
kubectl apply -f nvidia-device-plugin.yml
```

verify
```bash
kubectl describe node $(hostname) | sed -n '/Capacity:/,/Allocatable:/p'
```

should see 
```
  nvidia.com/gpu: 1
```

run test
```bash
kubectl apply -f gpu-test.yaml.yml
````

```bash


kubectl apply -f nvidia-runtimeclass.yaml

kubectl apply -f nvidia-device-plugin.yml

kubectl apply -f gpu-test.yaml.yml

```