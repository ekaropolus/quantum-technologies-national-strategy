---
title: "Quantum Technologies as Strategic Infrastructure: Evidence, Adoption Pathways, and a National Research Agenda for 2025-2035"
author: "Edgar Valdés, Hadox Research Labs"
date: "April 2026"
thanks: "Prepared for the Quantum Technologies track of the twenty-third edition of the Global Information Technology Management Association Annual Conference, Monterrey, Mexico, May 6-8, 2026, for which Edgar Antonio Valdés Porras serves as Track Chair. The author gratefully acknowledges Rogelio Marín and the Centro de Investigación en Matemáticas, A.C. for intellectual support and institutional context. All interpretations and remaining errors are the author's responsibility."
bibliography: quantum_references.bib
link-citations: true
nocite: |
  @acin2018, @alexeev2021, @arute2019, @barry2016, @bauer2020, @bernstein2017, @beck2024, @bharti2022, @biamonte2017, @bova2020, @bruzewicz2019, @campbell2017, @cao2019, @cerezo2021, @cisaNistNsa2022, @cohen1990, @cranganore2024, @degen2017, @dowling2003, @egger2020, @fowler2012, @georgescu2014, @gidney2021, @giovannetti2011, @harrow2017, @henriet2020, @kandala2017, @kaur2022, @kimble2008, @kjaergaard2020, @krantz2019, @kwon2026, @liu2024, @lundvall1992, @mazzucato2018, @mcclean2018, @montanaro2016, @mosca2018, @nelson1993, @nist2024, @nsa2024, @oecd2025a, @oecd2025b, @oecd2026, @openalex2026, @orus2019, @peruzzo2014, @pezze2018, @pirandola2020, @preskill2018, @proctor2022, @rogers2003, @saffman2016, @schuld2019, @slussarenko2019, @wehner2018, @xu2020
---

## Abstract

Quantum technologies have moved from a predominantly scientific programme into a strategic infrastructure domain affecting computation, sensing, communications, cybersecurity, industrial research, and national innovation policy. The 2025-2035 adoption horizon is examined through an integrative synthesis of the quantum information science literature, innovation systems theory, enterprise-adoption research, OECD national strategy data, OECD-EPO patent mapping, OpenAlex bibliometric indicators, NIST standards, high-performance computing (HPC) integration studies, and public readiness surveys. The analysis finds that quantum adoption is not a single market transition but a layered capability transition: post-quantum cryptography and selected quantum sensing applications already have institutional relevance; quantum communication develops through specialized network and security testbeds; and general-purpose quantum computing remains contingent on error correction, logical-qubit economics, application-level benchmarking, hybrid quantum-classical integration, and the ability to couple quantum processing units to HPC environments. The empirical record shows acceleration as well as structural unevenness. Governments had announced approximately USD 55.7 billion in quantum commitments by October 2025; OECD Fundstat identified USD 11.235 billion PPP in 12,209 quantum-related R&D awards during 2015-2023; OECD-EPO mapping identified 31,700 quantum patent families from 2005-2024; and OpenAlex bibliometrics show a publication geography concentrated in the United States, China, Germany, the United Kingdom, and France. These findings support a shift from hardware-centered readiness metrics toward absorptive capacity: the capacity of firms and states to understand, test, benchmark, procure, secure, regulate, and eventually produce quantum technologies. The article concludes with a staged roadmap, a critique of common adoption errors, and a frontier research agenda for nations seeking long-term technological sovereignty.

**Keywords:** quantum technologies, quantum computing, quantum sensing, post-quantum cryptography, quantum communication, national innovation systems, absorptive capacity, quantum policy, strategic infrastructure

## 1. Introduction

The term "quantum technology" now carries two different meanings. In public discourse it is often used as a synonym for quantum computing, accompanied by claims that quantum processors will soon transform every computational problem. In the research literature it denotes a broader family of technologies that exploit controlled quantum states for computation, measurement, communication, simulation, timing, and security [@dowling2003; @acin2018]. This distinction is analytically consequential because it changes how adoption, policy, investment, and national strategy are evaluated.

The first quantum revolution produced technologies such as transistors, lasers, magnetic resonance imaging, semiconductor electronics, and atomic clocks. These devices used quantum theory indirectly, often through bulk or statistical properties of matter. The second quantum revolution is different because it seeks direct engineering of individual or collective quantum states, including superposition, entanglement, squeezing, tunneling, and measurement back-action [@dowling2003; @giovannetti2011]. Quantum technologies therefore sit at the boundary between physics and infrastructure. They are scientific instruments, but they are also future components of cybersecurity, finance, telecommunications, energy, medicine, logistics, materials discovery, defense, and public administration.

The analysis treats quantum technologies as strategic infrastructure. That framing has three implications. First, quantum technologies are not a single product market. They form a stack of scientific, industrial, software, security, metrology, and governance capabilities. Second, their economic value will not be captured simply by the earliest vendors or by the largest hardware announcements. It will be captured by organizations and countries that develop the capacity to evaluate quantum claims, integrate quantum tools with classical systems, and adapt procurement, standards, talent, and cybersecurity. Third, the most important near-term actions are not always those that sound most futuristic. Post-quantum cryptography (PQC), quantum-safe procurement, quantum sensing pilots, metrology, workforce formation, and cloud-mediated experimentation may produce more strategic value before universal fault-tolerant quantum computing arrives.

Five research questions structure the analysis.

