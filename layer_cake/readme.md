# Layer Cake

## 1
```bash
 docker pull anssi/fcsc2024-forensics-layer-cake-1 
 docker history --no-trunc anssi/fcsc2024-forensics-layer-cake-1 | grep FCSC
```

## 2
We are going to look in all the files of the docker image's layers.
```bash
 docker pull anssi/fcsc2024-forensics-layer-cake-2 
 for i in $(docker inspect anssi/fcsc2024-forensics-layer-cake-2 | grep /var/lib/docker | cut -d '/' -f 6) ; do grep -nir FCSC /var/lib/docker/overlay2/$i ; done 
```

## 3 
We are going to use exactly the same strategy, I guess in at least one of the cases something else was expected, but anyway:
```bash
 docker pull anssi/fcsc2024-forensics-layer-cake-3 
 for i in $(docker inspect anssi/fcsc2024-forensics-layer-cake-3 | grep /var/lib/docker | cut -d '/' -f 6) ; do grep -nir FCSC /var/lib/docker/overlay2/$i ; done
```
