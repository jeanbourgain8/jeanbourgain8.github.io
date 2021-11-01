.. title: Audio Drivers Installion
.. slug: audio-drivers-installation
.. date: 2017-11-17 11:06 
.. tags: installation, software, paid
.. category: substack

**Description** : *repairing (installation) audio drivers of Debian PC*

It has been that there is a requirement of 4.11 kernel version for Realtek-ALC1220 to support. So if you too built a your new PC like me then it might be helpful to you for temporary replacement. Uninstall your alsa-base and reinstall latest version it will work fine.

```sh
sudo apt-get remove alsa-base
```

Now go to http://www.stchman.com/tools/alsa/alsa_setup.sh and download the script and then do

```sh
sudo ./alsa_setup.sh
```

This will reinstall the lastest driver in your system and reboots it.
 Precautions if you are having Hybrid Graphics(Intel + Nvidia) then it is suggested to run on Intel HD Graphics and then install. Because this driver is supported for Intel HDA versions if you try to install when you are running in NVIDIA this might cause several failures.