1. What does the scholarly literature imply about the maturity and adoption pathways of quantum computing, sensing, communication, and post-quantum cryptography?
2. What quantitative indicators can be used to estimate global quantum readiness when direct adoption data remain incomplete?
3. How does high-performance computing change the adoption pathway for quantum computing?
4. How can nations and enterprises compare quantum technologies under conditions of technical uncertainty, hype, and geopolitical competition?
5. What are the principal barriers to quantum adoption between 2025 and 2035?
6. What roadmap can guide a nation toward quantum capability without premature lock-in to immature hardware or rhetorical innovation policy?

The argument is intentionally critical. Quantum technologies are real and strategically important, but their adoption is often discussed with weak evidence. Market forecasts can be useful signals, but they are not adoption data. Qubit counts are not system capability. Random-circuit advantage is not automatically commercial value. Quantum key distribution is not a universal replacement for post-quantum cryptography. Quantum machine learning is not automatically superior to classical machine learning. A credible national strategy requires clear separation among scientific possibility, engineering feasibility, organizational readiness, and public value.

## 2. Literature Review and Theoretical Frame

### 2.1 From Quantum Revolution to Infrastructure

The modern quantum technology agenda begins with the claim that individual quantum systems can be engineered as resources rather than treated as unavoidable microscopic phenomena. @dowling2003 described this as the second quantum revolution. The European quantum roadmap later organized the field into quantum communication, quantum computation, quantum simulation, quantum metrology and sensing, quantum control, and quantum software [@acin2018]. This taxonomy remains useful, but national strategy requires an additional classification by adoption readiness, infrastructure burden, security urgency, and dependence on fault tolerance.

Quantum computing receives the most attention because its long-run computational implications are profound. @montanaro2016 shows that quantum algorithms can offer speedups in areas such as search, optimization, simulation, linear systems, and cryptography. @preskill2018 framed the present era as noisy intermediate-scale quantum computing, in which devices are large enough to be scientifically interesting but too noisy for many fault-tolerant algorithms. @bharti2022 and @cerezo2021 show that the near-term algorithmic landscape is dominated by variational and hybrid quantum-classical methods, not by the mature execution of Shor-scale fault-tolerant algorithms. This matters because the route from laboratory device to operational advantage is not a straight line; it runs through error correction, benchmark design, software tooling, and application-specific validation.

Quantum simulation and quantum chemistry provide the clearest intellectual case for future quantum computation because the target systems are themselves quantum mechanical. @georgescu2014 present quantum simulation as a natural application class, while @cao2019 and @bauer2020 review algorithms for chemistry and materials science. Yet even here the adoption problem is not solved by theoretical advantage. Useful workflows require chemical accuracy, problem encoding, error mitigation or correction, validation against experiments, and integration into existing research pipelines.

Quantum sensing follows a different path. @degen2017 define quantum sensing as the use of quantum systems to measure physical quantities with high sensitivity. @giovannetti2011 and @pezze2018 show why entanglement and nonclassical states can improve metrology. Applications such as clocks, magnetometers, gravimeters, inertial sensors, navigation, geodesy, and biomedical sensing do not require universal fault-tolerant quantum computation. This makes sensing a nearer-term adoption domain, although the engineering requirements remain demanding: ruggedization, calibration, cost, environmental stability, field deployment, and integration into domain workflows.

Quantum communication also has a distinct maturity profile. @kimble2008 and @wehner2018 describe the quantum internet as a future network for entanglement distribution, secure communication, distributed sensing, and eventually distributed quantum computation. @pirandola2020 and @xu2020 review quantum cryptography and QKD with realistic devices. The research case is strong, but practical deployment faces distance limits, loss, authentication, trusted nodes, device vulnerabilities, cost, and standards. The result is a specialized infrastructure pathway rather than a universal cybersecurity solution.

PQC is conceptually different from quantum communication. It is classical cryptography designed to resist quantum attacks. @bernstein2017 review the technical foundations of post-quantum cryptography; @mosca2018 frames the cybersecurity problem through the relation between data shelf life, migration time, and the timeline for cryptographically relevant quantum computers. @gidney2021 show why the threat is not imminent in an operational sense but is strategically serious: resource estimates for attacking RSA-2048 require very large fault-tolerant machines, yet the "harvest now, decrypt later" problem begins before those machines exist. This makes PQC the clearest near-term national adoption domain.

### 2.2 Adoption Theory: Absorptive Capacity and National Innovation Systems

Quantum adoption is not only a hardware problem. It is an absorptive capacity problem. @cohen1990 define absorptive capacity as the ability to recognize, assimilate, and exploit external knowledge. Quantum technologies require unusually high absorptive capacity because they are difficult to evaluate, require specialized expertise, and depend on complementary assets such as standards, laboratories, software platforms, cryptographic inventories, and procurement rules.

National innovation systems theory reinforces this point. Technological performance depends on networks of universities, firms, public agencies, standards bodies, financial institutions, and industrial users rather than isolated inventions [@lundvall1992; @nelson1993]. Mission-oriented innovation policy adds that governments can shape markets when they define public missions, coordinate capabilities, and create demand for difficult technologies [@mazzucato2018]. Quantum technologies fit this framework because the private sector alone is unlikely to fund all foundational science, cybersecurity transition, standards, workforce development, and testbed infrastructure required for adoption.

Enterprise adoption evidence is beginning to catch up with the physics. @kwon2026 analyze quantum computing adoption intention through expert interviews and a survey of 250 IT decision-makers. They find that perceived quantum advantage, belief in quantum superiority, continuous budget allocation, regulatory support, and co-creation increase adoption intention, while organizational resistance and financial risk reduce it. The result is consistent with the broader innovation diffusion literature: adoption requires not just technological promise but relative advantage, compatibility, trialability, organizational resources, and institutional support [@rogers2003].

