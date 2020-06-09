# Following up the afterglow: strategy for X-ray observation triggered by gravitational wave events

Author: Hui Tong, Mu-Xin Liu, Yi-Ming Hu, Man Leong Chan, Martin Hendry, Zhu Liu, and Hui Sun

## Abstract

The multi-messenger observation of compact binary coalescence promises great scientific treasure. However, a synthetic observation from both gravitational wave and electromagnetic channels remains challenging. Relying on the day-to-week long macronova emission, GW170817 remains the only event with successful electromagnetic follow up.
>We need to find ways to detect GW event by both GW signals and electromagnetic wave signals to achieve real multi-messenger observation.

In this manuscript, <font color=red>we explore the possibility of using the early stage X-ray afterglow to search for the electromagnetic counterpart of gravitational wave events</font>.Two algorithms, **the sequential observation** and **the local optimization** are considered and applied to three simulated events.
We consider the proposed Einstein probe as a candidate X-ray telescope. Benefiting from the large field of view and high sensitivity, we find that the sequential observation algorithm not only is easy to implement, but also promises a good chance of actual detection.
>The early stage X-ray afterglow might be utilised to search for GW events' EM counterparts, and two algorithms are tested. Supposing EP as our detector, we find that the sequential observation algorithm is better.

## 1. Introduction

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

## 2. Statistic framework

In order to optimize the observation strategy, we need to first determine the statistical framework. Since the luminosity of X-ray afterglows changes rapidly, <font color=red>we define the detection as when multiple observations reveals obvious luminosity difference</font>.
>The detection is deined as when the obvious luminousity difference is shown. <br />How obvious???

Throughout the work, we make certain **assumptions**.For example, <font color=red>we assume that the sky position and distance are independent of each other</font>, so that their joint probability distribution is simply the multiplication of each distribution. We also assume that <font color=red>the telescopes can point to any direction</font>, ignoring the potential influence from the Sun, the Moon, and the Earth.
>Several assumptions:<br />1.The sky position and distance are independent of each other, so that their joint probability distribution is simply the multiplication of each distribution.<br />2.The telescopes can point to any direction, ignoring the potential influence from the Sun, the Moon, and the Earth.

We use $D_{ag}$ to denote the successful detection of an afterglow. In order to confirm the existence of afterglow, one need to observe the change of luminosity, so $D_{ag}$ is only defined when multiple observations are finished. The probability of $D_{ag}$ is defined as when the inferred flux has obvious difference, or ∆f >0. We note that the probability of detection $P(D_{ag})$ depends on the field of view (FOV) $\omega$, the observed sky locations ($\alpha, \delta$), and the corresponding exposure time of the multiple observations $\tau_1$ and $\tau_2$. The posterior probability of successful detection can then be given as the probability of one first measure the flux for the first exposure, then observe an obvious change in flux between the two exposures:
$$
P(D_{ag}|\omega,\tau_1,\tau_2,I) =
P(N>N^*|\omega,\alpha,\delta,\tau_1,I) \times P(\Delta f > 0|\tau_1,\tau_2,I)
\tag{1}
$$
>Define the detection probability as the multiplication of the probabilities of a detection of a excess count in the fisrt exposure and a detection of a flux change between two exposures.<br /> ∆f > 0 may be too loose ???

Here,I is prior information that includes the parameters of the selected telescope, such as its photon collecting area A to name one. <font color=red>The threshold count $N^*$ is the criterion for detection determined by the expected signal-to-noise ratio (SNR), the background noise, and the sensitivity of the selected telescope</font>. We adopt the definition of SNR
$$
SNR = \frac{N_{signal}}{\sqrt{N_{noise}}}
\tag{2}
$$

hence, $N^*$ could be expressed as
$$
N^* = SNR \times \sqrt{N_{noise}}
\tag{3}
$$

>The threshold count $N^*$ is the criterion for detection determined by the expected signal-to-noise ratio (SNR), the background noise, and the sensitivity of the selected telescope.

