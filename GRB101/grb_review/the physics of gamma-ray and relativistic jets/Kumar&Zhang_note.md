# The Physics of Gamma-Ray Bursts &Relativistic Jets

[1.Introduction](#sect1)
[2.Raiative processes](#sect2)
[3.Afterglow theory](#sect3)
[4.Afterglow observations and interpretations](#sect4)
[5.Collisionless shock properties from GRB afterglow observations](#sect5)
[6.Observational properties of GRB prompt radiation](#sect6)

<div id='sect1'></div>
## 1. Introduction

- GRBs are irregular pulses of gamma-ray radiation
- Gamma spectrum: non-thermal (broken power law), peaking at ~10-10e4keV
- Connected to SN and possibly BH formation
- Isotropic radiated energy: 10e48 - 10e55erg
- Afterglow: power-deacy light curve & power-law decay spectrum
- External forward shock (synchrotron radiation) could be the origin of afterglow
- The decay of the light curve steepenning to ~-2.2 at ~1day after, which is called "jet break", is due to the collimated narrow jets.
- The initial opening angle and its kenetic energy can be obtained by modelling the broadband emission (radio to X-ray) of those afterglows' light curves with a jet break
- The opening angle is in the range of ~2-10 degrees.
- thus the true amount of energy released in most long GRBs is reduced by a factor of ~10e2 -10e3, which indicates that their radiated energy is 10e49 ~ 10e52 erg.
- The density of the medium within ~0.1pc of the burst is found to be uniform and is of the order of a few protons, which is different to the decreasing density that decreases as r^-2 due to the wind from the progenitor star, which is expected by the core collapse of the massive star model.
- GRB outflows are hightly relativistic.
- GRBs are typically found to be in star forming regions of their host galaxies, which can partly indicate the association between long GRBs and core collapse SNe.
- A fraction of sGRBs are located in elliptical galaxies, i.e. associated with older stellar population, and they're tend to be less energitic and at a lower redshift. These are consistent with the idea that sGRBs originate from neutron stars mergers which however is not conclusive yet.
- XRT found that for about half of GRBs the X-ray flux decays rapidly after the burst (t^-3), followed by a much slower decay (t^-1/2) than expected in the standard FS model. The former indicates that the prompt radiation and afterglows arises from different machanisms.
- The X-ray flux of some GRBs would sharply increase (flares) minutes to hours after the end of the GRB, suggesting that the central engine of these bursts is active for a longer time than the burst duration.
- The X-ray and optical light curves after 10^4s are however consistent with external forward shock emission. Thus the X-ray data prior to ~10^4s are not well understood.
- Achromatic breaks (associated with finite jet angle) are seen in some burst but not others.
- prompt γ-ray emission: internal shock? external shock model? other mechanisms?
- γ photons: synchrotron process? inverse compton process? other mechanisms?
- relativistic jet: baryonic matter? electron-positron pairs? energy in magnetic fields?

<div id='sect2'></div>
## 2. Radiative processes

- synchrotron process
- inverse-Compton process
- photo-pion proccess
- few basic relativity results

### 2.1 Photon arrival time from a moving source, Doppler shift, Lorentz invari-ance of power etc.

Suppose:

---

$v$ : source moving speed (lab frame)

$\nu'$ : the photon frequency in the observer frame

$\Gamma$ : Lorentz factor

$\theta$ : angle between moving direction and the line of sight

$\delta t'$ : time interval between two emitted photons in the **comoving frame**

---

then we have:

---

$\delta t$ : time interval between two emitted photons in the **lab frame**

$$\delta t=\Gamma \delta t'$$

$\delta t_{obs}$ : time interval of the arrival of these photons at the observer

$$\delta t_{obs}=\delta t' \Gamma(1-vcos\theta/c)=\delta t'D^{-1} = \delta t/(\Gamma D) \tag{1}$$

where $D$ : the Doppler factor

$$D=[\Gamma(1-vcos\theta/c)]^{-1} \tag{2}$$

>I ponder that redshift $z = D^{-1} -1$

For $\theta << 1$ and $\Gamma >>1$, $\delta t_{obs}$ can be approximted as:

$$\delta t_{obs}\approx\frac{\delta t'}{\Gamma}[1+(\theta\Gamma)^{2}/2]=\frac{\delta t}{\Gamma^{2}}[1+(\theta\Gamma)^{2}/2] \tag{3}$$

>1.How's that? Clues: $cos\theta \approx 1 - \theta^2/2$, and $v/c \approx 0$
>2.This approximation indicates that $D^{-1} \approx \Gamma^{-1}$ when $\theta$ is so small that $(\theta \Gamma)^2 \approx 0$

$\nu$ : the photon frequency in the observer frame(**standard Doppler shift formula**)

$$\nu=\frac{\nu'}{\Gamma(1-vcos\theta/c)} \equiv \nu'D \tag{4}$$

---

<center>
<img src="./arrival_time.png" height=100% width=100%>
</center>

### 2.1.1 Relativistic beaming of photons

For large $\Gamma$:

$$\theta \approx \theta' / \Gamma$$

which means, photons are focused in the farward direction, the angular size of the photon beam in the lab($\theta$) is smaller than it is in the comoving frame($\theta'$) by a factor ~ $\Gamma$. The solid angle for a conical beam in lab frame is thus smaller than in the comoving frame by a factor ～ $\Gamma^2$.

A mroe precise expression for Lorentz transformation of solid angle is:

$$d\Omega = d\Omega' / D^2$$

Besides, the power readiated by a particle is **Lorentz invariant** when the radiation beam is symmetric under parity transformation in particle rest-frame.

>Power is defined as the frequency integrated total energy radiated per unit timeover 4π steradians.

### 2.1.2 Transformation of specific luminousity and specific intensity

Specific luminousity:

Consider a source that is spherically symmetric and is expanding with Lorentzfactor $\Gamma$, we have:

$$L_\nu = \frac{dE}{d\nu dt_{obs}} = \Gamma \frac{dE'}{d\nu' dt'} = \Gamma L_\nu'$$

where $L_\nu$ is the total energy that flows through a surface enclosing the source per unit time and frequency.

Specific intensity is defined as flux per unit frequency and per unit solidangle carried by photons traveling within a narrow conical beam with its axisperpendicular to surfacedA, i.e.

$$I_\nu \equiv \frac{dE}{d\nu dt_{obs} dA d\Omega}$$

and

$$I_\nu = D^3 I_\nu'$$

#### 2.1.3 Observed lightcurve from a source that is suddenly turned off (???,see Page 16)

<center>
<img src="./various_angles.png" height=100% width=100%>
</center>

Suppose that the intrinsinc spectrum is $I'_{\nu'} = I' \nu'^{-\beta}$, we have:

$$f_\nu (t_{obs}) \propto (1-vcos\theta_t/c)^{2+\beta} \nu^{-\beta} \propto t_{obs}^{-(2+\beta)} \nu^{-\beta}$$

## 2.2 Synchrotron radiation

Consider:

An electron (Lorentz factor $\gamma_e$, speed $v_e$) moves perpendicular to the magnetic field B. The electric field in the electron rest fram is $E=\gamma_e v_e B/c$.

Hence according to Lamor's formula, the power radiated due to electron acceleration in this electric field is:

$$P_{syn} = \frac{2 q^4 E^2}{3 c^3 m_e^2} = \frac{2 q^4 B^2 \gamma_e^2 v_e^2}{3c^5 m_e^2} = \sigma_T B^2 \gamma_e^2 v_e^2/(4\pi c) \tag{15}$$

where $\sigma_T = 8\pi q^4/(3m_e^2 c^4)$ is the Thomson cross section. Again, this power is a Lorentz invariant quantity, so the synchrotron power in the lab frame is the same.

---

The Larmor frequency of the electron (or its angular speed) is

$$
\omega_L = \frac{qB}{\gamma_e m_e c} \tag{16}
$$

Due to relativistic beaming, a distant observer can only receive those photons which are emitted when the electron velocity lies within an angle $\gamma_e^{-1}$ of the observer's line of sight.

<center>
<img src="./relativistic_beaming.png" height=100% width=100%>
</center>

Hence the fraction of orbital time during which we can receive photons is $\sim 2\gamma_e^{-1}/ 2\pi$, and therefore the duration of the radiation pulse received by observer $\delta_{obs}$ in each oribit is:

$$
\delta t_{obs} \sim \frac{2}{\gamma_e \omega_L} \frac{1}{2\gamma_e^2} \sim \frac{m_e c}{qB\gamma_e^2} \tag{17}
$$

>Notice the relation between comoving time $\delta t'$ and observer frame time $\delta t_{obs}$ for photon arrival. But why there are three $\gamma_e$ in the denominater? I ponder there should be only two: one from the orbital fraction and one from the transform from comoving time to observer time. The '2' in the denomoinater also confuses me.

The inverse of this time is the characteristic frequency for synchrontron radiation:
$$
\omega_{syn} \sim \frac{qB\gamma_e^2}{m_e c}
\ \ \ \ and \ \ \ \  
\nu_{syn} = \frac{\omega_{syn}}{2\pi} \sim \frac{qB\gamma_e^2}{2\pi m_e c}
\tag{18}
$$

A more precise treatment has an additional factor (3/2)sin$\alpha$; $\alpha$ is the pitch angle between the electron’s velocity and themagnetic field.

>This is to say each electron with a specific $\gamma_e$ has a correponding characteristic frequency $\nu_{syn}$ at which the flux from this electron peaks in its spectrum.

The synchrotron spectrum peaks at $\sim \nu_{syn}$.**The spectrum below the peak scales as $P_{syn}(\nu) \propto \nu^{1/3}$, and it declines exponentially for frequency higher than $\nu_{syn}$**.

<center>
<img src='./synchrotron_spec.png' height=100% width=100%>
</center>

Refering to Rybicki and Lightman (1979), the power per unit frequency $P_{syn}(\nu)$ at the peak of the spectrum is
$$
P_{syn}(\nu_{syn}) \sim P_{syn} / \nu_{syn} \sim \frac{\sigma_T B m_e c^2}{2q}
\tag{19}
$$

Given a power-law ditributed of electrons, $dn_e / d\gamma_e \propto \gamma_e^{-p}$, we then can calculate synchrotron spectrum (the flux at given $\nu$) by adding up contributions from those electrons with LF larger than (see 18)
$$
\gamma_\nu \sim (\frac{2\pi \nu m_e c}{qB})^{1/2}
\tag{20}
$$
resulting in
$$
f_\nu = \int_{\gamma_e}^\infty d\gamma_e \frac{dn_e}{d\gamma_e} P_{syn}(\nu) \propto \nu^{-(p-1)/2}
\tag{21}
$$

>I deem the reason that adding up electrons larger than $\gamma_e$ is that this fraction of electrons dominates the flux at $\nu_e$ corresponding to the $\gamma_e$, since the flux from electrons smaller than $\gamma_e$ is already declining rapidly at  $\nu_e$.<br />Besides, eq.21 indicates that the flux also depends on the energy distribution of electrons.

Conclusion:The synchrotron spectrum for a power-law distribution of electrons,$dn_e / d\gamma_e \propto \gamma_e^{-p}$, is $f_\nu \propto \nu^{-(p-1)/2}$.

### 2.2.1 Effect of synchrotron cooling on electron distribution

Consider that after being accelerated at some time, electrons then cool via synchrotron radiation for time duration $t_0$. Electrons with LF $\gtrsim \gamma_c$ (defined below) lose a significant fraction of their energy during this time and their LF drops below $\gamma_c$
$$
\frac{dm_e c^2 \gamma_e}{dt}=-\frac{\sigma_T}{6\pi}B^2 \gamma_e^2 c
\ \ \ \ or \ \ \ \ 
\gamma_c \sim \frac{6\pi m_e c}{\sigma_T B^2 t_0}
\tag{22}
$$

> This is to say, there exists an $\gamma_c$ which is inversly proportional to $B^2$ and $t_0$ (which means that $\gamma_c$ is only related to the environment), and electrons bigger than this $\gamma_c$ would lose most energy due to synchrotron radiation.

Then we have another characteristic synchrotron frequency （cooling frequency） corresponding to this $\gamma_c$(see eq.18):
$$
\nu_c \equiv \frac{3qB\gamma_c^2}{4\pi m_e c} \sim \frac{27\pi q m_e c}{\sigma_T^2 B^3 t_0^2}
\tag{23}
$$

>What can we learn from the above?<br />1. This cooling frequency is then also depend on the environment. If this frequency can somehow be measured, maybe the properies of the environment can thus be derived.<br />2. As the LF drops below $\gamma_c$, the 'peak frequency' $\nu_e$ also drops below $\nu_c$.

The effect of the cooling of electrons is that as a result of loss of energy, the electron distribution function for $\gamma_e > \gamma_c$ is modified,leading to that the power-law index of the spectrum would changes at $\nu_c$.

This can be seen from the continuity equation for elctrons in the energy space:
$$
\frac{\partial}{\partial t} \frac{dn_e}{d\gamma_e} + \frac{\partial}{\partial \gamma_e}[\dot{\gamma_e} \frac{dn_e}{d\gamma_e}]=S(\gamma_e)
\tag{24}
$$

where $\dot{\gamma_e} = -\sigma_T B^2 \gamma_e^2 / (6\pi m_e c)$ is the rate of change of $\gamma_e$ due to the synchrotron loss, and $S(\gamma_e)$ is the rate at which electrons with LF $\gamma_e$ are injected into the system.

>Note that $\dot{\gamma_e}$ is due to synchrotron loss (cooling effect), so the solution of this equation is the electron distribution that has been modified due to cooling effect.

This equation has a steady state solution ($\partial / \partial t=0$) for **time independent magnetic field** which is: $dn_e/d\gamma_e \propto \dot{\gamma_e}^{-1} \propto \gamma_e^{-2}$ (i.e. p=2) for $\gamma_c < \gamma_e < \gamma_m$; where $\gamma_m$ is the minimum LF of injected electron so that $S(\gamma_e)=0$ for $\gamma_e < \gamma_m$. The specctrum corresponding to this segment of electron distribution is $f_\nu \propto \nu^{-1/2}$.

For $\gamma_e > \gamma_c > \gamma_m$, the solution of the continuity equation is $dn_e/d\gamma_e \propto \gamma_e^{-p-1}$ in the steady state (for constant B), the corresponding spectrum is $f_\nu \propto \nu^{-p/2}$.

### 2.2.2 Synchrotron self-absorption frequency

There is yet another characteristic frequency, $\nu_a$, which corresponds to the case where absorptions of photons by the inverse-synchrotron process (???) becomes important.

The easiest way to determine $\nu_a$ is by the application of Kirchhoff's law - the emergent specific flux cannot exceed the black body flux corresponding to the appropriate electron electron temperature which is
$$
k_B T \approx max(\gamma_a, min[\gamma_m, \gamma_c])m_e c^2/2.7
\tag{25}
$$

The synchrotron self-absorption frequency ($\nu_a$) is the frequency where the emergent synchrotron flux is equal to the black-body flux (???) :
$$
\frac{2m_e c^2 max(\gamma_a, min[\gamma_m, \gamma_c])\nu_a^2}{2.7c^2}
\approx \frac{\sigma_T B m_e c^2 N_{\gt}}{4\pi q}
\tag{26}
$$

where the left side of this equation is the Plank function in the Ratleign-Jeans limit, and $N_>$ is the column density of electrons with LF larger than max($\gamma_a$, min[$\gamma_m, \gamma_c])$.

The  emergent  synchrotron  spectrum  for  a  distribution  of  electrons  dependson the ordering of these characteristic frequencies. Spectra for two particularorderings are shown below.

<center>
<img src="./synchrotron_complete_spectrum.png"
height=100% width=100%>
</center>

### 2.2.3 Maximum energy of synchrotron photons

Charged articles are accelerated as they travel back and forth across a shock front via the fist order Fermi process.

They gain energy by a factor ~ 2 each time they are scattered from one side to the other of a relativistic shock front.

The maximun synchrotron frequency for an eletron in this case turns out to be about 50$\Gamma$ MeV, and for a proton it is a factor $m_p/m_e$ larger. $\Gamma$ is the LF of shocked plasma with respect to the observer.

>How does thit come about? Answer is as follows.

The minimum time required for acceleration of a charged particle of mass m while crossing a shock front is of the order of the Larmor time $t_L' = mc\gamma / (qB')$, where $\gamma$ is LF of the partical in the shock comoving frame, and prime (') refers to quantity measured in the rest frame of the shocked fluid.

>This is to say if the particle wants to have a LF up to $\gamma$, then the minimun time that it will need is $t_L' = mc\gamma / (qB')$

The particle should not lose more than half its energy to synchrotron radiation $t_L'$, otherwise it will ever  get accelerated to LF $\gamma$.

> This means that we could wirte an inequality like: <br />radiation power x ($t_L'$) < half of the particle energy

This implies that
$$
\frac{4q^4 B^{'2} \gamma^2}{9m^2 c^3} t_L' < \frac{mc^2 \gamma}{2}
$$

use $t_L' = mc\gamma / (qB')$, we get:
$$
\frac{qB' \gamma^2}{2\pi mc} < \frac{9mc^3}{16\pi q^2}
$$

The left side of this equation is the synchrotron frequency of particle with LF of $\gamma$. Thus we can use this inequality to find the maximun synchrotron photon energy for an electron (proton) is ~50 MeV  (100GeV) in shocked fluid comoving frame under the optimistic Bohm diffusion limit.

Synchrotron photons produced when a particle is passing through a region of muchhigher-than-average magnetic field can have energy larger than the limit de-scribed above, e.g. Kumar et al. (2012).

## 2.3 Inverse-Compton radiation

When a photon of frequency $\nu$ is scattered by an electron of larger energy, the photon gains energy in this process on the average. If the electron LF is  $\sim \gamma_e$, and $h\nu' = h\nu \gamma_e \ll m_e c^2$, then the average frequency of scattered photon is $\nu_s \sim \nu \gamma_e^2$, which is that the frequency, thus the energy, of the incident photon boost by a factor of $\gamma_e^2$.

Consider next an electron moving through a radiation field where the energy density in photons is $u_{\gamma}$ (namely, the energy density of the synchrotron radiation energy). The power in IC-scattered photons, $P_{ic}$,subsequently follows from the boost of energy for each photon by a factor of $\gamma_e^2$ (independent of photon energy far the case where $h\nu \gamma_e \ll m_e c^2$ as is being considered here.):
$$
P_{ic} \sim \sigma_T \int d\nu \frac{u_{\nu}c}{h\nu} h_{\nu} \gamma_e^2 \sim \sigma_T u_{\gamma} \gamma_e^2c
\tag{27}
$$

where $u_{\nu}d\nu$ is energy density in photons of frequency between $\nu$ and $\nu+d\nu$ (namely $u_{\gamma} = \int u_{\nu}d\nu$).

>Eq.27 indicates that $P_{ic}$ depends only on the environment and the electron energy ($P_{ic} \propto u_{\gamma}, \gamma_e^2$) under the reqired condition.

We see from eaqutions (15) and (27) that the ratio of synchrtron and IC powers is $u_B/u_{\gamma}$; where $u_B = B^2 / 8 \pi$ is the energy in the magnetic field.

Next we should introduce a particularly importance situation of IC radiation in the energetic radiative process. Consider the case when electrons first produce seed photons due to synchrotron radiation, and those seed photons are then IC scattered by the same electrons that produce them ealier, the seed photons would end up with a much larger energies. This process -- called synchrotron-self-Compton or SSC -- could be important for GRBs and other relativistic sources.

The relative importance of synchrotron and IC processes for extracting energy from a population of energetic electrons is specified by the Comptom Y parameter ($Y \sim P_{ic}/P_{syn} \sim u_{\gamma}/u_{B}$).

Energy density in photons for the synchrotron process is:
$$
u_{\gamma} = \int dr \int d\gamma_e \frac{P_{syn}}{c} \frac{dn_e}{d\gamma_e} = \frac{\sigma_T (\delta R)B^2}{6\pi} \int d\gamma_e \gamma_e^2 \frac{dn_e}{d\gamma_e}
= \frac{\sigma_T (\delta R) n_e B^2}{6 \pi} <\gamma_e^2>
\tag{28}
$$

>Of course the energy density for synchrotron process depends on the environment and the enegy of the electrons.

where $\delta R$ is the width of the source, and
$$
<\gamma_e^2> \equiv \frac{1}{n_e}\int d\gamma_e \gamma_e^2 \frac{dn_e}{d\gamma_e}
\tag{29}
$$

Using (28), we find the Compton-Y parameter to be
$$
Y \sim P_{ic}/P_{syn} \sim \tau_e <\gamma_e^2>
\tag{30}
$$
where $\tau_e = \sigma_T (\delta R)n_e$ is the optical depth of the source to Thomson scattering.

### 2.3.1 IC spectrum

The spectrum of IC radiation is obtained by convolving electron distribution with the seed photon spectrum (Rybicki and Lightman, 1979):
$$
f_{ic}(\nu_{ic}) \approx \frac{3\sigma(\delta R)}{4} \int d\nu \frac{\nu_{ic}}{\nu^2} f_{syn}(\nu) \int \frac{d\gamma_e}{\gamma_e^2} \frac{dn_e}{d\gamma_e} F(\nu_ic/4\gamma_e^2\nu)
\tag{31}
$$

where
$$
F(x) \approx 2(1-x)/3
\tag{32}
$$

For a $\delta-function$ seed photon spectrum (where photons have frequency $\nu_0$), and a power-law distribution of electrons with index $p$ which is cut off at the low energy end at $\gamma_m$, these equations give that the IC spectrum is proportional to $\nu_{ic}$ for $\nu_{ic} < 4\gamma_m^2 \nu_0$. Therefore, **the low energy part of IC spectrum can be significantly harder than the hardest possible part of IC spectrum when synchrotron-self-absorption is negligible**.

At higher photon energies, $\nu_{ic} > 4\gamma_m^2\nu_0$, the IC spectrum has an asymptotic power-law index $\nu_{ic}^{-(p-1)/2}$, same as the spectrum for the synchrotron process.

> From the above we can learn that there exists a critical frequency $4\gamma_m^2 \nu_0$ at which the IC spectrum reach its peak. The spectrum is proportional to $\nu_{ic}$ less than the critical frequency and is a power-law decline with respect to $\nu_{ic}$ larger than that frequency.

### 2.3.2 IC in Klein-Nishina regime

When photon energy in electron comoving frame approaches (or exceeds) $m_e c^2$, two effects become important. One of which is that the eletron recoil can no longer be ignored. The ohther effect is that the cross section is smaller than $\sigma_T$ and it decreases with increasing photon energy as $\sim \nu^{-1}$.

One simple consequence of the recoil effect is that the energy of the scattered photon is limited to $\sim m_e c^2 \gamma_e /2$ (no longer $\sim \nu_0 \gamma_e^2$) which is obviouse  from energy conservation.

<div id='sect3'></div>
## 3.Afterglow theory

<div id='sect3.1'></div>
### 3.1 Relativstic shocks: basic scalings

This is a relativistic blastwave theory that describes interaction between the "fireball" -- which moves with Lorentz factor $\Gamma_0$ before deceleration and has total "isotropic equivalent" energy E -- and the circumburst medium (CBM) described by the density profile, $n(R)=(A/m_p)R^{-k}$.

A power-law decaying multi-wavelength afterglow is predicted before the first observational detection of X-ray afterglow in 1997.

A relativistic shock theory was developed by Bland-ford and McKee (1976) in the context of AGN jets which turned out to bewell suited for interpreting GRB afterglows in X-ray, optical and radio bandswhen they were discovered in 1997.

 The self-similar nature of the blastwave solution naturallyexplains the power law behavior of the afterglow lightcurves.

 >1.Afterglow theory is a relativistic blastwave theory of the interaction between fireball and the CBM (which described by $n(R)=(A/m_p)R^{-k}$.).<br />2.The power-law decaying afterglow was indeed predicted before real observation.<br />3.A relativitic shock theory developed for AGN jets is well suited for interpreting GRB afterglows in optical, X-ray and radio bands.

The basic dynamics of blastwave is easy to understand using simple physicalarguments,  and  the  main  results are sketched in Figure 6.
<center>
<img src='./blastwave.png' height=100% width=100%>
</center>

It is best to work in the comoving frame of the shocked fluid which is traveling with Lorentz factor $\Gamma$ with respect to unshocked fluid. The density of the unshocked medium in this frame is $\Gamma n(R)$, and upstream particles are seen to be streaming toward the shocked fluid with a Lorentz factor of $\Gamma$; upstream particles have  thermal energy much smaller than their rest mass. What  a shock does is to randomize the orientation of particle velocity vectors, without changing their Lorentz factors, when they cross the shock front, and therefore the mean “thermal” energy of protons down-stream of the shock front is $\Gamma m_p c^2$ (derivation provided below). As viewed from the lab frame, the average energy of each down-stream proton is $\Gamma^2 m_p c^2$, and hence for a blast wave at radius R, the total energy in the shocked plasma is
>Consider the comoving frame of the shocked fluid, the unshocked fluid stream toward the shocked fluid with $\Gamma$, with the velocity direction of the unshocked particles randomized and magnitude unchanged. 

$$
E \approx 4 \pi A R^{3-k} c^2 / (3-k),
\tag{33}
$$



### 3.2 余辉同步辐射光谱和光变曲线

三个特征频率 $\nu_a$, $\nu_m$, $\nu_c$

- 慢冷却，$\nu_m$ < $\nu_c$

  ![eq61](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/eq61_p30.png)

- 快冷却， $\nu_c$ < $\nu_m$

  ![eq62](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/eq62_p30.png)

$\nu_m$和$\nu_c$由同步辐射公式给出（eq18,eq69,eq64,eq65,eq66），$\nu_a$可由对应温度等流量黑体算出（eq68）。

这三个特征频率随时间的变化可从激波动力学，特别是根据激波洛伦兹因子的演化算出u。

- constant CBM:

  ![eq70-72](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/eq70-72_p30.png)

- wind like CBM

  ![eq73-75](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/eq73-75_p31.png)



峰值频率的完整表达式（上为constant CBM， 与时间无关；下为wind-like CBM，随时间减小）

![eq79-80](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/eq79-80_p32.png)

光度距离由78式给出。



通过以上这些式子，可给出$\nu > max(\nu_m, \nu_c)$频段观测到的流量：

![eq81](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/eq81_p33.png)



外激波下的同步辐射机制可以给晚期（晚于10小时）的GRB提供较好的描述。

![fig7](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig7_p33.png)



### 3.3 Reverse shock

如果喷流中磁场不太强（比如磁化参数$\sigma = B'^{2}/(4 \pi n'_p m_p c^2) \ll 1$）则在余辉早期，反向激波会在喷流中传播，使喷流减速。RS-FS系统可被分为以下四个区域：

![fig8](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig8_p34.png)

3区域这样被反向激波加热的区域可发出辐射，这样的预言在GRB 990123中被发现。

- 2 3 区域的压强与洛伦兹因子相等，但密度不相等。



这几个区域之间的相对洛伦兹因子有如下关系（相对论情况下）：

![eq82](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/eq82_p34.png)

- $\Gamma_0$是4区相对1区的洛伦兹因子，即喷流的洛伦兹因子。

有了这些洛伦兹因子，即可推导出2和3区域的一些热动力学性质Sari and Piran (1995)。



基于以下无量纲化的宽度：

![eq83](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/eq83_p35.png)

- 若$\xi > 1$，则为 thin shell
- 若$\xi < 1$，则为 thick shell

两种情况下FS/RS系统的动力学不一样，进而光变曲线也不一样。

详细的讨论可参见35页提到的一众文献。



RS/FS系统三种类型的特征：

- re-brightening。标准的microphysics parameters下，如$\epsilon_e = 0.1 \epsilon_B = 0.01$，光变曲线显示出重燃的特征。第一个峰一般由RS主导，第二个峰则对应FS中$\nu_m$下降至光学波段以下。
- flattening。如果未激波化喷流区域（区域4）的磁化程度不够压制RS，且RS磁场强于FS磁场，则RS辐射将会主导光变，就像GRB 990123。早期光学耀发由RS主导，当RS穿透喷流时达到峰值，随后快速衰减（$ \sim t^{-2}$）。
- no RS component。Swift时代探测到的一些早期GRB余辉并未显示出RS迹象。原因可能是这些GRB喷流为Poynting流量主导的从而抑制RS(Zhang and Kobayashi, 2005; Mimica et al., 2009)，抑或是RS中$\nu_m$太低(Jin and Fan, 2007)。



### 3.4 Jet break

很多GRB余辉光变曲线中显示出了消色差拐折，表明GRB外流是准直的（Rhoads
1997 预测）。

光变曲线变陡由两方面因素造成：

- “edge” effect

  对于以洛伦兹因子$\Gamma$移动的喷流，其内部辐射出来的光子的在静系看来是集中在张角为$1/\Gamma$内的。对于一个张角为$\theta_j$的喷流，一开始洛伦兹因子比较大，$\Gamma > 1/\theta_j$，光子集束角小于喷流张角，观测者只看到了喷流的一小部分发出的辐射。这一阶段的光变曲线为拐折前曲线。随着喷流减速，洛伦兹因子变小，当$1/\Gamma \sim \theta_j$时，即光子集束角与喷流张角相当，光变曲线便开始出现拐折。此后洛伦兹因子继续减小，光变曲线开始以更陡峭的斜率衰减。

  该效应是一个几何+相对论性的效应，受此影响，特定流量在拐折前后会有一个$\propto \Gamma^2$因子的变化。

  对于均匀密度CBM的情形，$\Gamma^2 \propto t^{-3/4}$；同步辐射的各特征频率随时间的演化不受此效应的影响。

  对于wind-like CBM的情形，$\Gamma^2 \propto t^{-1/2}$，且该情形下的喷流拐折会显得更光滑，整个拐折过程大约会跨越两个星等（2 orders of magnitude）。有数值模拟显示该情形的拐折时标会更短一点，大约跨越一个星等。

- sideways expansion

  当边缘效应发生作用时，横向声波也传播到了喷流外侧，引起侧向延展，张角会随洛伦兹因子减小而增加：$\theta_j \sim 1/\Gamma$。均匀密度CBM下，结合能量守恒，可知喷流半径的增大速度在拐折之后会大幅下降，$\Gamma \propto \sim t_{obs}^{-1/2}$。测向延展影响了洛伦兹因子的演化，进而也会影响特征频率以及光变曲线的演化。

  ![eq84-89](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/eq84-89_p38.png)

  数值模拟显示侧向延展造成的影响在$\Gamma < 2$之前都不重要。 



一般认为GRB喷流是结构性的，即其性质（如光度和洛伦兹因子）存在一个相对中轴线的角分步，如幂律分布或高斯分布。对于一个正轴观测者，结构性喷流衰减的斜率会比普通高帽模型的斜率要陡。而对于偏轴观测者，光变曲线的行为大部分会受到观测角$\theta_v$的影响，喷流拐折时间将由观测角$\theta_v$而非喷流张角$\theta_j$决定。

有理论认为，所有GRB的喷流都是类似的，观测上呈现的不同性质是因为观测角度不同而导致的。 （"quasi-universal" jet, Rossi et al., 2002; Zhang and
Mészáros, 2002b; Zhang et al., 2004a）

还有一种广泛讨论的结构性喷流是二成分喷流，由中间狭窄的，高洛伦兹因子和高光度的部分，加上四周包围的更宽但光度较低，洛伦兹因子较小的部分组成。这样的模型，在不同的观测角下也可以解释一些GRB的光变曲线的现象，如较早的喷流拐折以及晚期的重燃（re-brightening）现象。这种模型也包括“cocoon”模型，可由塌缩型超新星的长暴中产生。

偏轴观测也可能会导致“孤儿”余辉的发现，即仅观测到了余辉辐射，而没有观测到伽玛辐射本身。观测者可能会看到余辉流量上升，直到$1/\Gamma$辐射椎进入了视线后开始像喷流拐折后的情形一样衰减。


<div id='sect4'></div>
## 4. Afterglow observations and interpretations

1997年GRB 余辉首次被预测，紧接着在GRB 970228中首次观测到X射线和光学波段余辉，在GRB 970508中首次观测到射电余辉。



### 4.1 Late time afterglow observations and interpretations

在Swift卫星发射以前就已经通过观测收集了许多GRB的晚期（10小时后）且宽波段的余辉数据。这些观测数据通常都符合外部前向激波的同步辐射模型。主要的观测特征如下：

- 通常，光学余辉会呈现出幂律衰减$F_{\nu} \propto t^{-\alpha}$，衰减指数$\alpha \sim 1$。这与标准外激波余辉模型的预测吻合。
- 通常在明亮的GRB的光变曲线中会观测到拐折，大概发生在一天左右。拐折之后曲线衰减会变陡，$\alpha \sim 2$。这与喷流拐折理论是吻合的。
- 射电波段的余辉光变曲线通常会先上升，在10天左右达到峰值后开始衰减。达到峰值时一般也是同步辐射注入频率$\nu_m$或同步辐射自吸收频率$\nu_a$演化到射电波段的时候。
- 余辉i的宽频光谱可以用一个broken power law来拟合，同样符合同步辐射余辉模型。
- 一些有高质量观测数据的GRB（如GRB 021004、 GRB 030329）的光变曲线中会出现一些其它的结构，如bumps（鼓包）或者wiggles（波动），偏离了理想余辉模型的预测。曲线中出现光滑的鼓包的原因有可能是暴周介质的一个“密度鼓包”造成的；而比较尖锐的特征则有可能是因为中心引擎的能量注入，每单位立体角的能量的角分布波动，又或是由于双成分喷流的存在。

通过对余辉光变数据的模型（Panaitescu and Kumar2001, 2002; Yost et al. 2003）拟合，可以推出激波参数（$\epsilon_e,\  \epsilon_B,\  p$）。结果证明这些参数对于不同的GRB通常是不同的。

另外，余辉数据似乎更倾向于一个均匀密度的介质而不是密度分层的星风型介质。

还有一个有趣的事实是，尽管GRB blastwaves的各向同性动能的分布会跨越三个量级，但经过喷流修正的余辉能量通常集中在约一个量级，伽玛能量也是如此。这反映了Swift之前探测到的GRBs的能量储备大概是接近的。



### 4.2 Early afterglow observations and interpretations

Swift卫星上天后，我们可以得到早期（从小于100s开始）余辉的观测数据，这些数据展示了很多意料外的有趣的特征。

GRB 990123的早期观测数据呈现了一个明亮的光学耀发，显示其与伽玛辐射有着不同的来源。这个耀发显示为一个sharp rise和一个steep decay，衰减部分的指数约为2。这是不符合外部前向激波模型的，但可以用逆向激波来解释。但如果用逆向激波来解释的话，逆向激波区域的磁场应该比前向激波区域的磁场强，同时不能太强，否则会抑制逆向激波导致其无法辐射出观测水平的辐射流量。

可能是与光学耀发联系在一起的射电耀发，也在一些GRB中被探测到，如GRB 990123 和 GRB 021004。射电耀发的峰值要来的晚些（一天左右），它同样可以用逆向激波来解释。

![fig9](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig9_p48.png)



Swift在早期的X波段余辉探测到了数个令人惊讶的辐射成分。这些数据可以看作光变曲线的模板，通常包含5个成分。

![fig10](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig10_p49.png)

![fig11](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig11_p49.png)



但不是所有的GRB都有这5个成分。这5个成分的主要性质总结如下：

- 第一阶段是一个快速衰减阶段，衰减指数大于2。这一阶段可能与瞬时辐射的结尾有关。This phase may be simply the high latitude emission (described in §2.1) associated with the prompt γ-ray source at R > ∼ 10 cm when the central engine turns off faster than the decline of the X-ray lightcurve (Kumar and Panaitescu, 2000a; Dermer, 2004; Zhang et al., 2006; Nousek et al., 2006; Liang et al., 2006a). On the other hand if the emission region is at a much smaller radius then the rapidly declining X-ray lightcurve reflects the time dependence of the central engine activity (Fan and Wei, 2005; Barniol Duran and Kumar, 2009).
- 第二阶段是慢衰减阶段（或平台期），衰减指数约0.5或再大一点。有时候是平的，甚至稍微上升。在大多数GRB，第二阶段后面会跟着一个"“普通（normal）”的衰减阶段$\sim t^{-1}$。在外激波模型中，这一阶段可以视为中心引擎持续向blast wave供能的体现。偶尔平台期后会跟着一个非常快速的衰减，这可能显示平台期有一个“内部（internal）”起源。
- 第三阶段是普通衰减阶段，$\sim t^{-1}$，符合典型的前向激波模型。
- 第四阶段是晚期的加快衰减阶段，$\sim t^{-2}$或更陡一些。符合jet break后的前向激波理论。
- 第五种是X射线耀发。经常在GRB的X射线余辉中发现一个或多个耀发，其性质与瞬时辐射的脉冲相像，通常认为其是由晚期中心引擎的活动导致的。

有理论（O’Brien et al., 2006; Willingale et al., 2007; Ghisellini
et al., 2009）将X射线余辉描述成是双成分组成的：瞬时辐射+余辉辐射。这一唯象（phenomenological）理论对一些Swift GRB的X射线余辉数据可以拟合地较好。

有一部分的GRB会显示出一个“色差”的余辉：X射线光变发生的拐折（阶段2到阶段3或阶段3到阶段4。）而光学余辉的光变没有发生拐折。这就要求至少两个辐射区域分别辐射不同波段的辐射。

接下来介绍和总结一些解释余辉光变各种特征的理论观点。

#### 4.2.1 Steep decay of early X-ray light-curve

如前所说，对快速衰减的I阶段的标准解释是，该阶段反映的是瞬时辐射的末期。但具体来说还有一些问题没有定论，如该阶段的X射线流量是单纯来自瞬时辐射迅速结束情形下的高纬辐射，还是来自某种衰退不那么快的中心引擎。另外我们通常会在快速衰减阶段观察到强烈的光谱变软的现象， 这并不能用简单的高纬辐射模型解释。

其他关于快速衰减阶段辐射来源的模型包括快速扩散（rapidly expanding）的cocoon；爆炸波中强子能量的快速释放（rapid discharge of hadronic energy of the blastwave）；外部反向激波的高纬辐射（high-latitude emission of the external reverse emission）；以及较低最大频率的外前向激波同步辐射谱扫过X射电波段的表现。后三年种都潜在假设瞬时辐射是外激波起源的，因为观测上这一阶段辐射是瞬时辐射的尾巴，而后三种均认为这一阶段来源于外激波模型，而伽玛射线光变曲线的多变性（variability）则并不支持这种观点，所以这三种模型都不被支持。

#### 4.2.2 Sudden increase in X-ray flux (flares)

X射线耀发通常的解释是来源于GRB中心引擎的重启，因为其时标相对较短$\delta t_{obs}/t_{obs} \ll 1$。数据分析(Chincarini et al., 2010; Margutti et al.,2010, 2011)也直接支持了这一解释。

#### 4.2.3 Plateaus in X-ray light-curves

慢衰减或是平台期的II阶段以及后面的III和IV阶段的解释更具挑战性。一般的解释是，正在减速的外激波由于能量注入而减慢了衰减，而当能量注入停止后，光变曲线则进入阶段III的衰减。而在这一情景下，X射线和光学波段应该均表现出相似的拐折，即这个拐折是消色差的（achromatic），事实也的确有一些GRB可以用这一模型解释，如GRB 060614，GRB 060729。

然而对于有色差行为的余辉，单靠这一模型就无法解释了，还需补充其他成分的辐射机制。对于外激波模型最为直接的扩充就是引入双成分喷流，其中狭窄的喷流主导X射线辐射，较宽的喷流则主导光学辐射(e.g. Racusin et al., 2008)。另一种扩充就是把反向激波辐射也囊括进来，两种激波叠加起来形成观测到的光变曲线。

Shen 和 Matzner （2012）将慢衰减阶段解释为滑行阶段的前向激波在wind-like介质中的同步辐射，但这个模型要求一个相对小的洛伦兹因子Shen 和 Matzner （2012）将慢衰减阶段解释为滑行阶段的前向激波在wind-like介质中的同步辐射，但这个模型要求一个相对小的洛伦兹因子，可能与有瞬时辐射数据中得到的较大洛伦兹因子相矛盾。另外该模型也只能解释消色差的余辉光变行为。

#### 4.2.4 Steep decay foloowing the plateau in X-ray light-curve

有一小部分的GRB的X射线光变曲线在平台期后会跟着一个快速的衰减$f_\nu \propto t_{obs}^{-3}$，或者更陡。

![fig12](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig12_p54.png)

这样平台后跟随快速衰减的现象比较少见，图10中也未表现这种特征阶段。该现象不能用外激波模型解释，它只能起源于“内部（internal）”涉及持久喷流的直接耗散（involving direct dissipation of a long-lasting jet）。X射线耀发以及这种内部起源的平台都反映了持久性中心引擎的存在。



总之，早期余辉的多样性向我们展示了使用多种辐射成分来解释光变曲线的必要性。不管是中心引擎的活动，某些内部的过程如内激波，还是外部反向激波和前向激波，都可用来解释的各类光变曲线的行为（主要是色差性余辉的光变）。这些成分的叠加组成了我们观测到的光变曲线，而不同GRB的参数条件的不同则导致各自曲线的不同特征。



### 4.3 High energy ($\gt 10^2 MeV$) afterglow radiation

在Compton-Gamma-Ray-Observatory (CGRO)时代，有一个GRB，GRB 941017，在其爆后1.5小时从地球遮掩中重现时仍有GeV的辐射被探测到。

接下来总结一些解释这些GRB发出的延迟的，持久的高能光子的理论模型。这些模型包括内激波模型，当反向激波正穿过喷流时外激波中的同步自康普顿散射（SSC）模型，反向激波和前向激波的双SSC模型以及两个交叉的逆康普顿（IC）模型（前向激波的光子被反向激波中的电子碰撞加速，以及反过来）。另外，瞬时辐射中的伽玛光子也可能在FS或RS中的电子碰撞加速而变得更高能。还有一种情形可以产生延迟的高能GeV光子，就是CMB中的光子被星系际介质中高洛伦兹因子的电子-正电子对散射加速，而这样的电子-正电子对则是在GRB的TeV光子与宇宙红外背景辐射相互作用产生的。但这样的机制只有在星系际介质的磁场很低时$\lt \sim 10^{-15} G$才能发生。

Fermi卫星的上天让我们能系统研究100MeV以上的GRB，并解决高能伽玛光子的来源问题。Fermi的LAT和GBM每年联合探测约10个GRB，通过这些观测我们发现100MeV以上的光子通常在GBM触发几秒后到来， 且LAT能段（> 100MeV）的辐射能够持续长达~$10^3 s$，远长于GBM能段（~5keV - 10MeV）典型持续时间的$10-30s$。另外，LAT的光变曲线通常在其几乎部持续时间内呈现简单的幂律衰减。

在Fermi发现这些性质后，我们才意识到瞬时辐射后的持续时间~ 30s 的100MeV以上的光子是由外前向激波中的同步辐射过程产生的，理由如下：

LAT的谱指数和光变曲线的衰减指数 $f_\nu(t) \propto \nu^{-1.1}t^{-1.3}$完美符合$\nu > \nu_c$时激波加热的CBM的同步辐射的closure relationship。

![fig13](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig13_p58.png)

Kumar (2000) 展示了当观测频段大于同步辐射冷却频率时，外前向激波的单色（specific）流量仅决定于爆炸波的能量和电子所占的能量，而与不确定的CBM密度无关，也对磁场能量不敏感（$f_\nu \propto \sim \epsilon_B^{0.1}$）（式81）：

![eq81](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/eq81_p33.png)

据此我们就可以较可靠地根据瞬时辐射中伽玛射线的能量来预测Fermi/LAT能段的流量，并且在一些研究详细的GRB里，预测的流量与实际的LAT能段观测到的流量吻合较好。

![tab1](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/tab1_p68.png)

同样，我们可以根据早期（$t \sim 10^2 s$）的Fermi数据来推算外激波的参数，再利用相关参数预测晚期的光学和X射线流量（见fig 13），且观测与预测也符合得很好。相反，也可以用晚期（0.5天后）的X射线，光学以及射电数据来确定外激波参数，进而计算早期（早于约$10^3 s$）的高能（100MeV）流量。这些都表明LAT探测到的30s后的高能光子是由同步辐射过程产生的。

![fig14](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig14_p59.png)

不过要指出的是，同步辐射过程要产生高于$\sim 50\Gamma MeV \sim 5GeV$的高能光子并不容易（见2.2节讨论同步辐射能产生的最高能量光子），这些最高能的光子有可能是同步辐射的光子被逆康普顿散射而产生的。 

Kumar 和 Barniol Duran (2009, 2010)发现，要使Fermi GRB 外激波中产生的1 MeV的以下的流量不超过观测值，这些GRB的外激波的$\epsilon_B$应该比较小（~$10^{-6}$ for a 0.1 cm$^{-3}$ CBM，密度越高则越小）才行。另外，Fermi/GBM 的10keV - 10MeV的光变曲线在顺势辐射阶段后衰减得很快，所以前向激波在此能段的贡献（~$t^{-1.2}$）必须足够低于观测值，才能确保瞬时辐射结束阶段的GBM曲线快速衰减。

> 这段说的应该是，要使前向激波的理论预测的早期高能辐射值小于观测值（因为还有瞬时辐射对观测值的贡献），磁场就必须相对小。

It can be shown that this small magnetic field is sufficient for confining high
energy electrons of thermal Lorentz factor ~ $10^8$ (that produce ~ 10 GeV
photons), both upstream and down-stream of the shock front, and for their
efficient acceleration by the first order Fermi mechanism as long as these electrons are not exposed to a large flux of a few eV photons ( > ~ 10 mJy in our frame) to cause severe IC losses (Barniol Duran and Kumar, 2011; Piran and Nakar, 2010).

> 不明白这段话要表达什么意思，不过应该与高能光子的产生有关。

第5节会讨论更多GRB关于$\epsilon_B$的测量及其意义。

前面提到GeV余辉的光变曲线几乎都呈现简单的普通（normal，斜率中等）幂律衰减，而只有5%的X射线余辉是简单幂律衰减的，大多数呈现陡峭—缓慢—中等—陡峭的衰减行为（4.2节）。只有很少数的GRB同时触发了Swift/XRT和Fermi/LAT，目前有GRB 090510 (De Pasquale et al., 2010)和 GRB 110731A (Ackermann et al., 2013b)，而它们的GeV和X射线光变曲线在几乎全部持续时间内（LAT开始于~5s，XRT开始于~100s）都显示出幂律衰减行为。这些爆的光学，X射线和GeV的数据也都符合外前向激波的模型。这样的话，不禁会想伴随有GeV余辉的GRB是否也都会呈现少见的简单幂律衰减的X射线余辉。

当然如果观测到有拐折的GeV余辉曲线（steep—shallow），可以解释为辐射机制从瞬时辐射主导变为余辉同步辐射主导。

<br>

<div id='sect5'></div>
## 5 Collisionless shock properties from GRB afterglow observations

GRB余辉提供了研究相对论性非碰撞激波（collisionless shock）的天然实验室。目前，尽管有很多理论研究工作，还是有不少相关的问题没有解决，重要的如：激波面（shock front）上/下游的磁场的产生（$\epsilon_B$）,粒子加速（$p$）以及激波化等离子体中转移到电子的能量（$\epsilon_e$）。因为同步辐射的计算设计到这几个量，所以多波段余辉的光变曲线可以帮助我们反过来测量这些量，从而有助于collisionless shock的基础等离子物理的发展。

在同步辐射框架下，GRB余辉在任何给定时间辐射的流量是由这四个参数决定的：$E$（爆炸能量），$n$（CBM密度），$\epsilon_e$和$\epsilon_B$。电子分布参数$p$可以从X射线光谱导出，故不在上述几个未知参数中。因此，要确定这四个参数，我们至少需要4组独立的观测，且这4组观测应该落在同步辐射谱的不同特征区段（比如一组的观测频率在$\nu_m$一下，另一组在$\nu_m$以上；或一个在同步自吸收区段，另一个不在），这样每组观测才能提供独立的信息。但通常我们难以满足这一点，因此除了少数在X射线，光学，射电均有长时间跟踪观测的GRB，我们很少能唯一地测量这4个参数。

$\epsilon_e$是由相对论激波的微观物理（micro-physics）决定的；如果磁化流体的磁场是由Weibel不稳定性或是其它基于当地等离子体物理条件下的某种不稳定性而产生的，那么$\epsilon_B$也决定于激波微观物理。所以，基于基础物理的考虑，$\epsilon_e$和$\epsilon_B$应该可作为能够描述相对论激波的变量的函数，即可作为$E$，$n$，$\Gamma$（激波前的洛伦兹因子）的函数。

由于$\nu_m$以上频段的余辉流量正比于$\epsilon_e^{p-1}$（eq.81），对$\epsilon_e$依赖较强，所以这个参数的测量是相对最可靠的一个。

![fig15](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig15_63.png)

上图展示了30个GRB的$\epsilon_e$的分布，平均值为0.2，且围绕平均值有一个因子为2的dispersion。$\epsilon_e$ ~ 0.2与最近的相对论非碰撞电子-离子激波的模拟比较吻合。这些爆的$E$和$n$的跨度比较广。所以，可以粗浅的说，$\epsilon_e$与激波的强度无关，且不同的GRB的$\epsilon_e$变化因子~2。

![santana_fig1](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/santana_fig1.png)

![santana_tab6](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/santana_tab6.png)

假设GRB的瞬时伽玛辐射的辐射效率为20%（即blast wave中的能量为瞬时伽玛辐射能量的4倍），以及外激波中$\epsilon_e = 0.2$，则从光学余辉的数据就可以推得$\epsilon_B / n$。下图展示了Swift探测的35个GRB的$\epsilon_B$的分布，可以看出其分布很广，中值为$3 \times 10^{-5}$，跨度大于4个量级。

![fig16](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig16_p64.png)

没有证据显示$\epsilon_B$依赖于激波的洛伦兹因子。对于一些Fermi/LAT的爆，我们可以从其早期当洛伦兹因子大于100时的伽玛射线数据来推断$\epsilon_B$（下图左）或者从晚期当洛伦兹因子减小到~10时的X射线和光学的数据来推断$\epsilon_B$（下图右），并且由早期数据得到的和晚期数据得到的$\epsilon_B$是吻合的。另外，Collisionless shock 模拟也显示$\epsilon_B$与$\Gamma$之间没有关联（Sironi and Spitkovsky 2011）。这些表明，磁场应该不会仅与相对论激波的微观物理相关。

![fig17](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig17_p65.png)

在激波波前的区域，CBM的磁场$B_0$会被放大，放大因子为AF（$\propto \sim n^{0.2} B_0^{-1}$），在一定假设下（给定$n,B_0$）可结合观测算出，注意算出的AF应对应所有对观测值有贡献的辐射区域（激波化等离子体区域）处磁场的平均。上面35个GRB的放大因子分布如下，中值~30（$AF \sim 10^4$ for equipartition magnetic field）。

![fig18](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig18_p67.png)

如果磁场由下游（激波化区域）的Weibel不稳定性产生，则波前区域理论预期为$\epsilon_B \sim 0.1$，但这样的磁场的相干长度（coherence length scale）较小，且在尺寸相对比较大的激波化等离子体区域上有较强的衰减，导致整体的放大因子不大。一些数值模拟的工作支持这样的波前附近磁场较强以及它们存在衰减的情景。

另一些磁场产生机制，如shear across the GRB-jet，或能导致下游湍流的ISM密度不均匀性，它们产生的磁场的相干长度较大，贯穿整个下游（激波化）区域。

Lemoine et al.(2013) 通过分析4个不同GRB的X射线和GeV余辉数据，提出激波中的湍流磁场在接近波前的位置（同步辐射产生GeV光子的位置）较强（$\epsilon_B \sim 10^{-2}$），且强度随距波前距离衰减，在X射线产生的位置$\epsilon_B \sim 10^{-6}$。他们发现X射线的数据符合$\epsilon_B \propto \sim d'^{-0.5}$。

另外，GeV高能光子的探测给前向激波的上游（未激波化）磁场提出了一个下限：磁场强度至少应该能将产生这些高能光子的电子局限在激波中。Barniol Duran and Kumar (2011) 给出10$\mu G$的CBM磁场足够将电子加速至产生~10GeV的同步辐射光子。

至于电子能量分布指数$p$，一些计算给出对于非碰撞相对论激波，其值应约为2.2，与激波的洛伦兹因子无关，而GRB余辉光谱显示不同GRB的$p$值存在显著差异。一种可能是通过X射线余辉光谱计算得到的$p$值不是真实的外激波电子分布，因为光谱中辐射可能包含内部辐射的成反。当然也有可能是理论计算本身除了问题，这样的话我们应该根据观测得到的$p$值分布来修正理论模型。

<br />

<div id='sect6'></div>
## 6 Obsevational properties of GRB prompt radiation

### 6.1 Temporal properties

观测上，GRB瞬时辐射阶段一般指GRB探测器探测到sub-MeV辐射的阶段，而一个爆的持续时间通常用$T_{90}$表示：探测器探测到总通量的5%到95%所经历的时间。但这样观测上定义的时间会有一些限制：

- 与探测器的能段相关。对于同一个GRB，低能段探测器一般给出更长的$T_{90}$。
- 与灵敏度相关。探测器越灵敏，给出的$T_{90}$也越长。
- 一些GRB瞬时辐射的阶段不是连续的，中间存在间隔，这种情况下传统的$T_{90}$可能会高估中心引擎的实际持续时间。
- $T_{90}$内的辐射也可能包含外激波等其它区域的辐射。内部辐射和外部辐射的分界目前并不清晰。

下面的叙述依然把$T_{90}$作为瞬时辐射的持续时间，但讨论仅限于瞬时辐射的内部耗散模型（internal dissipation models）。

GRB的时域特性可总结如下：

- $T_{90}$的分布以约2s为分界显示出两种GRB类别：以20-30s为分布峰值的长爆和以0.2-0.3s为分布峰值的短爆。长爆在统计上比短暴要更软，即低能光子数量与高能光子的数量比值相对较高。

![fig19](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig19_p71.png)

- 瞬时辐射的光变曲线很不规则，有的非常多变，最小变化时标能达到毫秒量级，而有的光变则比较平滑，结构简单。一些GRB还具有间歇的辐射行为。

![fig20](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig20_p72.png)

- 部分GRB存在一般较软较弱的前兆（precursor）辐射，这些辐射会单独发生于主爆发的10s到100s之前。大概有3%到12%的GRB会有一个前兆辐射。一些统计研究表明主爆发阶段的性质和有没有前兆辐射无关，且一些GRB中的前兆辐射的性质与主爆发阶段辐射的性质相似。

- Power density spectrum (PDS) analysis of GRB lightcurves reveals null
  periodicity. The PDSs of individual GRBs can be noisy. However, averaging
  the PDS of several bright GRBs leads to a power law with index -5/3 and
  a sharp break around 1 Hz (Beloborodov, 2000).

- 有证据表明GRB光变曲线是一个慢成分（slower component）和一个快成分（faster component）的叠加。This is evidenced by a gradual depletion of the fast component at low energies (Vetere et al., 2006), and the existence of a distinct low frequency component in a stepwise low-pass filter correlation analysis (Gao et al., 2012).
- 光变曲线中的单个脉冲一般是非对称的，它们呈现突然的增强和稍慢一些的衰减。对一些明亮的单脉冲，多用“FRED”（fast-rising exponential-decay）函数来拟合。
- 一个爆在持续阶段中会存在沉默阶段。这些脉冲间的间隔时间的分布也符合对数正态分布。
- 光变曲线的形状随能段的不同会有变化。在更硬的能段，脉冲会变得更窄。一个脉冲的宽度随能量的变化 $\omega(E) \propto E^{-\alpha}$，$\alpha \sim 0.3 - 0.4$。

![fig21](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig21_p73.png)

![fig22_p74](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig22_p74.png)

- 在很多长GRB中，keV-MeV能段会存在“光谱延迟（spectral lag）”现象，即低能段的脉冲相较高能段的脉冲存在系统的延迟(Norris et al., 2000; Norris, 2002; Norris et al., 2005)。短爆没有表现出明显的spectral lag。一部分短爆显示出相反的延迟(Yi et al., 2006)。

![norris_fig26](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/norris_fig26.png)

<br />

### 6.2 Spectral properties

#### 6.2.1 Spectral shapes and functions

GRB光谱分time-integrated 和 time-resolved两种，后者能提供光谱演化的信息，但一般只有较亮的GRB才在每个time bin中有足够的光子用来抽取time-resolved的光谱。

一个典型的GRB宽频谱可以用一个平滑的拐折幂律：Band 函数 来拟合。

![eq9_p73](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/eq98_p73.png)

能谱的峰值能量由$E_p = (2+\alpha)E_0$给出。下图展示了GRB 990123的time-integrated能谱可以用Band函数很好的拟合。

![fig23_p75](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig23_p75.png)

能量峰值$E_p$的分布较广，从几个keV到MeV连续分布。从硬到软可以大致归类为 伽玛射线爆gamma-ray bursts(GRBs,$E_p$ >50 keV)，富X射线伽玛爆X-ray rich GRBs (XRGRBs, 30 keV < $E_p$ < 50 keV), 以及 X射线耀发X-ray flashes (XRFs, $E_p$ < 30 keV)，它们之间也没有明确的分界。对于BATSE探测的明亮的爆，两个谱指数的分布为$\alpha \sim -1 \pm 1$，$\beta \sim -2^{+1}_{-2}$，且Fermi和INTEGRAL探测的样本也证实了这样的分布。

另一方面，对于能段较窄的探测器探测的GRB，如Swift，一般可以用截断幂律去拟合

![eq100_p75](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/eq100_p75.png)

这实际上就是Band函数的前半部分。后半部分因为缺少高能数据所以难以限制高能谱指数。不过如果Swift爆同时也被高能探测器探测到，如Konus-wind, Fermi/GBM，则仍可以用Band函数来拟合。

在Fermi上天之后，我们认识到目前至少有两种瞬时辐射谱，一种谱包含覆盖6-7个量级的Band谱成分，没有热成分，较为常见，如GRB 080916C。另一种则是类热成分与非热幂律谱的叠加，如GRB 090902B，这类谱较为少见。这两种谱的差别在time-resolved能谱中会变得比较明显。当缩小time bin时，GRB 080916C的Band谱拟合指数几乎不变，而GRB 090902B的Band成分则逐渐变窄，最后变为由准热成分+幂律成分来拟合，不过主导的还是幂律成分。

![fig24](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig24_p76.png)

Zhang et al (2011) 提到一些顺势辐射可能包含三个成分：I 非热Band谱；II 准热成分；III 另一个延伸至高能段的非热幂律成分 。如下图

![fig25_p78](/home/xlew/git/Astro101/GRB101/grb_review/the physics of gamma-ray and relativistic jets/fig25_p78.png)

另外，一个有趣的现象是，一些低光度的GRB表现出一定程度上不太一样的瞬时辐射光谱，如GRB 060218的顺势辐射光谱可以用内秉截断幂律很好的描述，且其峰值能量$E_p$的演化很迅速，从~80 keV 演化到 5 keV。考虑到GRB 060218在很多方面都比较特殊（距离近z=0.033，光度低，有成协超新星，持续时间长，存在热成分），这个爆（以及或许包括其他邻近低光度的GRB）可能有不同于高光度的GRB的辐射机制。

#### 6.2.2 Spectral evolution

GRB的time-resolved能谱分析能给我们提供更多关于瞬时辐射的线索，以下总结一些有趣的特点：

- 关于GRB脉冲中的光谱演化，一般有两种类型，第一种的演化模式为“hard-to-soft”演化，即$E_p$从脉冲一开始就开始下降。第二种演化表现出一种“tracking”行为，光谱硬度跟踪脉冲强度，即脉冲的上升期，光谱的$E_p$也在变大。观测上，这两种行为可以在一个爆中观测到。考虑到光谱不同成反的叠加效应，有观点认为所有的脉冲都符合“hard-to-soft”模式。
- 相当一部分LAT的GRB表现出GeV辐射的开始晚于MeV辐射的开始，如图21的GRB 080916C和图22的GRB 090902B，这当然也可能与谱指数的演化或者某些谱成分但尚不清楚原因。