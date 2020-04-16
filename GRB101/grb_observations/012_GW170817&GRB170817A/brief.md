# Brief note of No.12

Questions:

1. The observations of GW170817 and GRB 170817A?
2. The connection?
3. The implication?
4. Why this GRB is less energetic than typical?
5. The joint detection rate?

Methods:

1. GW170817
    - sky-location and signal offset time: EM follow-up observations (targeted searches???)
    - Hubble flow velocity + Hubble canstants -> verification of GW distance
    - GW data and known distance could constrain the inclination angle which could further constrain the jet viewing angle with two reasonable assumptions.
    - see the reference articles PhRvL, 119, 161101

2. GRB 170817
    - compareing the properies of gamma-ray data to the known distribution of short and long GRBs, Goldstein confirmed GRB 170817A as a short GRB.

3. Association confirmation
    - temporal agreement for being independent events: $P_{temporal} = 2\Delta t_{SGRB-GW} R_{GBM-SGRB}5.0 \times 10^{-6}$.
    - spatial agreement for being independent events: ??? result: 0.01
    - together: $5.0 \times 10^{-7}$

4. Implications
    - the diviation of the speed of gravity from the speed of light: $\Delta v/v_{EM} \approx v_{EM} \Delta t/D$
      - with different $\Delta t$ resulting in upper and lower limits.

    - the limits on Lorentz invariance violation
      - the effective field theory

    - the confirmation on the Equivalence princeple
      - shapiro delay

    - the size and lorentz factor of the emitting region from explaining the time delay
      - the lag from merger time to the collision between two shells (internal origin)
      - external origin
      - photospheric: thermal radiation (flawed)

    -  

Conlutions:

- The joint event set a **stringent limits on fundamental physics** and **probed the central engine of SGRBs** in ways that have not been possible with EM data alone.

- Unambiguous association of GW170817 and GRB 170817A

- Explanations for the observed dimness of GRB170817A is proposed.

- Joint detection could be more common than previously predicted.

## What can we learn from the observations of GW170817/GRB 170817A

1. Introduction
2. Observation Results
    - LIGO–Virgo Observation of GW170817
    - Fermi-GBM Observation of GRB 170817A
    - INTEGRAL SPI-ACS Observation of GRB 170817A

3. Unambiguous Association
4. Implications for Fundamental Physics
    - Speed of Gravity
    - Lorentz Invariance Violation Limits
    - Test of the Equivalence Principle

5. Astrophysics Implications
    - GRB physics
    - Neutron Star EOS Constraints

6. Gamma-ray Energetics of GRB 170817A and their Implications
    - Isotropic Luminosity and Energetics of GRB 170817A
    - Implications of the Dimness on the Central Engine
    - Observational Bias Against Low-luminosity GRBs
    - Predicted Detection Rates
    - Limits on Precursor and Extended Emission

7. Conlusion

## 1. 背景介绍

- BNS（双中子星）与NS-BH（中子星-黑洞）是LIGO/Virgo主要的搜寻目标，因为这些事件很有可能是同时探测到引力波辐射和电磁辐射信号的共同起源。
- 而双中子星并合事件理论上会引发SGRB，产生瞬时伽玛辐射以及较长时标的余辉辐射。
- 到目前（170817）为止，BNS（或NS-BH）与SGRB之间的关联只有间接的观测证据能够证明，如短暴观测中超新星成分的缺失以及短暴余辉与宿主星系之间的偏离等。而这次的GW与SGRB的联合观测清晰地表明了BNS并合与SGRB之间存在关联。

## 2. 有关的观测结果

详细的观测文章见references文件夹下的 Goldstein2017_GRB170817AObservation_GBM.pdf 与 probability of obtaining test Abott2017_GW170817Observation.pdf 两篇文章。

### 2.1 LIGO-Virgo对GW170817的观测

- 12:41:04 UTC LIGO首次探测到来自双中子星并合的引力波信号
- LIGO-Virgo的联合观测为该引力波信号确定了一个面积为28平方度的90%置信水平的天区范围（GBM给出的90％置信的范围大小约为1100平方度）。
- 该信号在致密星并合的全天搜寻中的错误率为1/80000年。

<img src='./fig1.png'>

- 两次offline targeted search（？？？）结果的p值都很低（9.4 x 10e-6; 1.3 x 10e-5）,表明检验高度显著，拒绝原假设的理由充分（原假设是什么？）

- 假设双星质量分别为$m_1$和$m_2$,且$m_1 \geqslant m_2$：
    - 在‘high-spin prior’(dimensionless spins ~ 0.89)？？？条件下给出$m_1 \in (1.36, 2.26) M_{sun}$， $m_2 \in (0.86, 1.36) M_{sun}$ and total mass $2.82_{-0.09}^{+0.47} M_{sun}$
    - 在‘low-spin prior’(dimensionless spins $\leqslant$ 0.05)条件下给出$m_1 \in (1.36, 1.60) M_{sun}$， $m_2 \in (1.17, 1.36) M_{sun}$ and total mass is $2.74_{-0.01}^{+0.04} M_{sun}$
    - 这样的质量范围符合目前已知的双星系统(Ozel & Freire 2016; Tauris et al. 2017).
- GW的观测数据给出源的距离为$40_{-14}^{+8}$ Mpc，对宿主星系（NGC 4993）的距离测量给出$42.9 \pm 3.2$ Mpc，两者是相符的。
- 另外GW数据还限制了倾斜角$\theta_{JN}$(观测视线与系统总角动量的夹角，其大小的限制与距离有关)：cos$\theta_{JN} \leqslant -0.54$. 假设SGRB的喷流方向与总角动量方向相同，则$\theta_{JN}$也可以近似看作伽玛暴的喷流观测角$\zeta$：$\zeta \leqslant 56\degree$。如果考虑宿主星系的距离，则给出$\zeta \leqslant 36\degree or \  28\degree$（取决于不同的哈勃常数）。

### 2.2 Fermi-GBM Observation of GRB 170817A

- GBM的数据显示了两个间隔明显的辐射阶段：
    - 第一个峰持续大约半秒，符合短暴的持续时标
    - 第二个阶段相比更软且持续时间达数秒

<img src="./fig2.png">

- 12:41:06.474598 UTC 是GBM的trigger时间($T^{GBM}_0$)，若以GW信号接收时间作为$T_0$ ($T^{GW}_0$),则相对的伽玛射线辐射的开始时间为(+1.74　$\pm$  0.05)s。

<img src="./Goldstein_fig1.png">

- 主峰可以较好地用一个康普顿辐射模型拟合，而后面的‘尾巴’辐射则可以用黑体谱较好拟合：

<img src="./Goldstein_table2.png">

- 由于并没有探测到“前兆辐射”（precursor eimssion），Goldstein给出了GRB 170817A的暴发前200s内的前兆辐射的流量上限：(6.8–7.3) × 10e−7 erg/s cm$^2$ (assuming 0.1s duration)and (2.0–2.1) × 10e−7 erg /s cm$^2$ (assuming 1.0 s duration)

### 2.3 INTEGRAL SPI-ACS Observation of GRB 170817A

- $T_0^{ACS} = T_0^{GW} +1.88 s$
- [-0.320s, +0.256s]时间间隔内得到的通量为(1.4 $\pm$ 0.4) x 10$^{-7}$ erg/cm$^2$(75–2000 keV)，与GBM的结果一致。
- 理论上SPI-ACS与GBM的信号到达时间的差异可以用来提高GRB的定为精度