The flux received by the telescope depends on multiple factors. The GW event is localised by GW detectors with uncertainties, and one can assess how likely a certain area contains the GW source. With the knowledge of luminosity and the distance R, one can estimate <font color=red>the distribution of the expected flux, which can be later translated into the distribution of detected photon numbers</font>.  Then the first part of Equation (1) can be expanded as
$$
P(N>N^*|\omega,\alpha,\delta,\tau_1,I) = \int^{\infty}_{N^*} dN \int df \int dR \int_{\omega} d\alpha d\delta \\
\times p(N|f,\tau_1,I)p(f|I,R)p(\alpha,\delta,R|I)
\tag{4}
$$

The quantity $P(N|f,\tau_1,I)$ is the probability of received photons, given the flux $f$ of the source and observation time $\tau_1$, which is described by a Poisson distribution. Since we assume that the prior distribution on the distance to the target afterglow is statistically independent of the prior distribution on its sky location, Equation(4) can be written as
$$
P(N>N^*|\omega,\alpha,\delta,\tau_1,I) = P_{gw}(\omega) \times P_{ag}(\tau_1)
\tag{5}
$$

where
$$
P_{gw}(\omega) = \int_{\omega} p(\alpha,\delta|I) d\alpha d\delta
\tag{6} \\
$$
$$
P_{ag}(\tau_1)=\int df \int dR \int^{\infty}_{N^*} dN \times p(N|f,\tau_1,I)p(f|I,R)p(R|I) \\
= \int df \int^{\infty}_{N^*} dN p(N|f,\tau_1,I) \times \int dR p(f|I,R)p(R|I)
\tag{7}
$$