### 2.3 The Strategic Error: Confusing Scientific Milestones with Adoption

The quantum field has produced genuine scientific milestones. @arute2019 demonstrated quantum computational advantage on a programmable superconducting processor for a sampling task. @harrow2017 explain why such demonstrations matter for computational complexity. However, scientific advantage and economic advantage are not the same. A random-circuit sampling task can demonstrate that a quantum device is difficult to simulate classically without solving a valuable business problem. This is not a criticism of the science; it is a warning against using the wrong inference for policy.

The same distinction applies to quantum machine learning. @biamonte2017 and @schuld2019 identify plausible quantum machine learning mechanisms, especially through feature maps and Hilbert-space representations. @mcclean2018, however, identify barren plateaus as a serious training obstacle. For enterprise strategy, the relevant question is not whether a circuit is quantum, but whether it improves accuracy, time-to-solution, energy consumption, robustness, interpretability, or cost relative to the best classical baseline.

## 3. Data and Methods

### 3.1 Research Design

The study is designed as an integrative research synthesis. This design is appropriate because the object of inquiry is not a single empirical estimate but a strategic interpretation of a heterogeneous evidence base. The evidentiary corpus includes quantum information science, innovation theory, policy reports, open bibliometric data, patent mapping, standards documents, and business-readiness surveys.

The methodology follows four steps. First, the literature was organized into seven domains: quantum computing, quantum sensing, quantum communication, PQC, high-performance computing integration, innovation/adoption theory, and national policy. Second, each domain was evaluated according to technology readiness, adoption barriers, infrastructure requirements, and relevance to national strategy. Third, quantitative adoption proxies were assembled from OECD, OECD-EPO, OpenAlex, NIST, and readiness survey sources.[^adoption-proxies] Fourth, the evidence was translated into a strategic roadmap and a set of decision criteria for nations and enterprises.

[^adoption-proxies]: Adoption proxies are used because comprehensive public data on direct quantum deployment remain unavailable. They measure different dimensions of readiness and are not treated as interchangeable indicators.

The design is not a systematic review in the narrow PRISMA sense, since the objective is not to estimate an effect size across comparable empirical studies. It is a structured narrative review and evidence synthesis of an emerging technology field in which relevant evidence comes from physics, computer science, cybersecurity, policy, and management research. The inclusion criteria prioritized major review articles, highly cited foundational papers, empirical adoption studies, standards-relevant cybersecurity literature, and recent policy datasets from public institutions.

### 3.2 Source Selection

The scholarly corpus was drawn from journals and proceedings in physics, computer science, engineering, cryptography, management, and innovation policy. It includes work published in *Reviews of Modern Physics*, *Nature*, *Nature Reviews Physics*, *Nature Communications*, *Physical Review Letters*, *Physical Review A*, *PRX Quantum*, *npj Quantum Information*, *Quantum*, *Chemical Reviews*, *Applied Physics Reviews*, *Annual Review of Condensed Matter Physics*, *IEEE Transactions on Quantum Engineering*, *IEEE Security & Privacy*, *International Journal of Information Management*, *Administrative Science Quarterly*, and *Industrial and Corporate Change*.

The quantitative layer uses public datasets and official sources. OECD national strategy material provides estimates of public commitments and governance models. OECD Fundstat provides project-award evidence. OECD-EPO mapping provides patent-family evidence. OpenAlex provides publication and country-affiliation proxies. NIST, NSA, and CISA provide standards and cybersecurity guidance. These sources are not treated as interchangeable. Funding measures state commitment; patents measure invention and appropriation; publications measure scientific absorptive capacity; standards measure institutional readiness; surveys measure organizational preparation.

### 3.3 Bibliometric Extraction

OpenAlex data were extracted for 2015-2025 using the concepts "Quantum technology" (C190463098) and "Post-quantum cryptography" (C108277079), grouped by publication year and institutional country. The quantum technology query returned 15,279 works in the extracted concept set. The leading country affiliations were the United States (2,584), China (1,641), Germany (1,225), the United Kingdom (1,102), France (607), Italy (552), India (551), Japan (519), Canada (463), and Australia (438). Mexico appeared with 56 works. The post-quantum cryptography query showed a different distribution: the United States (168), India (163), China (132), the United Kingdom (61), Germany (60), Japan (52), France (42), Korea (36), Spain (30), and Russia (29) led the extracted country counts; Mexico appeared with 5 works.

These counts are used cautiously. OpenAlex concept assignment, affiliation metadata, co-authorship, and indexing practices affect results. The 2025 quantum technology count is especially high relative to prior years; the year trend is therefore interpreted as a query-index indicator rather than a precise measurement of annual global production. The country counts are more useful as a broad proxy for scientific absorptive capacity.

![Global distribution of quantum-technology publication capacity. OpenAlex country-affiliation counts for the concept "Quantum technology" show a concentrated geography led by the United States, China, Germany, the United Kingdom, and France, with Mexico included as a comparison case. Counts are bibliometric proxies rather than direct deployment measures.](figures/fig1_global_country_distribution.png){width=95%}

![Indexed publication trajectory for quantum technology and post-quantum cryptography. OpenAlex annual counts are indexed to 2015=100 to compare differently sized literatures. The 2025 quantum-technology spike is interpreted as a query and indexing signal requiring cautious interpretation.](figures/fig2_publication_trends.png){width=95%}

