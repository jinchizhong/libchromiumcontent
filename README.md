# libchromiumcontent

Automatically builds and provides prebuilt binaries of the [Chromium Content
module](http://www.chromium.org/developers/content-module) and all its
dependencies (e.g., Blink, V8, etc.).

## Development

### Prerequisites

* [Linux](https://chromium.googlesource.com/chromium/src/+/master/docs/linux_build_instructions_prerequisites.md)
* [Mac](https://chromium.googlesource.com/chromium/src/+/master/docs/mac_build_instructions.md#Prerequisites)
* [Windows](https://chromium.googlesource.com/chromium/src/+/master/docs/windows_build_instructions.md)

### One-time setup

    $ script/bootstrap

### Building

    $ script/update -t x64
    $ script/build -t x64

### Updating project files

If you switch to a different Chromium release, or modify
files inside the `chromiumcontent` directory, you should run:

    $ script/update

This will regenerate all the project files. Then you can build again.

### Building for ARM target

> TODO: This section may be out of date, needs review

```bash
$ ./script/bootstrap
$ ./script/update -t arm
$ cd vendor/chromium/src
$ ./build/install-build-deps.sh --arm
$ ./chrome/installer/linux/sysroot_scripts/install-debian.wheezy.sysroot.py --arch=arm
$ cd -
$ ./script/build -t arm
```

### build on \*BSD

I'm sorry, but I have already done my best. Cause of too complex cross dependencies, building libchromiumcontent on \*BSD is really complex.

1. Install ports tree

If you already have ports tree, you can skip this step.

    # [ -d /usr/ports ] || ( portsnap fetch && portsnap extract )

2. Install all dependencies of www/chromium or make www/chromium first

    # cd /usr/ports/www/chromium
    # make BATCH=1

BTW: this may take a lot of time, you can run `pkg install chromium` first to save your life.

3. Bootstrap source

    $ cd path_of_this_project
    $ ./script/bootstrap

4. Configure

    $ ./script/update

5. Build

    $ ./script/build

If you are being asked type root password during update or build. This means you are missing some of dependencies.
Please press ^C, and goto step 2.
