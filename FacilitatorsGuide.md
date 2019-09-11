# Intro to IoT, I3, and IOTA Facilitator’s Guide

This document contains MeetUp plans for the MeetUp Series Intro to IoT, I3, and IOTA. This MeetUp Series is designed so that participants learn through experience.  It teaches how to  build simple IoT devices, connect them using the I3 marketplace, store data on the IOTA Tangle, and turn raw data into useful information.
 
### Devices

Participants can choose between four devices.  Using Raspberry Pi components and IOTA tutorials, they can quickly snap together AstroPiOTA and EnviroPhat in order to sense environment data. CO2-TVOC requires wiring and Autonomous Gardener requires soldering, wiring, and connecting more types of components.  

### Software

Participants do not need prior knowledge of Raspbian and Python, but it will be helpful.  The facilitator should have a working knowledge of both in order to troubleshoot and answer questions. 

## What is the learning methodology?

By asking thought provoking questions, the MeetUp facilitator directs participants to discover the IoT, I3, and IOTA technology. This guide includes templates to jumpstart the facilitator in planning their sessions.

# MeetUp 1: Introduce <i>Intro to IoT, I3, and IOTA</i> Meetup Series

This video introduces the vision of [IoT, I3, and IOTA](https://www.youtube.com/watch?v=81rXoSRIRSA&t=11s)

Welcome to an exciting series of meetups to learn, in a hands-on manner, about IoT programming, data marketplaces, and distributed ledger technologies for new mobility and smart city applications.  

This introduction guides you through a series of questions towards discovery of how IoT, I3, and IOTA can benefit you  and which components you should buy in order to build your device.  First, here’s our Code of Conduct, schedule and FAQ.

## Code of Conduct

Everyone is welcome and diversity is encouraged. We are meeting at the USC campus and agree to follow USC code of conduct. I represent the IOTA Foundation. IOTA invents technology for social good and a sustainable economy. IOTA does not license software for military use.

## Schedule

MeetUp 2: Build your IoT device, or use IoT emulator, to collect environment data.  Each device has a tutorial has links to the components you will need.  The emulator is a CSV file with sensor data collected from actual sensors.

MeetUp3: Test your IoT device.  We will work together to make sure everyone has a working device

MeetUp 4: Connect your data to I3

MeetUp 5: Store data on the IOTA Tangle.  By design the I3 Marketplace does not store data.  You can store data in the Tangle.

MeetUp 6: MOBI Month - [Auto Mobility](https://automobilityla.com/)is an important event every November in Los Angeles, so November is “MOBI Month”.  We will work together to learn about platooning and EV charging

MeetUp 7: MOBI Month – invited speaker: Anne Smith, IOTA 

MeetUp 8: into to Data Science for IoT using Kaggle, a data science platform with tools for turning raw data into useful information

MeetUp 9: you will be given an opportunity to showcase your project to industry professionals

## Materials

Python textbook: 	Think Python, How to Think Like a Computer Scientist

Online Tutorials: 	https://github.com/iota-community/I3-IOTA

## FAQ
**Must I attend every session?**
While sessions build on each other, drop-ins are welcome.

**Where do I park?**
______________________

**Is parking validated?**
_________________________

**Must I buy my own device?**
We offer a device emulator in the form of data in a csv file. Owning your device makes it possible for you to continue exploring this technology.

**Can I attend if I don’t know Python?**
Yes, the tutorials include pre-written scripts.

**Will this count towards my IOTA Developers Certificate?**
The IOTA Foundation refers developers to the official certification course. However, you will learn important fundamentals that are key to passing this exam. Participants may want to form study groups to support learning.

## Get started
What is your goal in building an IoT device?

How many have used Raspberry Pi before?

How many have coded in Python?

How many have built a device using sensors?

How can this group help you achieve your goal?

## Why buy and sell data?

Why collect environment data?

Take a look at this [video](https://www.youtube.com/watch?v=81rXoSRIRSA&t=7s)

You may also want to view the [IOTA coffee supply chain video](https://www.youtube.com/watch?v=Gr-LstcDcAw)

How to collect environment data?

## What is IoT?

Show IOTA IoT video:  WhatisIOTA.mp4

Show examples of IoT devices:
		AstroPiOTA, enviroPhat, Autonomous Gardener, CO2-TVOC

https://www.youtube.com/channel/UClxDa0qkOqxIguokXPhnuOA

**What is I3?**

[I3 Consortium](https://i3.usc.edu/about/i3-consortium/)

[IOTA Foundation](https://www.iota.org/)

[IOTA Technical Documentation](https://docs.iota.org/)

**How can we transform raw data into useful information?**

Show www.Kaggle.com website along with AstroPIOTA and CO2-TVOC notebooks

## What components should I purchase to build my device?

Components for each device are listed in the tutorial for that device

# MeetUp 2: Build your IoT device, or use IoT emulator, to collect environment data

Introduce the IoT using this video:  WhatisIOTA.mp4

This is a hands-on working session so you can experience building your own IoT Device.  Let’s take a look at what everyone decided to build.  Did anyone bring a working device?  Please show us how it works.  Any questions?

Let’s get started.  You can work solo or team up. 

IOTA Device Tutorials

http://www.nelsonglobalgeek.com/I3/Phase1/Phase1-Demo.htm

IOTA Emulator Tutorials

Anyone working with the emulator?  Here’s a link to download the emulator data:

(TBD)

# MeetUp 3: Test your IoT device

Show the coffee supply chain video https://www.youtube.com/watch?v=Gr-LstcDcAw&t=4s

Last week, we started building IoT devices. How many have working devices? Who wants to explain how they built their device?

How many have questions?  Why don’t we team up and work together to make sure everyone has a working device so we can buy and sell data together.

When everyone has a working device (or after one hour), ask one or two participants to recap how to build an IoT device. Ask participants to show their data streams.

What are your observations?  Can you see any obstacles for buying and selling data?  How can we share data with all these different formats?

# MeetUp 4: Connect your data to I3

Last week, we finished building our IoT Devices and we talked about how to share data. Tonight, we’re each going to setup a publisher and a subscriber on the I3 Marketplace.  Since we’re talking about pub-sub technology, I’ll show you ZMQ so you can query the Tangle.

Before getting started, consider the format that you will use to send your data.  Here are some examples:   AstroPiOTA, enviroPhat, Autonomous Gardener, and CO2-TVOC. When you have chosen your format, please share it with the group

Here’s the guide for setting up your two accounts.  You will use your publisher account to sell data and your subscriber account to retrieve it.

(Add the new location of I3 Marketplace)

https://github.com/NelsonPython/Connect_IoT_Device_to_I3

https://anrgusc.github.io/iotm/I3_API_Documentation.pdf


Set up products and start buying and selling data.

How did it go?  Were you successful in buying and selling data?  What observations do you have?  When you were a subscriber, did you notice that you have no place to store the data you purchased?  How about storing it on the Tangle?

You can listen as your transactions are published, using ZMQ.  Here’s an example:
https://github.com/NelsonPython/IoT-ZMQ-listener/blob/master/README.md






# MeetUp 5: Store data on the IOTA Tangle
Last week, we bought and sold data. Did you notice that when you bought data, you had no place to keep it? Tonight we will learn how to store data on the IOTA Tangle.  First, I’ll show you where to find our technical documentation

## IOTA Technology

https://www.youtube.com/watch?v=mZSG93W1u7A

https://docs.iota.org/

## PYOTA

Next, I’ll introduce PYOTA.  Follow the Python IOTA Workshop to install pyota and learn how to use the API

https://github.com/iota-community/python-iota-workshop

References:

[Python for Data Scientists](https://www.kaggle.com/learn/python)

## IOTA Device Tutorials

Dive deeper into the code walkthroughs in the tutorials to understand how the devices store data in the Tangle

http://www.nelsonglobalgeek.com/I3/Phase1/Phase1-Demo.htm







# MeetUp 6: MOBI Month

[Auto Mobility](https://automobilityla.com/) is an important conference hosted in Los Angeles every November. So this is “MOBI Month”.  

Jaguar Earn as you drive:  https://www.youtube.com/watch?v=9pzd4MPy1AI

IOTA’s vision:  https://www.youtube.com/watch?v=81rXoSRIRSA&t=11s

During this meetup, the group will work together on a MOBI project. Possible projects include platooning, IOTA EV Charger, buying and selling parking spaces and foot traffic data

[Platooning](https://github.com/NelsonPython/platooning)

EV Charger - coming soon


# MeetUp 7: Invited speaker: IOTA MOBI

Anne Smith, Head of Mobility and Automotive, will speak about IOTA MOBI



# MeetUp 8: Into to Data Science for IoT

Now that we have a number of IoT Devices buying and selling data, how do we turn all this raw data into useful information?

Introduce [Kaggle](https://www.kaggle.com) data science platform and walk participants through two notebooks: AstroPiOTA and CO2-TVOC

[Pandas](https://www.kaggle.com/learn/pandas)
Give an overview of Pandas

Matplotlib
Give an overview of plotting a chart using matplotlib





# MeetUp 9: demo what we learned

We are inviting members of the OMG standards group to see a demo of what we learned. This gives participants an opportunity to showcase their skills to industry professionals.