## 4. Quantitative Evidence: What Can Be Measured

No comprehensive public database currently measures global quantum adoption directly. There is no single dataset covering deployed quantum sensors, QKD links, PQC migrations, enterprise pilots, QCaaS usage, cloud experiments, and quantum software workflows. The evidence is therefore triangulated across multiple proxies.

| Evidence layer | Quantitative signal | Interpretation |
| --- | --- | --- |
| Public commitments | OECD reports approximately USD 55.7 billion in announced public quantum commitments worldwide since 2013, as of October 2025 | Quantum has become a state-level strategic technology |
| Public R&D awards | OECD Fundstat identifies USD 11.235 billion PPP across 12,209 quantum-related R&D awards, 2015-2023 | Public investment is organized through research and mission programmes |
| Patent families | OECD-EPO mapping identifies 31,700 quantum patent families with earliest publication years 2005-2024; quantum patenting increased sevenfold between 2005 and 2024 and grew at about 20 percent CAGR since 2014 | Invention is accelerating but geographically concentrated |
| Publications | OpenAlex "Quantum technology" query returns 15,279 works, 2015-2025; top countries are the United States, China, Germany, the United Kingdom, and France | Scientific absorptive capacity is unevenly distributed |
| PQC publications | OpenAlex PQC query shows the United States, India, and China as leading country affiliations | PQC readiness depends on cryptographic and software capacity, not only physics hardware |
| Business readiness | OECD summarizes surveys in which expected disruption is high but planning, budgets, and use-case identification are low | Awareness does not equal readiness |
| Standards | NIST finalized ML-KEM, ML-DSA, and SLH-DSA in 2024 | PQC migration has become an implementation agenda |

The strongest pattern is not simple growth. It is uneven capability formation. Public funding is rising, patenting is accelerating, and publications are concentrated in a small set of countries. At the same time, enterprise readiness remains weak. In the OECD readiness evidence, 97 percent of UK executives in one survey expected quantum disruption, but only about one-third had begun readiness planning; 87 percent of financial-sector respondents in another survey viewed quantum as an opportunity, while 73 percent lacked a commercial-advantage use case and 87 percent lacked a dedicated budget; ISACA evidence summarized by OECD found that only 20 percent of respondents had formal quantum readiness plans despite broad expectations of impact [@oecd2026].

This is the adoption gap. Countries and firms are hearing the quantum narrative, but many have not built the mechanisms required to act on it. The gap is not a public-relations problem. It is a capability problem.

![Awareness-readiness gap in quantum computing adoption. Survey evidence summarized by OECD indicates that high expected impact coexists with substantially lower levels of planning, use-case definition, and dedicated budget formation.](figures/fig3_readiness_gap.png){width=95%}

## 5. Results: Adoption Pathways by Technology Domain

### 5.1 Quantum Computing: High Optionality, Low Near-Term Certainty

Quantum computing has the largest long-term strategic upside and the greatest adoption uncertainty. Its theoretical foundation is strong. Quantum algorithms can offer asymptotic speedups in specific problem classes [@montanaro2016]. Quantum simulation and chemistry are natural targets because classical computers struggle with the exponential structure of many quantum systems [@georgescu2014; @cao2019; @bauer2020]. Hybrid variational algorithms offer near-term experimental pathways [@peruzzo2014; @kandala2017; @cerezo2021; @bharti2022].

The hard constraint is that most valuable applications require deeper circuits, lower logical error rates, and better verification than current devices provide. Fault tolerance remains the transition point from experimental devices to reliable infrastructure. Surface codes provide a leading approach because they are compatible with two-dimensional local interactions, but they impose large overheads [@fowler2012; @campbell2017]. Resource estimates for cryptographically relevant machines remain high, even when improved algorithms reduce requirements [@gidney2021].

The adoption implication is that quantum computing functions in the near term as a learning, benchmarking, and option-value domain. The most rational enterprise and national actions are not mass deployment but targeted experimentation, workforce formation, algorithmic evaluation, access to QCaaS platforms, and careful benchmarking against classical alternatives.

### 5.2 Quantum Sensing: The Most Immediate Public-Value Domain

Quantum sensing is the strongest near-term application domain because it can produce value without universal fault-tolerant quantum computers. It uses quantum systems as measurement devices: atomic clocks for timing, magnetometers for magnetic fields, gravimeters for subsurface mapping, inertial sensors for navigation, and quantum defects in diamond for local magnetic sensing [@degen2017; @barry2016]. The underlying value proposition is not "faster computation" but improved information about the physical world.

The distinction is important for public policy. Many countries have urgent problems in water, infrastructure, mining, health, energy, navigation, border monitoring, seismic risk, environmental monitoring, and industrial quality control. Quantum sensing can be linked to these missions earlier than quantum computing can be linked to general enterprise transformation. The barrier is not theoretical uncertainty but field deployment: instruments require ruggedization, calibration, cost-effectiveness, interoperability, and operational relevance.

### 5.3 Quantum Communication: Strategic, Specialized, and Infrastructure-Heavy

Quantum communication has strong long-term strategic significance, especially for entanglement distribution, secure links, distributed sensing, and future quantum networks [@kimble2008; @wehner2018]. QKD has already moved beyond pure laboratory demonstration, and the security literature has become sophisticated about realistic devices, side channels, and measurement-device-independent protocols [@pirandola2020; @xu2020].