The first part of Equation (1) only considers single observation. As for the second part of Equation (1),∆f is the different flux of the multiple observations(called $f_1$ and $f_2$) at different moments.  And the $f_1$ and $f_2$ can be approximated by a distribution depending on the prior known flux $f'$, which is based on the afterglow light curve model. The equation of this distribution can be written as
$$
P(f_0|f',\tau)=\sum^{\infty}_{N=0} P(N|f',\tau) \times P(f_0|N,\tau) \\
= \sum^{\infty}_{N=0} P(N|f',\tau) \times \frac{P(N|f_0,\tau) P(f_0)}{\int^{\infty}_0 P(N|f,\tau) P(f) df}
$$

Here P(f)is the prior probability of the flux emitted by afterglow. P(N|f,τ) can be approximated by Poisson distribution. For convenience of description, we refer to the probability in Equation (7) as $P_1$,
$$
P_1 = P_{ag}(\tau_1) = \int df \int dR \int^{\infty}_{N^*} dN \times p(N|f,\tau_1,I)p(f|I,R)p(R|I) \\
= \int df \int^{\infty}_{N^*} dN p(N|f,\tau_1,I) \times \int dR p(f|I,R)p(R|I)
\tag{9}
$$

And the second part in Equation (1) as $P_2$,
$$
P_2 = P(\Delta f > 0|\tau_1,\tau_2,I)
\tag{10}
$$

Thus the Equation (1) could be written as
$$
P(D_{ag}|\omega,\tau_1,\tau_2,I) = P_{gw} \times P_1 \times P_2
\tag{11}
$$

In the Equation (1), we only consider the probability of detecting the afterglow of one observation field.In actual observations, the more likely scenario is that multiple fields would be observed. The total number of fields can be estimated as follows. Assuming that the GW sky localization error region covers $S deg^2$ and the size of the telescope FOV is $\omega deg^2$, the maximum number of fields n can be estimated as $n \lessapprox S/\omega$ in the caseof small FOV.  <font color=red>If a large FOV is considered, more fields than $n' = S/\omega$ may need to be observed due to the GW sky localization error region in the shape of strip</font>. There will even overlap between the fields. **In this article, we mainly consider the situation with a large FOV**.
>The total number of fields needed to be observed for large FOV telescope can be estimated as more than $n' = S/\omega$ due to the GW sky localization error region in the shape of strip.

We will not set a constrained total observation time atfirst, but the observation time do have natural restraint. The luminosity will decrease and when the signal is so small, we can not do a valid observation to achieve the expected SNR any longer. <font color=red>In other words,$P_1$ will not increase at that time. We mark this time as $T_{threshold}$.When the time has exceeded $T_{threshold}$, we no longer consider doing the first time observation for new fields</font>.
>At time $T_{threshold}$, expected SNR can no longer be achieved and $P_1$ can no longer increase with $\tau_1$. So no new fields for the fisrt time observation after $T_{threshold}$.

## 3. Algorithm

### 3.1 Tiliing

There are many methods about skymap tiling. Here we **use greedy algorithm to optimize the tiling** of the observing fields. Firstly, find out the number of <font color=purple>HEALPix</font> that can just meet the required confidence level (in our case we set itto 90%) in order to simplify the calculation. Then, the observation field is divided according to the size of the FOV. <font color=red>Each time, the field with the maximum detection probability will be output and named in order from one to n</font>. Hence their label indicates their rank in terms of enclosed GW probability.
>First, find the HEALPix meeting requiement (find obsering fields?). Greedy algorithm is used to optimized the tiling of observing fields. The output are fields named in order from one to n, ranked by their detection probabilities.<br />What is HEALPix??? HEALPix is an acronym for Hierarchical Equal Area isoLatitude Pixelation of a sphere. As suggested in the name, this pixelation produces a subdivision of a spherical surface in which each pixel covers the same surface area as every other pixel. See `https://healpix.sourceforge.io/`

We use the telescope, Einstein Probe (EP)’s Wide-field X-ray Telescope (WXT module), as an example in our work, and its FOV is about 3600 $deg^2$. Because of the large FOV, the observation field covers a large area around the center point, which means that the area of the observation field may exceed the range previously determined by the 90% confidence level. <font color=red>With the increase in the number n of observation fields, almost all areas of the GW probability distribution would be cov-ered. The sum of $P_{gw}$ of all observation fields may be greater than 90%, and even reach 99% in some events</font>.The result would be shown in Section 4.
>The FOV of EP's WXT is 3600 deg^2. The sum of $P_{gw}$ of all observation fields may be considerable.

### 3.2 Sequential Observation Algorithm

Firstly, we consider a relatively simple algorithm, Sequential Observation Algorithm(SO). As shown in Equation (5), the probability can be separated to two parts, depending on the pointing directions and observation time τ respectively. Then one principle of our observation strategy can be given. As we mentioned before, the label of fields indicates their rank in terms of enclosed GW probability. <font color=red>If we choose to observe a new field,the label of this field must be the smallest among all the fields that never be observed</font>.
>Sequential observation according to the labels of the outpur fields.

We intend to complete the first time observation for as many field as possible until the signal is too weak to achieve the expected SNR. Then, we start the second time observation in the same sequence of fields. As for the time allocation, **we make the shortest step** to change the observation time and comparing the probabilities of each choice. <font color=red>So, considering that there is a slew time interval when making the telescope point at the new field, we compare the increment of $P_1$ when observing more (1 +slewtime) seconds in the old field with the probability of observing 1 seconds in the new field. We continue observing the old field till the the increment of $P_1$ is smaller than the probability of observing a new field</font>. To be fair to compare the difference in the number of photons observed between two observations, we simply adopt the same <font color=purple>time distribution</font> in the second time observation.
>More fields as possible for the fisrt time observation till the SNR falls blow the expected value.<br />Then the second time observation is started with the same sequence, together with a time allocation trick. But why 1 seconds??? How to calculate the $P_1$ of each field???

We can easily find that such a simple algorithm make large $P_1$ for the most fields. We complete the first timeobservation as many fields as possible when the signal isstrong enough. Although when we do the second time observation the signal is weak, what determines $P_2$ indeed is the difference between the two observation signals. That is, no matter how weak the signal is, as long as the intensity of the first observation and the second observation are relatively different, then we will get alarge $P_2$. <font color=red>We can find that getting large $P_1$ and large $P_2$ do not actually conflict, so we believe that this simple but useful algorithm SO will perform well</font>.
>Sequential Observation might get both large $P_1$ and $P_2$.

### 3.3 Local Optimization Algorithm

Here we consider a more complex algorithm, Local Optimization Algorithm(LO), as a comparison.  The <font color=purple>first principle</font> mentioned before is still followed.  <font color=red>And here is another principle that if we choose to observe a field the second time, the label of this field must be the smallest among all the fields that has been observed</font>. Based on these two principles, <font color=purple>we can compare the probability of all choices within the shortest step to optimize the time allocation</font>. The difference from SO is that <font color=red>we can choose to observation the same field for the second time before we finish the first time observation for all fields</font>. This algorithm will get the local optimal result.
>Fisrt principle: If we choose to observe a new field,the label of this field must be the smallest among all the fields that never be observed ???<br />This LO's fist observation is no different with the SO's second observation???

## 4. Results

In this section, we present the performance of our two different algorithms by using the example telescope EP to the follow-up of a few simulated GW events. These events have different error region areas as well as shapes,leading to the distinction of the tiling. We test our algorithms on a couple of simulated events from Singer et al.(2014). <font color=red>Notice that these data were generated assuming the O1 sensitivity, which has already been surpassed by current detectors. The same event is expected to have higher SNR, thus smaller sky localisation error. In order to better mimic the realistic scenario, we manually multiply the distance of every event by a factor of 2</font>. The actual injected distances for our chosen events range from 30Mpc to 100Mpc. However, which we updated to the range of **60Mpc to 200Mpc**
>Use EP to follow up a few simulated GW events, their distance after mannually updated range from 60 Mpc to 200 Mpc.

We use two quite different light curve model respec-tively. The first light curve is shown in Figure 1(a) ,named as GRB Afterglows Model(GAM). It is fit based on the data from `https://www.swift.ac.uk/xrt_curves/`, more details about how the data were produced can be seen in Evans et al. (2007) and Evanset al. (2009). <font color=red>They are detected when compact binaries(NS-NS or NS-BH) merger and we are at the line of sight of the jet (or slightly off-axis)</font>. For later calculation, we fit the binned data with a two-step linear function in logarithmic space.
The second is shown in Figure 1(b) from Sun et al. (2019); Xue et al. (2019), called X-ray Transient Model(XTM) in our work. It may not be related to GRBs. <font>This kind of X-ray transient is produced when binary neutron stars merger and produce a highly-spinning massive neutron star, called magnetar</font>. These X-ray transients are more like isotropic and may be more faint.
So both the X-ray afterglows and the X-ray transients can be observed if the merger leave a magnetar and we are close to the jet direction. But sometimes we can only detect one of them if the two conditions are not satisfied at the same time. But generally both the two types of X-ray emissions can be regarded as the X-ray counterparts of gravitational events. So we work out both of them with our calculations.
![fig](./fig1.png)

### 4.1 Tiling

Figure 2-4 show the optimized tiling of observing fields obtained using the greedy algorithm approach for <font color=purple>three typical events</font>. Although EP’s WXT has such a large FOV about 3600 $deg^2$, the error region in the shape of strip may result in a few observation fields needed to be observed in order to covering as much error region as possible. <font color=red>In our algorithms, we neglect the fields with small probability lower than about 1%</font>. So the required number and location of fields differ for different events. The largest and smallest number of observation fields are 3 and 7. And there exists the difference of total $P_{gw}$ of all fields for different events but less than 3%, which means <font color=red>we will covering error region more than 95% for all events if we finish the detection of all fields except for the neglected ones</font>.

![fig2&3](./fig2&3.png)
![fig4](./fig4.png)

### 4.2 Time Allocation And Observation Sequence

The work flow 5 shows the results of observation sequence for different algorithms **used in four typical events, using GRB Afterglows Model**.
For Local Optimization, the strategy always requires two consecutive observations of the same field, which is determined by two factors. First, local optimization is to consider the effect of both $P_{gw}$ and <font color=purple>$P_{em}$</font>. <font color=red>Since the fields with smaller index are relatively higher in $P_{gw}$, the strategy is more inclined to observe the previous field immediately. Secondly, because it takes a relatively long time to slew the telescope to observe a new field, it also makes the algorithm tend to complete two times of observation in the same field and then perform a new field observation</font>.
For Sequential Observation, the sequence is determined at the beginning, that is, we do the first time observation of all fields in order initially and then the second time observation.
![fig5&6](./fig5&6/png)
>Observation Sequence for SO and LO algorithm.<br />Are these sequences only the fisrt time observation sequences for both algorithm???

Table 1 displays the time allocation. Since the signal is strong enough and we do not need to spend too much time on a very small increase of detection probability,it could be found that the first observation of all fields in Sequential Observation is 1s. That means within a short exposure time, an expected signal-to-noise ratiocan be achieved. For the same consideration, the first time observation for each field does not takes much timeas well in Local Optimization. The second observation time of Sequential Observation is the same as the first observation, so it is fixed in 1s. <font color=red>The second observation time of Local Optimization shows great difference. If the difference of $P_{gw}$ between the former and later fields is not very large and the light curve changes rapidly (which means we will see the brightness differs obviously within a short second observation time), the second observation time may be only 1s. For the period when the difference of  $P_{gw}$ between the former and later fields is relatively larger and the light change is relatively flatter, it will be required to continue the second time observation of the former field even until 220s.</font>
![tab1](./tab1.png)

### 4.3 Multi-sample Events Comparison

Then we will show the results of the simulated X-ray follow-up observations for the multi-sample events, using two algorithms as well as two quite different light curve model respectively.

Firstly we can compare the efficiency of two algorithms in Figure 7. <font color=red>We use the GRB Afterglows Model here</font>. Because the curve has a very bright signal in the early stage, if it can be observed soon after the outburst of GW events, it will be detected successfully without special strategic optimization. In addition, considering that the trigger of GW events and the telescope slewing to the expected position require time, so the initial observation time for strategy optimization of the GRB Afterglows Model is set at 1000s after the event outburst. The figure displays the optimized detection probability corresponding to different 90% error region events, using two algorithms respectively. It can be seen that for the same event, compared with Local Optimization, Sequential Observation can have a significantly higher and more stable probability.
![fig7](./fig7.png)
>For GRB afterglow model, with the observation start time set as 1000s, SO have a significantly higher and more stable probability($P_{gw} \times P_1 \times P_2$) than LO.

There may be some slight fluctuations in the detection probability of Sequential Observation between different events. <font color=red>Because the probability of $P_1$ and $P_2$ in Sequential Observation is close to saturation, that is, both are close to 100%</font>, the fluctuation mainly results from the different $P_{gw}$ of the different events observation region. <font color=red>When the $P_{gw}$ of a new field is too small to observe, we will stop our first time observation and start the second time observation of all fields. There will be a maximum of about 3% change, but it is basically stable above 95%, which is also mentioned above</font>.
> Despite a small fluctuation (at most 3%), the probability of SO is basically stable above 95%.

A trend can also be seen in the figure. <font colot=red>For events with a smaller 90% error region fields, the detection probability of Local Optimization is higher</font>. Smaller 90% error region fields lead to the smaller total observation fields to some extent(In fact, the total observation fields are alsorelated to the size of the field of view and the shape of the 90% error region, so we can see that the fields of the90% error region and the detection probability are notcompletely linearly related).
>For events with a smaller 90% error region fields, the detection probability of Local Optimization is higher.

With smaller observation fields, which means fewer observation fields as well,$P_{gw}$ is more concentrated on the first few observation fields. Therefore, <font color=red>when using Sequential Observation, more observation time can be spent on the first few observation fields with high $P_{gw}$</font>, so that the detection probability in these fields is closer to saturation.
>With smaller observation fields, SO can spend more time on observation fields with high $P_{gw}$.

For events with a large observation field,$P_{gw}$ is distributed in more observation fields, and the difference between the fields is not big enough to tilt the time allocation to fields with high $P_{gw}$ probability, resulting in the failure of the locally optimized observation strategy to concentrate time on a small part area of the high $P_{gw}$. So the larger observation area has a relative disadvantage in the totaldetection probability.
>For large observation field, $P_{gw}$ is dispersed, leading to the failure of the LO strategy to concentrate time on a small part area of the high $P_{gw}$.

In the Figure 8 we also can see that for the events with more observation fields, $P_{em}$ may be smaller than those who have fewer observation fields, leading to the difference in final detection probability. <font color=red>For Sequential Observation, since the second time observation is always made after a fairly long timeinterval, the probability of $P_2$ can always be nearly saturated.</font> So it is only necessary to ensure that the signal is large enough when we are doing the first time observation. Then the probability of the first time observation will be close to saturation, and we can get a good overallobservation probability.
>What is $P_{em}$???<br />After all, it is better to observe as much fields as possible while the signal is still large enough.

![fig8](./fig8.png)

We work our another light curve, the X-ray Transient Model, with our calculations as well. Figure 9 displaythe results. We still get a conclusion basically similarto the GRB Afterglows Model. It shows that under different models, Sequential Observation has shown signif-icantly better results than Local Optimization.
>For X-ray Tranient model, SO is also better than LO.

![fig9](./fig9.png)

We further consider that applying the same strategy,which means the same observation time and observation fields sequence, obtained in the GRB Afterglows Modelto the the X-ray Transient Model. The Sequential Observation still shows its superiority. The detection probability is close to 100%, that is, <font color=red>the total probability is still basically determined by $P_{gw}$ of observed sky area as long as the source is bright enough to finish the first time observation. Local Optimization shows relatively poor results in both different models</font>.

We also compare the results of different models withthe same strategy. The detection probability results of Sequential Observation under different models are basically the same. While using the same strategy givenby Local Optimization in a different model, we get generally lower detection probability. This result actuallyillustrates the strategy based on the local optimization of the detection probability change in the shortest step,depends heavily on the model in the actual calculation. <font color=red>However, Sequential Observation, the strategy of doing the first time observation of all fields initially, can better ensure that the time interval between two observationsof the same field is long enough, and the probability of $P_2$ can be close to saturation. So as long as the signal is not too weak to observe, even for different models,Sequential Observation will give a good detection prob-ability. Therefore, Sequential Observation is not highly dependent on the model.
>SO is not highly dependent on the model. <br />In fact, the principle of SO naturally ensures a high $P_2$ and a high $P_1$.

## Discussion And Conclusion

In this work, we devised and compared two different algorithms to <font color=red>optimize the probability of a successful X-ray afterglow detection triggered by GW alerts</font>. We apply the EP’s WXT as a candidate telescope, which has a large FOV and can get most of the $P_{gw}$ with handful fields. Interestingly, the simpler strategy, or <font color=red>Sequential Observation, which is to finish the first time observation of as many fields as possible initially, constantly outperform the more complicated algorithm.  The results indicates that **multiple observations of the same fields in fairly long time interval** would have better chance to observe the afterglow</font>. We notice that large FOV will be very beneficial for rapid detection of afterglow. Indeed, for the earlier cases, the afterglow is expected to be bright enough that a very short exposure time is sufficient for detection, the majority of time is actually spent on the slew of telescopes.
>Sequential Observation is better, indicating that multiple observations of the same fields in fairly long time interval would have better chance to observe the afterglow.

There are multiple aspects we can further explore.For example:

1. Our threshold for distinguishing the flux change using only the information of integrated photon numbers, while X-ray telescopes can register the arrival time of X-ray photons, which can further help distinguish random fluctuation from actual change of flux.
2. This analysis based on the assumptions of a static telescope with unconstrained pointing and the independence of statistical uncertainty between the distance and the GW trigger sky location.

Space-borne gravitational wave detectors like TianQin has the potential of predicting the merger with very high accuracy, and a co-ordinated observation can better depict the very early stage evolution. All issues can help shape a more realistic and more promising future of successfulmulti-messenger astronomy.

> kind of ignorable

To extend this work, it may be helpful to consider the further constraints that arise from the diurnal cycle,observing time available for afterglows, limitations onthe pointing a particular telescope is capable of, and the rise and set of tiles.
>prospection
