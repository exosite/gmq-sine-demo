# gmq-sine-demo
A simple demo using gmq and gwe.

## Build
To build the app, run the following command:

```
source gwe.build && gwe_build
```

## Install

Two ways to install. 

### Command-line

Copy the tarball from the build step onto your gateway and install it via `gwe` cli.

```
scp $(source gwe.build && gwe_build) <USER>@<GW_IPADDR>:/tmp
ssh <USER>@<GW_IPADDR> "cd /tmp ; gwe -d DEBUG -I <TARBALL_NAME>"
```

### Over the Air Update/Install

* Upload the content with MrMurano.
* Execute `source gwe.build && deploy_to_gw` and use the JSON output string in the `engine_fetch` alias.