The critique is equally important. QKD does not remove the need for authentication, endpoint security, network engineering, procurement standards, or cost-benefit analysis. It requires specialized infrastructure and can be limited by loss, distance, trusted-node assumptions, and device assurance. Quantum repeaters are the network analog of fault tolerance: without reliable repeaters, memories, entanglement swapping, and low-loss interfaces, large-scale quantum networks remain constrained.

Consequently, quantum communication is best pursued through targeted testbeds and high-value links rather than broad claims that it will replace existing cybersecurity. Its national value lies in strategic learning, telecom experimentation, high-assurance niches, and preparation for future quantum networks.

### 5.4 Post-Quantum Cryptography: The First National Adoption Mandate

PQC is the most urgent adoption domain because it addresses a real security transition that can begin before cryptographically relevant quantum computers exist. Shor's algorithm threatens RSA, Diffie-Hellman, and elliptic-curve cryptography once large fault-tolerant machines exist. The relevant risk is not only future attack; it is present-day collection of long-lived encrypted data [@mosca2018]. NIST's 2024 standards give organizations a concrete migration target, especially ML-KEM, ML-DSA, and SLH-DSA [@nist2024].

The hard part is not choosing an algorithm in isolation. Migration requires cryptographic inventories, crypto-agility, vendor coordination, protocol testing, legacy system replacement, procurement language, compliance governance, and prioritization by data shelf life. PQC is therefore a digital-infrastructure programme. Treating it as a narrow cybersecurity patch underestimates the institutional work involved.

## 6. Hardware Comparison and Logical-Qubit Economics

No hardware modality has won. Each platform expresses a different engineering bargain.

| Modality | Strength | Bottleneck | Strategic interpretation |
| --- | --- | --- | --- |
| Superconducting qubits | Fast gates, strong industrial ecosystem, microfabrication path, cloud availability | Cryogenic wiring, dielectric loss, crosstalk, thermal load, calibration | Strong near-term platform, but scale depends on control and error correction economics |
| Trapped ions | High fidelity, long coherence, natural qubit uniformity, flexible connectivity | Gate speed, shuttling, heating, laser/control complexity | Excellent quality, but engineering scale and throughput remain central questions |
| Neutral atoms | Large arrays, reconfigurable geometry, promising scalability | Atom loss, leakage, gate fidelity, readout, optical control | Strong option for simulation and scaling, with open questions about fault-tolerant architecture |
| Photonics | Natural communication medium, room-temperature potential, networking compatibility | Photon loss, deterministic gates, source and detector integration | Strategically important for networks and some computing architectures |
| Quantum annealing | Available systems and optimization experiments | Limited universality, benchmark ambiguity, mapping overhead | Useful for experimentation when benchmarked against classical heuristics |

Superconducting platforms have advanced rapidly and are reviewed in detail by @krantz2019 and @kjaergaard2020. Trapped-ion systems are reviewed by @bruzewicz2019. Neutral atom systems are reviewed by @saffman2016 and @henriet2020. Photonic systems are reviewed by @slussarenko2019. The comparison shows why qubit count alone is a weak metric. A device with more physical qubits may be less valuable than a smaller device with better gate fidelity, lower correlated noise, better connectivity, or a clearer route to logical error suppression.

The strategic metric is logical-qubit economics. A useful quantum computer will not be defined by the number of physical qubits it contains. It will be defined by the cost, reliability, and speed of logical operations. Relevant metrics include logical error rate, code distance, cycle time, decoding latency, leakage, connectivity, calibration stability, circuit depth at useful fidelity, energy cost, and physical resources per logical qubit. @proctor2022 argue that quantum computer capability is measured by the programmes a processor can run successfully, not by a single scalar benchmark. This is the standard required for policy and procurement.

## 7. Application Domains: Promise, Evidence, and Critique

### 7.1 Chemistry and Materials

Chemistry and materials science remain the strongest long-run application case. Quantum computers may eventually simulate molecular and materials systems more naturally than classical machines [@georgescu2014; @cao2019; @bauer2020]. Potential applications include catalysts, batteries, pharmaceuticals, high-temperature superconductors, corrosion, fertilizers, polymers, semiconductors, and carbon capture.

The critique is that scientific relevance does not automatically produce industrial adoption. A useful workflow improves a decision in drug discovery, materials design, or manufacturing. It produces accuracy that matters, integrates with laboratory experiments, and reduces time or cost. The adoption pathway is therefore hybrid: quantum algorithms, classical high-performance computing, AI models, experiments, and domain experts working together.

### 7.2 Optimization

Optimization is often cited as the earliest commercial opportunity, but it is also the easiest area to overstate. Logistics, portfolio optimization, scheduling, grid management, and supply chains are valuable, but classical optimization is extraordinarily strong. Mixed-integer programming, constraint programming, heuristics, approximation algorithms, GPUs, and domain-specific solvers already perform well. A quantum optimization claim is credible only when it beats the best classical baseline on a relevant instance at a relevant cost.

The more realistic near-term role is exploratory: quantum annealing, QAOA-like workflows, and quantum-inspired methods can help identify problem classes and software practices. They are not general replacements for operations research.

### 7.3 Finance

Finance is attractive because small improvements in risk, optimization, sampling, or pricing can create large value. @orus2019 and @egger2020 review potential finance applications including portfolio optimization, Monte Carlo acceleration, risk analysis, credit scoring, and derivatives pricing. The most serious institutions will not ask whether quantum computing is fashionable. They will ask whether it improves model quality, speed, regulatory auditability, and capital allocation compared with classical methods.

