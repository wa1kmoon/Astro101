# Following up the afterglow: strategy for X-ray observation triggered by gravitational wave events

Author: Hui Tong, Mu-Xin Liu, Yi-Ming Hu, Man Leong Chan, Martin Hendry, Zhu Liu, and Hui Sun

## Abstract

The multi-messenger observation of compact binary coalescence promises great scientific treasure. However, a synthetic observation from both gravitational wave and electromagnetic channels remains challenging. Relying on the day-to-week long macronova emission, GW170817 remains the only event with successful electromagnetic follow up.
>We need to find ways to detect GW event by both GW signals and electromagnetic wave signals to achieve real multi-messenger observation.

In this manuscript, <font color=red>we explore the possibility of using the early stage X-ray afterglow to search for the electromagnetic counterpart of gravitational wave events</font>.Two algorithms, **the sequential observation** and **the local optimization** are considered and applied to three simulated events.
We consider the proposed Einstein probe as a candidate X-ray telescope. Benefiting from the large field of view and high sensitivity, we find that the sequential observation algorithm not only is easy to implement, but also promises a good chance of actual detection.
>The early stage X-ray afterglow might be utilised to search for GW events' EM counterparts, and two algorithms are tested. Supposing EP as our detector, we find that the sequential observation algorithm is better.

## Introduction

The successful operation of ground-based gravitational wave (GW) detectors like LIGO and Virgo has marked the beginning of a new era ofGW astronomy. Throughout the first to the third observation run of LIGO and Virgo, a series of detection of compact binary coalescence has been made, containing a large variety of features like mass, mass ratio, spin, and distance, etc. Following the excellent traditions of observational astronomy, where the opening of each new observation channel promises great scientific return, the operation of GW observatories greatly deepens our understanding to the most dense objects in the Universe.
>Ignorable.

Apart from the window of GW, other observational channels like electromagnetic (EM), neutrinos and cosmic rays, often referred to as “messengers”, can also be used to study the properties of the underlying sources. The joint force of multi-messenger observation of a specific systems opens an exciting potential for astronomers. The simultaneous optical and neutrino observations of SN1987A set limits to properties of neutrinos. In 2017, the neutrino detector IceCube detected a high-energy neutrino,IceCube-170922A, hinted blazars as possible origin of the high energy neutrinos. The reported flash 0.4 seconds after GW150914 claimed by Fermi GBM triggered huge interests among astronomers. In fact, even prior to the first direct GW event,the non-detection of GW signals could already be used to put constraints on certain sources under the multi-messenger framework, like limiting the origin of GRB070201, or deduce the property of equation of state (EoS).
>Several interesting detected events and implications under Multi-messenger framework: optical and neutrino observations of SN1987A, IceCube-170922A, the reported flash 0.4 seconds after GW150914, limiting the origin of GRB070201...

In 17 August, 2017, the GW signal from a binary neutron star merger was observed as GW170817, and a GRB event GRB170817A was observed simultaneously around the same location. Such simultaneous observations of both GW and EM waves sparked huge interests amongastronomers, leading to a series of scientific discoveries,from confirming the link between short gamma ray burstand binary neutron star merger, to revealing its role in producing heavy elements throughout the Universe.
>Introduction about GW170817.

However, notice that due to the exceptional nature of GRB170817A, which is the closest short GRB detected by human, it is the only event with multi-messenger observations from both GW and EM channels. It is also by far the weakest short GRB in terms of luminosity, No detection of EM counterpart of the next neutron star binary merger event GW190425 was made. The status quo of multi-messenger observation triggered by GW detections reflect its intrinsic difficulty.
>There is difficulty in detecting EM counterparts of GW events. Multi-messenger observations are still seems at arms length.

Although GRBs are powerful sources of light, they are highly beamed. Only those who locate in a small solid angle close to its collimated jet could easily detect it. Detections of gamma rays often come with large uncertainties in their sky locations, therefore, even if the gamma ray burst is detected, the pinpointing of the location or identifying the host galaxy is still a needle-in-a-haystack search. The successful identification of host galaxy for GRB170817A relies on the much later stage emission called kilonova or macronova, where infrared emission powered by decay of radioactive materials produced in the so-called r-process after the binary neutron star merger. Compared with the prompt emission of GRB, macronovae has the advantage of much wider viewing angle, however, it suffers from lower luminosity.
>Because of the collimation nature, GRB detection requires a small viewing angle, though with rather high luminousity. Macronovae has the advantage of much wider viewing angle, however, it suffers from lower luminosity.

In this work, <font color=red>we explore the X-ray afterglow stage of emission, to assist the **rapid localization of a binary neutron star merger**</font>. The X-ray afterglow is expected to happen sooner compared with the macronova, enabling the observation of earlier stage phenomenon. On the other hand, X-ray afterglow can be observed at a larger viewing angle compared with the highly beamed gamma ray emission. More importantly, the duration for gamma ray burst prompt emission is too short to perform target of opportunity observation, while X-ray afterglow can last long enough to perform maneuver triggered by GW alerts.  <font color=red>We aim to study that under the assumption that a trigger from GW observatories has been issued, and no short GRB has been observed, what observation strategy should X-ray telescopes adopts, so that one can increase the chance of observing the EM counterpart and pinpoint its sky location.</font>
>X-ray afterglow happens sooner than the macronava, and has a larger viewing angle and a longer duration than gamma-ray emission. These advantages can be used to make a difference when no short GRB is observed after a GW alert, like increasing the chance of observing the EM counterpart and pinpointing its sky location.

This paper is organized as follows. Section 2 describes the statistical framework we adopt. Section 3 illustrates the two algorithms we uses for the observation strategy. We show the results in section 4, and discuss future work and summary in section 5.

|Sect|content|
|---|---|
|Sect.2|the statistical framework|
|Sect.3|the two algorithms|
|Sect.4|results|
|Sect.5|future work and summary|

## statistic framework
