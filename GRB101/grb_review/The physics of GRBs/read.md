## Catalogue

| **Chapter**    | **Content**                                                  |
| -------------- | ------------------------------------------------------------ |
| **Chapter 1**  | **General introduction** 1-26                                |
| **Chapter 2**  | **Overview of GRB phenomenology** 27-95                      |
| **Chapter 3**  | **Relativity** 122-148                                       |
| **Chapter 4**  | **Relativistic hydrodynamics and magnetohydrodynamics** 149-181 |
| **Chapter 5**  | **Leptonic processes** 182-220                               |
| **Chapter 6**  | **Hadronic processes** 221-227                               |
| **Chapter 7**  | **Overview of the basic theoretical framework of GRBs** 228-272 |
| **Chapter 8**  | **Afterglow physics** 273-348                                |
| **Chapter 9**  | **Prompt emission physics** 349-417                          |
| **Chapter 10** | **Progenitor** 418-443                                       |
| **Chapter 11** | **Central engine** 444-472                                   |
| **Chapter 12** | **Non-electromagnetic signals** 473-497                      |
| **Chapter 13** | **Cosmological connections** 498-518                         |
| **Chapter 14** | **Impacts on fundamental physics ** 519-527                  |

## 1. Introduction

## 1.1 What Are Gamma-Ray Bursts?

- 能谱的峰值能量$E_P$可用于衡量GRB的能量释放的多寡程度。GRB的$E_p$分布很广，所谓XRFs是那$E_p$小于30keV的GRB事件。

- GRB的电磁辐射横跨射电波段到100GeV以上波段，但各波段的行为应该不尽相同（？2）。

- GRB还可能是一些非辐射类信号的源头，如极高能宇宙射线，中微子（MeV-EeV[dev=18]）和引力波。

- GRB的各向同性$\gamma$射线光度量级为 ~ 51-53 (erg/s)，相比之下，太阳的光度量级为33， 银河系所有星光的光度量级为44，AGN的光度量级约48。所以GRB是大爆炸后最明亮的爆发。GRB总释放能量与SN相当。
- 一些长爆被观测到与BL IC型SN关联，这是这些长爆起源于某些特定类型的大质量恒星死亡的直接证据。
- 短爆一般位于其宿主星系中恒星形成较少的区域：NS-NS 或者 NS-BH(stellar size)。

- 长爆或短爆将形成一个高速吸积的恒星级黑洞或者是一个毫秒磁星作为残留物，它们将作为引擎发射（或维持？）相对论性的喷流。

  > 似乎有两个阶段：塌缩/并合阶段+残留物驱动阶段。瞬时辐射主要来自于哪一个阶段的贡献？这两个阶段如何提供抛射物质和提供能量？（自旋减慢？）喷流是在哪一阶段如何形成的？

- 目前，我们还没有实现对GRB全过程的全波段观测。



## 1.2 Brief History of GRB Research

### 1.2.1 Observational Progress

- 1967-1973 The discovery era

  - 美国军事卫星Vela偶然发现GRB 670702，该GRB持续时间约10秒，具有峰值流量不同的双峰结构，脉冲轮廓不对称，峰值能量约MeV。这些是GRB的基本特征。（Figure 1.1）

- 1973-1991 The dark era

  - 由于伽马射线探测器的**定位精度较差**，不足以进行有效的低频段对应体搜寻，所以尽管这一阶段发现了500多个GRB，人们对GRB起源的认识进展缓慢。
  - 不过在这一时期，Konus GRB catalog展现呈现出GRB根据持续时长可分为两类。
  - 1994年前，关于GRB的模型数量约为118个，其中比较接近现在的认识的模型是Stirling Colgate 1974提出的"supernova shock"模型。

- 1991-1997 The BATSE era

  - BATSE是CGRO卫星上搭载的一个专门用来探测GRB的仪器，它携带了8个能量覆盖范围为20keV-1.9MeV的大面积探测器（Large Area Detectors）以及8个10keV-100MeV的测谱探测器（Spectroscopy Detectors），总视场达到了全天覆盖，灵敏度为3E-8 erg/cm2 （1s爆）（以这么多的探测器通量持续1s的爆就能看见？）
  - BATSE在其工作期间（1991-2000）发现了2704个GRB，但定位误差较大，对于最强爆约为0.2度，对于最弱爆约为18度。因此在1997年之前一致没有发现确凿的GRB电磁对应体。

  - 主要进展：
    - 宇宙学起源的间接证据：角分布的各向同性以及强度的非均匀分布
    - 短爆与长爆以约2s为分界，长爆一般比短爆软
    - 光谱是非热的，通常可以用平滑连接的拐折幂律函数描述（Band function）

- 1997-2004 The BeppoSAX/HETE era

  - BepposSAX是一颗X射线探测卫星，它搭载了一个GRB monitor(40-700 keV)，两个宽视场仪器（WFI，2-30 keV）和一些窄视场仪器（NFI）

  - 两个WFI相比伽马射线探测器有更精确的定位精度，同时比光学波段更容易在伽马射线探测器的误差范围内寻找对应体（可见光波段相比之下太拥挤）。因此它成功探测到了GRB 970228 和 GRB 970508的X射线余辉，同时使得地面设备顺利在可见光和射电波段探测到余辉，并且辨认出了宿主星系，确定了GRB的宇宙学起源。

  - HETE（High Energy Transient Explorer）是美国（日本法国参与）的天文卫星，主要目标是抢先探测GRB的多波段对应体。1996年11月发射的HETE卫星因故丢失，HETE-2于2000年发射，任务持续到2006年。它携带了一个法国伽马射线望远镜（6-400 keV），一个大视场X射线监测器（WXM，2-30 keV）和一个软X射线相机（SXC，0.5-10keV）。

  - 这两个卫星提供了100多个GRB的精确定位，主要成就：

    - 首次发现GRB的X射线和可见光波段的余辉（GRB 970228, BeppoSAX）。首次发现射电余辉（GRB 970508, BeppoSAX）。后者红移也被成功测定为0.835。

    - 解决了长爆的起源问题：在GRB 980425 (BeppoSAX, z=0.0085)误差范围内发现邻近星系的Ic型超新星SN 1998bw。几年后，HETE-2 GRB 030329/SN 2003dh的联系也被确定。随后的对长爆的宿主星系的研究表明这些GRB通常发生在恒星诞生星系中恒星形成最活跃的区域。

      > 恒星形成区域难道是不断的形成新恒星又不断有恒星死亡？这样的持续时间大概有多久？

    - 丰富的多波段余辉数据检验以及发展了GRB物理模型：幂律衰减的行为符合火球前向激波模型；早期光学闪耀可用反向激波解释；部分GRB光变中存在的拐折预示准直的喷流的存在。这些喷流或许在GRB中普遍存在。

    - 发现了多样的长爆：富X射线的GRB， XRF经常被探测到，这些时间似乎形成了一个GRB家族在更软端的连续分布。另外，GRB似乎也分为光学亮和光学暗亮中，且后者占大多数。