### 7.4 Machine Learning and AI

Quantum machine learning is intellectually rich but commercially immature. @biamonte2017 identify reasons quantum systems may support useful learning models. @schuld2019 connect quantum feature maps with kernel methods. @mcclean2018 show that training can fail through barren plateaus. The resulting policy advice is straightforward: QML belongs in the research portfolio, not in exaggerated enterprise transformation claims. The near-term value may come more from AI improving quantum systems - calibration, error mitigation, pulse design, materials discovery, and control - than from quantum systems improving mainstream AI.

### 7.5 Cybersecurity

Cybersecurity is the most immediate cross-sectoral application because PQC migration affects almost every digital system. The core policy issue is time. Data requiring confidentiality for 10, 20, or 30 years may be vulnerable to future quantum decryption. Large organizations may need many years to inventory and migrate cryptographic assets. If the sum of data shelf life and migration time exceeds the time to a cryptographically relevant quantum computer, action is late by definition [@mosca2018].

## 8. High-Performance Computing and Quantum Computing

The adoption pathway for quantum computing is inseparable from high-performance computing. Quantum computers are unlikely to replace classical supercomputers as general-purpose machines. The more plausible transition is an accelerator model in which quantum processing units are integrated into heterogeneous HPC environments alongside CPUs, GPUs, storage systems, workflow managers, schedulers, and scientific software stacks. In this architecture, quantum computation is invoked only for subroutines where a quantum representation may improve simulation, sampling, optimization, or linear-algebra tasks, while classical HPC performs data preparation, orchestration, error mitigation, optimization loops, verification, and post-processing.

Recent HPC-QC research reflects this transition. @cranganore2024 formalize hybrid quantum-classical scientific workflows and identify workflow-management requirements for mapping classical scientific pipelines onto hybrid resources. @beck2024 frame quantum computing as a computational accelerator within scientific HPC ecosystems, emphasizing hardware-agnostic integration, benchmarks, user interfaces, and workflow management. @liu2024 develop a quantum-centric HPC perspective for quantum chemistry, where quantum algorithms, quantum emulators, and classical HPC resources jointly support chemical simulation. This literature shifts the question from "when will quantum computers replace supercomputers?" to "which components of a scientific workflow can be delegated to a QPU under realistic latency, noise, queueing, and verification constraints?"

The HPC view changes four elements of quantum strategy. First, it changes infrastructure. A useful quantum computing ecosystem requires not only QPUs and cloud accounts, but also schedulers, middleware, compilers, error-mitigation software, data movement protocols, provenance systems, reproducibility controls, and interfaces with existing scientific codes. Second, it changes benchmarking. A quantum subroutine must be evaluated inside a full workflow, including data-loading cost, classical optimization time, queue latency, error-mitigation overhead, and validation against classical HPC baselines. Third, it changes workforce formation. Quantum computing adoption requires computational scientists and HPC engineers who can decompose applications into classical and quantum components, not only physicists who understand qubits. Fourth, it changes national procurement. A country that invests in quantum computing without HPC integration capacity risks buying isolated devices that cannot support scientific or industrial workflows.

The complementarity is especially important for middle-income and emerging quantum economies. Domestic ownership of a leading quantum computer may be unrealistic in the short run, but access to HPC centers, GPU clusters, scientific workflow systems, and cloud-based QPUs can still create meaningful absorptive capacity. The strategic objective is therefore not a binary transition from HPC to quantum computing. It is the construction of an HPC-QC continuum in which classical supercomputing remains the operational substrate and quantum computing enters as a specialized accelerator when evidence justifies it.

## 9. Comparative National Strategy

Different national models reveal different strategic theories.

The United States combines federal coordination, national laboratories, universities, venture capital, major cloud platforms, and defense-linked research. Its advantage is ecosystem diversity and private capital depth. Its weakness is fragmentation and uneven translation across agencies and sectors.

China has emphasized state-directed investment, secure communication infrastructure, and technological self-reliance. Its advantage is coordination and strategic focus. Its weakness may be lower transparency and a risk of overbuilding symbolic infrastructure before operational value is clear.

Europe emphasizes cross-border coordination, public research networks, standards, and strategic autonomy. Its advantage is institutional coordination and research quality. Its weakness is commercialization speed and fragmentation across national markets.

Middle-income and manufacturing-intensive countries face a different problem. They cannot simply copy the largest programmes. Their strategic opportunity is selective capability building: PQC migration, quantum sensing for public missions, cloud-mediated access to quantum computing, metrology laboratories, workforce networks, and participation in standards. The right goal is not to immediately own every layer of the stack. It is to avoid becoming merely a buyer of quantum technologies designed, benchmarked, and governed elsewhere.

## 10. Toward a National Quantum Capability Model

The evidence supports a capability model with seven pillars.

| Pillar | Core capability | Main institutional question |
| --- | --- | --- |
| Scientific frontier | Research in quantum information, algorithms, metrology, materials, error correction, foundations | Can the country participate in frontier knowledge production? |
| Security transition | PQC migration, crypto-agility, long-lived data protection | Can critical systems remain secure through the quantum transition? |
| Sensing and metrology | Atomic clocks, magnetometry, gravimetry, inertial sensing, calibration | Can quantum measurement solve national problems in territory, water, health, energy, and infrastructure? |
| HPC-QC computing access | QCaaS, HPC integration, hybrid workflows, benchmarks, quantum software | Can institutions learn without premature hardware lock-in while preserving continuity with scientific computing infrastructure? |
| Standards and procurement | Benchmarking, interoperability, vendor evaluation, anti-hype criteria | Can public and private buyers distinguish performance from narrative? |
| Workforce | Researchers, engineers, technicians, cybersecurity professionals, procurement officers | Can the ecosystem build the missing middle between physics PhDs and operational deployment? |
| Industrial position | Components, control systems, photonics, cryogenics, software, sensing integration | Where can domestic firms enter the value chain realistically? |

