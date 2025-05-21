# KVM

basic usage:
```bash
virsh list --all
virsh start ubuntu2404
virsh shutdown ubuntu2404
virsh destroy ubuntu2404
```

create vm:
```bash
virt-install \
    --name=ubuntu2404 \
    --memory=8192 \
    --vcpus=4 \
    --os-variant=ubuntu24.04 \
    --cdrom=<image.iso> \
    --disk size=50 \
    --network network=default \
    --graphics vnc,listen=0.0.0.0 \
    --noautoconsole
```

ssh into vm:
```bash
virsh net-dhcp-leases default
ssh <usrname>@<vm-ip>
sudo socat TCP-LISTEN:<port-to-open>,fork,reuseaddr TCP:<vm-ip>

```

snapshot
```bash
virsh snapshot-list ubuntu2404
virsh snapshot-create-as --domain ubuntu2404 --name <snapshotname> --description <comment> --atomic
virsh snapshot-revert ubuntu2404 --snapshotname <snapshotname>
```

change vm setting:
```bash
virsh dumpxml ubuntu2404 > ubuntu2404.xml
virsh define ubuntu2404.xml
```
