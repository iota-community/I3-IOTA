# Intro to IoT, I3, and IOTA Facilitator’s Guide

This document contains MeetUp plans for the MeetUp Series Intro to IoT, I3, and IOTA. This MeetUp Series is designed so that participants learn through experience.  It teaches how to  build simple IoT devices, connect them using the I3 marketplace, store data on the IOTA Tangle, and turn raw data into useful information.
 
### Devices

Step-by-step tutorials are provided for four devices.  These devices are built by attaching sensors to a Raspberry Pi.  [AstroPiOTA](https://github.com/NelsonPython/AstroPiOTA) and [EnviroPhat](https://github.com/NelsonPython/EnviroPhat) are easy to build because you snap one component called a "hat" onto the Pi.  [CO2-TVOC](https://github.com/NelsonPython/CO2TVOC) requires connecting a few wires.  [Autonomous Gardener](https://github.com/NelsonPython/AutoGardener) has multiple components with a more complex wiring scheme. 

### Software

Participants do not need prior knowledge of Raspbian and Python, but it will be helpful.  The facilitator should have a working knowledge of both in order to troubleshoot and answer questions. 

## What is the learning methodology?

By asking thought provoking questions, the facilitator directs participants to discover the IoT, I3, and IOTA technology. This guide includes templates to jumpstart the facilitator in planning their sessions.

# MeetUp 1: Introduce <i>Intro to IoT, I3, and IOTA</i> Meetup Series

Watch this video to see the vision of [IoT, I3, and IOTA](https://www.youtube.com/watch?v=81rXoSRIRSA&t=11s)

Welcome to an exciting series of meetups to learn, in a hands-on manner, about IoT programming, data marketplaces, and distributed ledger technologies for new mobility and smart city applications.  

This introduction guides you through a series of questions towards discovery of how IoT, I3, and IOTA can benefit you and which components you should buy in order to build your device.  First, here’s our Code of Conduct, schedule and FAQ.

## Code of Conduct

Everyone is welcome and diversity is encouraged. We are meeting at the USC campus and agree to follow USC code of conduct. I represent the IOTA Foundation. IOTA invents technology for social good and a sustainable economy. IOTA does not license software for military use.

## Schedule

MeetUp 2: Build your IoT device, or use IoT emulator, to collect environment data.  Each device has a tutorial has links to the components you will need.  The emulator is a CSV file with sensor data collected from actual sensors.

MeetUp 3: Test your IoT device.  We will work together to make sure everyone has a working device

MeetUp 4: Connect your data to I3

MeetUp 5: Store data on the IOTA Tangle.  By design the I3 Marketplace does not store data.  You can store data in the Tangle.

MeetUp 6: MOBI Month - [Auto Mobility](https://automobilityla.com/) is an important event every November in Los Angeles, so November is “MOBI Month”.  We will work together to learn about platooning and EV charging

MeetUp 7: Introduction to Data Science for IoT using Kaggle, a data science platform with tools for turning raw data into useful information

MeetUp 8: Participants will be given an opportunity to showcase your project to industry professionals

## Materials

[Learn Python playlist](PythonPlaylist.md)

IOTA Tutorials: 	https://github.com/iota-community/I3-IOTA

Raspberry Pi Tutorials:  https://tutorials-raspberrypi.com/

Sense Hat Tutorial:  https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat

Kaggle Data Science Micro Courses:  https://www.kaggle.com/learn/overview

## FAQ

**Must I attend every session?**
While sessions build on each other, drop-ins are welcome.

**Must I buy my own device?**
We offer a device emulator in the form of data in a csv file. Owning your device makes it possible for you to continue exploring this exciting technology.

**Can I attend if I don’t know Python?**
Yes, the tutorials include scripts

**Will this count towards my IOTA Developers Certificate?**
The IOTA Foundation refers developers to the official certification course. However, you will learn important fundamentals that are key to passing this exam. Participants may form study groups.

## Getting started
What is your goal in building an IoT device?

How many have used Raspberry Pi before?

How many have coded in Python?

How many have built a device using sensors?

## Introducing I3 and IOTA

[I3 Consortium](https://i3.usc.edu/about/i3-consortium/)

[IOTA Foundation](https://www.iota.org/)

[IOTA Technical Documentation](https://docs.iota.org/)

Introduce the www.Kaggle.com website along with AstroPIOTA and CO2-TVOC notebooks


## Why buy and sell data?

Why collect environment data?

Let's revisit our [video of what is possible in the future](https://www.youtube.com/watch?v=81rXoSRIRSA&t=7s)


## What is IoT?

Show IOTA IoT video:  WhatisIOTA.mp4

[AstroPiOTA](https://github.com/NelsonPython/AstroPiOTA), [EnviroPhat](https://github.com/NelsonPython/EnviroPhat) are easy to build because you snap one component called a "hat" onto the Pi.  [CO2-TVOC](https://github.com/NelsonPython/CO2TVOC) requires connecting a few wires.  [Autonomous Gardener](https://github.com/NelsonPython/AutoGardener) has multiple components with a more complex wiring scheme.  The [IOTA YouTube channel](https://www.youtube.com/channel/UClxDa0qkOqxIguokXPhnuOA) has more examples. 

## What components should I purchase to build my device?

Components for each device are listed in the tutorial for that device

# MeetUp 2: Build your IoT device, or use IoT emulator, to collect environment data

Introduce the IoT using this video:  WhatisIOTA.mp4

This is a hands-on working session so you can experience building your own IoT Device.  Let’s take a look at what everyone decided to build.  Did anyone bring a working device?  Please show us how it works.  Any questions?

Let’s get started.  You can work solo or team up. 

#### IOTA Device Tutorials

https://github.com/iota-community/I3-IOTA/blob/master/README.md

#### IOTA Emulator Tutorials

Anyone working with the emulator?  Here’s a link to download the emulator data:

https://github.com/iota-community/I3-IOTA/tree/master/data

# MeetUp 3: Test your IoT device

Show the [IOTA coffee supply chain video](https://www.youtube.com/watch?v=Gr-LstcDcAw) as another example of connected IoT devices

Last week, we started building IoT devices. How many have working devices? Who wants to explain how they built their device?

How many have questions?  Why don’t we team up and work together to make sure everyone has a working device so we can buy and sell data together.

When everyone has a working device (or after one hour), ask one or two participants to recap how to build an IoT device. Ask participants to show their data streams.

What are your observations?  Can you see any obstacles for buying and selling data?  How can we share data with all these different formats?

# MeetUp 4: Connect your data to I3

Last week, we finished building our IoT Devices and we talked about how to share data. Tonight, we’re each going to setup a publisher and a subscriber on the I3 Marketplace.  Since we’re talking about pub-sub technology, I’ll show you ZMQ so you can query the Tangle.

Before getting started, consider the format that you will use to send your data.  Here are some data format examples:   

- <a  class="w3-btn" href="https://devnet.thetangle.org/address/ZNJWDJBGQVLCNJIRXPDUKHESBYXGFADCKAUCXFZFCWEOUJOJIDZHDCMVQQTEMZIMPOXFCTM9QSNNUZVBX">AutoGardener</a>

- <a  class="w3-btn" href="https://devnet.thetangle.org/address/VFMEYGUNJVBMRFORVRIOHVET9L9A9AJFCETCOEVI9WPJPRWWALLOBFLXQGGHTZWQKTBJELJNVA9SILXVZTMPMXKPWC">AstroPiOTA</a>

- <a  class="w3-btn" href="https://devnet.thetangle.org/address/K9LYCBRIBMKPDPMDPTJSQTCXYVPBULSIRQZJEHINYQXBYNFCFSWUXIMXELKTGXCZLYDZNDJEVKSOBWDXXTTNMMPRPC">CO2-TVOC</a>

- <a  class="w3-btn" href="https://devnet.thetangle.org/address/ORTP9BWTENDHERKNXRHRN9CAYPWSUXDPUZGFJVV9APCWORUFSE9N9OQYBSJEQAIBHJSWBIGFNQUDT9IUWBBPUYLAHB">EnviroPhat</a>

Here’s the link to the I3 Marketplace plus a tutorial and the API guide:  

[Connect an IoT Device to I3 Tutorial](https://github.com/NelsonPython/Connect_IoT_Device_to_I3)

[I3 Marketplace](http://3.15.198.123:8000/)

[I3 API Documentation](https://anrgusc.github.io/iotm/I3_API_Documentation.pdf)

You will use your publisher account to sell data and your subscriber account to retrieve it.

Set up products and start buying and selling data.  

How did it go?  Were you successful in buying and selling data?  What observations do you have?  When you were a subscriber, did you notice that you have no place to store the data you purchased?  How about storing it on the Tangle?

Using ZMQ, you can listen as your transactions are published to the Tangle.  Here’s an example:
https://github.com/NelsonPython/IoT-ZMQ-listener/blob/master/README.md



# MeetUp 5: Store data on the IOTA Tangle
Last week, we bought and sold data. Did you notice that when you bought data, you had no place to keep it? Tonight we will learn how to store data on the IOTA Tangle.  First, here's the technical documentation for IOTA

## IOTA Technology

[IOTA docs video](https://www.youtube.com/watch?v=mZSG93W1u7A)

[IOTA docs](https://docs.iota.org/)

## PYOTA

Next, I’ll introduce PYOTA, the IOTA Python client library.  Follow the installation instructions to install pyota and learn how to use the API

https://github.com/iota-community/python-iota-workshop

If you are new to Python, here's the Ultimate Python Learner's Playlist:

http://www.nelsontech.blog/Tutorial-Python/PythonPlaylist.htm

# MeetUp 6: MOBI Month

[Auto Mobility](https://automobilityla.com/) is an important conference hosted in Los Angeles every November. So this is “MOBI Month”.  Take a look at a [new Jaguar Landrover where you can earn iota tokens while you drive](https://www.youtube.com/watch?v=9pzd4MPy1AI)  

Check out [IOTA’s vision for a future of mobility](https://www.youtube.com/watch?v=81rXoSRIRSA&t=11s)

During this meetup, the group will work together on a MOBI project. Possible projects include platooning, IOTA EV Charger, buying and selling parking spaces and foot traffic data

 - [Platooning tutorial](https://github.com/NelsonPython/platooning)

 - EV Charger - coming soon


# MeetUp 7: Invited speaker: IOTA MOBI

Anne Smith, Head of Mobility and Automotive, will speak about mobility



# MeetUp 8: Into to Data Science for IoT

Now that we have a number of IoT Devices buying and selling data, how do we turn all this raw data into useful information?

Introduce [Kaggle](https://www.kaggle.com) data science platform and walk participants through two notebooks: AstroPiOTA and CO2-TVOC

Give an overview of [Pandas](https://www.kaggle.com/learn/pandas), the data analysis library

Give an overview of plotting a chart using matplotlib





# MeetUp 9: demo what we learned

We are inviting members of the OMG standards group and the I3 Consortium to see a demo of what we learned. This gives participants an opportunity to showcase their skills to professionals.