The workforce pillar deserves emphasis. @kaur2022 show that quantum education initiatives are expanding globally, but the workforce problem is not only a need for more PhDs. Quantum industries require technicians and engineers who can align lasers, operate cryostats, build RF control systems, manage vacuum systems, write firmware, perform calibration, design software interfaces, audit cryptography, and translate domain problems into testable workflows. A nation that trains only researchers but not operators will remain dependent on imported systems.

![Sequencing of national quantum capabilities. The heatmap scores strategic priority across three roadmap phases, emphasizing that PQC, workforce, standards, sensing, QCaaS, communication, and frontier R&D mature on different policy timelines.](figures/fig4_capability_heatmap.png){width=95%}

## 11. Strategic Roadmap, 2025-2035

### 11.1 Phase I: Preparation and Security, 2025-2027

The first phase is not about buying a national quantum computer. It is about becoming a competent adopter. Core institutional actions include a quantum readiness office, cryptographic asset inventories, PQC migration priorities for long-lived data, procurement language for quantum-safe systems, quantum sensing feasibility studies, QCaaS access for universities and agencies, HPC-QC workflow training, and workforce modules for engineers, cybersecurity professionals, and public-sector decision makers.

The measurable outputs are not press releases. They are inventories, trained personnel, use-case pipelines, testable requirements, procurement standards, and baseline institutional competence.

### 11.2 Phase II: Testbeds and Mission Pilots, 2027-2030

The second phase centers on operational learning. Quantum sensing pilots can be linked to water, energy, health, geodesy, infrastructure, mining, and environmental risk. PQC migration moves from planning to staged implementation. Quantum software testbeds evaluate algorithms against classical baselines. HPC centers test hybrid quantum-classical workflows, including scheduler integration, simulator-to-hardware transition, and workflow provenance. Telecom and research institutions can test QKD and early network components where high-value links justify the cost. Standards laboratories evaluate vendor claims.

The main risk in this phase is quantum washing. Vendors and agencies may label classical, quantum-inspired, or immature systems as strategic breakthroughs. The protection is benchmark discipline: every pilot requires a classical baseline, a performance metric, a cost metric, a verification method, and a decision rule.

### 11.3 Phase III: Selective Scaling and Frontier Integration, 2030-2035

The third phase scales only what has demonstrated value. Sensing systems that solve mission problems can move into procurement. PQC can become standard across public digital infrastructure. Quantum computing can expand where workflows show credible advantage or where workforce and scientific value justify continued experimentation. National research deepens in error correction, logical qubits, quantum repeaters, device-independent security, quantum metrology, quantum materials, and foundations.

![Roadmap for national quantum capability formation, 2025-2035. The sequence is organized around institutional readiness, operational learning, and selective scaling rather than prediction of a single hardware breakthrough.](figures/fig5_roadmap_timeline.png){width=95%}

The strategic objective is optionality. By 2035, the successful nation is not necessarily the one with the largest announced quantum computer. It is the one with trained people, secure cryptography, functioning testbeds, standards capacity, metrology capability, domain pilots, international partnerships, and a research base connected to the frontier.

## 12. Frontier Research Agenda

National quantum strategy includes frontier topics that are not immediately commercial. These areas generate instruments, expertise, and long-term autonomy.

**Logical-qubit economics.** Research moves from physical qubit counts to logical operation cost. This includes error correction, decoders, leakage management, magic-state overhead, qLDPC codes, and architecture-specific resource estimates.

**Quantum network break-even.** Quantum repeaters, memories, transducers, and entanglement swapping are the network equivalent of fault tolerance. The milestone is not a laboratory link alone; it is performance beyond direct transmission under realistic cost and reliability constraints.

**Quantum sensing for national missions.** Research connects gravimetry, magnetometry, timing, and inertial sensing to real public problems. The central question is not maximum sensitivity in isolation, but operational value under field conditions.

**Benchmark science.** Nations need independent capability to test quantum claims. This includes randomized benchmarking, application-level benchmarks, error characterization, reproducibility, and cost-based performance metrics [@proctor2022; @alexeev2021].

**Quantum foundations as instrumentation strategy.** Foundational work on contextuality, measurement, macroscopic superposition, decoherence, and non-Markovian noise is not merely philosophical. It drives instrumentation in interferometry, isolation, optics, cryogenics, detectors, and control.

**AI for quantum systems.** AI may be most valuable as a tool for quantum engineering: calibration, control, error mitigation, materials discovery, scheduling, pulse optimization, and interpretation of sensor data.

## 13. Discussion: What a Serious Quantum Strategy Must Avoid

The first error is waiting. Waiting for fault-tolerant machines before preparing for PQC, workforce, standards, and sensing would leave institutions unprepared when adoption pressure rises. Readiness takes years.

The second error is hardware nationalism without capability. Buying or announcing a domestic quantum computer does not create a quantum ecosystem if there are no trained operators, no benchmarking laboratory, no software pipeline, no procurement discipline, and no mission demand.

The third error is confusing QKD with PQC. QKD may be valuable for specialized links and research networks, but PQC is the broad migration path for existing digital systems. Treating QKD as a general substitute for PQC misreads both the technology and the infrastructure problem.

