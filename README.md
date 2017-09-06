# gmq-sine-demo
A simple demo using gmq and gwe.

## How it works

The app itself is a simple While-True loop that sends sinusoidal data to a `sine-data` resource in your Murano device. To accomplish this, the `gwe.build` script creates the `install.sh` and `supervisor.conf` files for GWE and prompts the user for the information required to run the app. The app is started by `supervisord` (the GWE standard way of starting apps).

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

## Add the 'sine-data' Resource

You can manually add a single resource to your Gateway Engine device with the Murano UI, or use the commands, below to add it for you.

```
mr syncup -V --specs
```




