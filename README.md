# gmq-sine-demo
A simple demo using gmq and gwe.

## Build
To build the app, run the following command:

```
gwe --build-app gwe-buildfile.json -d DEBUG
```

## Install

Two ways to install. 

### Command-line

Copy the tarball from the build step onto your gateway and install it via `gwe` cli.

```
scp $(gwe --build-app gwe-buildfile.json) <USER>@<GW_IPADDR>:/tmp
ssh <USER>@<GW_IPADDR> "gwe -d DEBUG -I <TARBALL_NAME>"
```

### Over the Air Update/Install

Upload the content and deploy with MrMurano.

See [docs.exosite.com](docs.exosite.com) for more information about Gateway Engine and Over-the-air-Updates.

## Add the 'test' Resource

```
mr config location.specs specs
mr config product.spec gmq-sine-demo.spec
mr syncup -V --specs
```