The fourth error is treating QCaaS as neutral access. Cloud access democratizes experimentation, but it can also concentrate platform power. The cloud provider may control developer tools, backend access, pricing, data policies, and enterprise relationships. Nations need QCaaS access, but they also need sovereignty over knowledge, benchmarks, critical data governance, and the ability to connect quantum experiments to domestic HPC infrastructure.

The fifth error is accepting quantum advantage claims without baselines. A credible claim specifies the problem class, classical baseline, hardware assumptions, error model, verification method, time-to-solution, energy cost, and economic relevance. Without these elements, the claim is not a procurement basis.

The sixth error is underfunding the missing middle. Quantum strategy often funds elite research and startup promotion while ignoring technicians, engineers, standards experts, cybersecurity auditors, and procurement professionals. These roles determine whether science becomes infrastructure.

## 14. Policy and Enterprise Recommendations

For national governments, the first recommendation is to create a quantum readiness function with authority across science, economy, cybersecurity, defense, education, standards, and public procurement. Fragmented committees are insufficient if they cannot set priorities or coordinate budgets.

Second, PQC migration is critical digital infrastructure. The correct unit of work is not only algorithm selection. It is asset inventory, data-shelf-life classification, crypto-agility, vendor management, testing, staged migration, and compliance.

Third, quantum sensing is best funded through mission pilots. Water, energy, health, territory, infrastructure, mining, navigation, and environmental monitoring offer public-value use cases where better measurement can change decisions.

Fourth, quantum computing policy emphasizes HPC integration, access, benchmarks, and talent before domestic hardware lock-in. QCaaS, shared testbeds, open software, and hybrid workflow managers can build competence while hardware trajectories remain uncertain.

Fifth, public procurement requires anti-hype evidence. Every quantum pilot includes a classical baseline, performance metric, cost metric, interoperability requirement, security assessment, and exit criterion.

Sixth, the research system funds frontier science and industrialization together. Error correction, repeaters, metrology, foundations, materials, and control systems are not separate from commercialization; they are the base from which commercialization will emerge.

For enterprises, the first step is not a large quantum transformation programme. It is a small readiness portfolio: identify high-value problems, map cryptographic risk, train technical staff, test QCaaS workflows, track standards, and join consortia. Investment is justified when a quantum method improves a decision, not when it improves a narrative.

## 15. Conclusion

Quantum technologies will shape the next decade less through sudden universal disruption than through uneven capability formation. PQC is already a cybersecurity migration problem. Quantum sensing can produce public and industrial value before fault-tolerant computing. Quantum communication is strategically important but infrastructure-heavy. Quantum computing remains the largest long-term opportunity, but its value depends on logical-qubit economics, verified advantage, and integration with classical workflows.

The most important conclusion is that quantum readiness is a national capability, not a hardware purchase. Countries that build cryptographic migration capacity, sensing pilots, standards laboratories, workforce pathways, QCaaS competence, and frontier research networks will be positioned to adopt whichever hardware modalities mature. Countries that wait for the market to deliver finished quantum products will become dependent buyers.

The future of quantum technologies therefore requires disciplined ambition. The ambition is to build scientific and technological sovereignty in a field that will affect security, measurement, computation, and industrial discovery. The discipline is evidentiary: rigorous science, reproducible benchmarks, classical baselines, operational pilots, and transparent procurement. Quantum strategy succeeds when it turns fragile quantum effects into reliable public capability.

## Acknowledgments

This manuscript was prepared for the Quantum Technologies track of the twenty-third edition of the Global Information Technology Management Association Annual Conference, Monterrey, Mexico, May 6-8, 2026. The author acknowledges his role as Track Chair for Quantum Technologies and gratefully acknowledges Rogelio Marín and the Centro de Investigación en Matemáticas, A.C. for intellectual support and institutional context. All interpretations and remaining errors are the author's responsibility.

## Data Availability

The quantitative tables generated for this manuscript are deposited in the companion research repository. They include OpenAlex country and year counts for the concepts "Quantum technology" and "Post-quantum cryptography" for 2015-2025. OECD, NIST, NSA, CISA, OECD-EPO, and market-readiness data are cited to public sources in the reference list. The OpenAlex queries used concept IDs `C190463098` and `C108277079`, grouped by publication year and institutional country.

## Code Availability

The companion research repository is available at https://github.com/ekaropolus/quantum-technologies-national-strategy. It contains the source manuscripts, processed data, BibTeX bibliography, figure-generation code, and reproducible build script used to generate the manuscript outputs. The repository is intended to support inspection of the OpenAlex extracts, regeneration of figures, and reconstruction of the PDF, TeX, and DOCX versions from the manuscript sources.

## Author Contributions

Edgar Valdés conceptualized the manuscript, directed the research synthesis, interpreted the evidence, and prepared the manuscript.

## Funding

No external funding was declared for this manuscript.

## Competing Interests

The author declares no competing interests.

## Limitations

The analysis relies on adoption proxies rather than direct global deployment data. Funding, patents, publications, standards, and readiness surveys measure different dimensions of quantum capacity and are not interchangeable. OpenAlex counts depend on concept assignment, institutional metadata, and indexing practices. Market forecasts are treated only as directional evidence. A future empirical extension would require interviews with government agencies, infrastructure operators, quantum vendors, cybersecurity teams, and enterprise adopters, plus a structured survey of quantum readiness across sectors.

## References

::: {#refs}
:::
