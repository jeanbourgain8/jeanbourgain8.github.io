---
title: Audio Drivers Installion
slug: audio-drivers-installation
date: 2017-11-17 11:06 UTC+05:30
status: published
tags: [code, system-maintenance, installation, drivers]
category: posts/substack/product
---

> Repairing (installation) Audio Drivers of Debian PC

![](/images/Audio%20Drivers%20Installation.jpg)

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


---
## Subscribe!
If you find the content here helpful/interesting and wish to read more, then _**subscribe**_ to [**Random Product**](https://randomproduct8.substack.com/) to **never miss an update.**

**PS:** Don’t hesitate to comment or leave a **[message](https://twitter.com/jeanbourgain8)**
<div class="row">
	<iframe src="https://randomstack8.substack.com/embed" max-width="480" height="120" frameborder="0" scrolling="no" class="centred"></iframe>
	<br>
</div>