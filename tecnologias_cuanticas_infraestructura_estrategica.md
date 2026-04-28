---
title: "Tecnologías cuánticas como infraestructura estratégica: evidencia, rutas de adopción y una agenda nacional de investigación para 2025-2035"
author: "Edgar Valdés, Hadox Research Labs"
date: "Abril de 2026"
lang: es-MX
thanks: "Preparado para el track de Tecnologías Cuánticas de la vigésima tercera edición de la Conferencia Anual de la Global Information Technology Management Association, Monterrey, México, 6-8 de mayo de 2026, en la cual Edgar Antonio Valdés Porras participa como Track Chair. El autor agradece a Rogelio Marín y al Centro de Investigación en Matemáticas, A.C. por el apoyo intelectual y el contexto institucional. Todas las interpretaciones y errores remanentes son responsabilidad del autor."
bibliography: quantum_references.bib
link-citations: true
nocite: |
  @acin2018, @alexeev2021, @arute2019, @barry2016, @bauer2020, @bernstein2017, @beck2024, @bharti2022, @biamonte2017, @bova2020, @bruzewicz2019, @campbell2017, @cao2019, @cerezo2021, @cisaNistNsa2022, @cohen1990, @cranganore2024, @degen2017, @dowling2003, @egger2020, @fowler2012, @georgescu2014, @gidney2021, @giovannetti2011, @harrow2017, @henriet2020, @kandala2017, @kaur2022, @kimble2008, @kjaergaard2020, @krantz2019, @kwon2026, @liu2024, @lundvall1992, @mazzucato2018, @mcclean2018, @montanaro2016, @mosca2018, @nelson1993, @nist2024, @nsa2024, @oecd2025a, @oecd2025b, @oecd2026, @openalex2026, @orus2019, @peruzzo2014, @pezze2018, @pirandola2020, @preskill2018, @proctor2022, @rogers2003, @saffman2016, @schuld2019, @slussarenko2019, @wehner2018, @xu2020
---

## Resumen

Las tecnologías cuánticas han pasado de ser un programa predominantemente científico a constituir un dominio de infraestructura estratégica que afecta la computación, la sensórica, las comunicaciones, la ciberseguridad, la investigación industrial y la política nacional de innovación. Este artículo examina el horizonte de adopción 2025-2035 mediante una síntesis integradora de la literatura en ciencia de la información cuántica, teoría de sistemas de innovación, investigación sobre adopción empresarial, datos de estrategias nacionales de la OCDE, mapeo de patentes OCDE-OEP, indicadores bibliométricos de OpenAlex, estándares del NIST, estudios sobre integración con cómputo de alto desempeño (HPC) y encuestas de preparación institucional. El análisis muestra que la adopción cuántica no es una transición de mercado única, sino una transición estratificada de capacidades: la criptografía post-cuántica y ciertas aplicaciones de sensórica cuántica ya poseen relevancia institucional; la comunicación cuántica avanza mediante redes especializadas y bancos de prueba de seguridad; y la computación cuántica de propósito general sigue dependiendo de la corrección de errores, la economía de qubits lógicos, la evaluación comparativa a nivel de aplicación, la integración híbrida cuántico-clásica y la capacidad de acoplar unidades de procesamiento cuántico a entornos HPC. La evidencia empírica revela aceleración, pero también desigualdad estructural. Para octubre de 2025, los gobiernos habían anunciado compromisos públicos cuánticos por aproximadamente USD 55.7 mil millones; Fundstat de la OCDE identificó USD 11.235 mil millones PPP en 12,209 apoyos de I+D relacionados con tecnologías cuánticas durante 2015-2023; el mapeo OCDE-OEP identificó 31,700 familias de patentes cuánticas entre 2005 y 2024; y la bibliometría de OpenAlex muestra una geografía de publicaciones concentrada en Estados Unidos, China, Alemania, Reino Unido y Francia. Estos hallazgos apoyan un desplazamiento desde métricas de preparación centradas en hardware hacia la capacidad de absorción: la capacidad de empresas y Estados para entender, probar, comparar, adquirir, asegurar, regular y eventualmente producir tecnologías cuánticas. El artículo concluye con una hoja de ruta por etapas, una crítica de errores comunes de adopción y una agenda de investigación de frontera para naciones que buscan soberanía tecnológica de largo plazo.

**Palabras clave:** tecnologías cuánticas, computación cuántica, sensórica cuántica, criptografía post-cuántica, comunicación cuántica, sistemas nacionales de innovación, capacidad de absorción, política cuántica, infraestructura estratégica

## 1. Introducción

El término "tecnología cuántica" tiene hoy dos significados distintos. En el discurso público suele usarse como sinónimo de computación cuántica, acompañado de afirmaciones según las cuales los procesadores cuánticos transformarán pronto todo problema computacional. En la literatura de investigación, en cambio, designa una familia más amplia de tecnologías que explotan estados cuánticos controlados para computación, medición, comunicación, simulación, temporización y seguridad [@dowling2003; @acin2018]. Esta distinción es analíticamente decisiva porque modifica la forma en que se evalúan la adopción, la política pública, la inversión y la estrategia nacional.

La primera revolución cuántica produjo tecnologías como transistores, láseres, imagen por resonancia magnética, electrónica de semiconductores y relojes atómicos. Estos dispositivos usaban la teoría cuántica de forma indirecta, a menudo mediante propiedades estadísticas o colectivas de la materia. La segunda revolución cuántica es distinta porque busca la ingeniería directa de estados cuánticos individuales o colectivos, incluyendo superposición, entrelazamiento, compresión cuántica, tunelamiento y retroacción de medición [@dowling2003; @giovannetti2011]. Por ello, las tecnologías cuánticas se ubican en la frontera entre física e infraestructura. Son instrumentos científicos, pero también componentes futuros de la ciberseguridad, las finanzas, las telecomunicaciones, la energía, la medicina, la logística, el descubrimiento de materiales, la defensa y la administración pública.

El análisis trata las tecnologías cuánticas como infraestructura estratégica. Este encuadre tiene tres implicaciones. Primero, las tecnologías cuánticas no constituyen un solo mercado de productos; forman una pila de capacidades científicas, industriales, de software, seguridad, metrología y gobernanza. Segundo, su valor económico no será capturado simplemente por los primeros proveedores ni por los anuncios de hardware más grandes. Será capturado por organizaciones y países que desarrollen la capacidad de evaluar afirmaciones cuánticas, integrar herramientas cuánticas con sistemas clásicos y adaptar compras públicas, estándares, talento y ciberseguridad. Tercero, las acciones más importantes de corto plazo no siempre son las que suenan más futuristas. La criptografía post-cuántica (PQC), las compras públicas cuánticamente seguras, los pilotos de sensórica cuántica, la metrología, la formación de fuerza laboral y la experimentación mediada por la nube pueden producir más valor estratégico antes de que llegue la computación cuántica universal tolerante a fallas.

Seis preguntas de investigación estructuran el análisis.

1. ¿Qué implica la literatura académica sobre la madurez y las rutas de adopción de la computación cuántica, la sensórica, la comunicación y la criptografía post-cuántica?
2. ¿Qué indicadores cuantitativos pueden usarse para estimar la preparación cuántica global cuando los datos directos de adopción siguen incompletos?
3. ¿Cómo modifica el cómputo de alto desempeño la ruta de adopción de la computación cuántica?
4. ¿Cómo pueden las naciones y las empresas comparar tecnologías cuánticas bajo condiciones de incertidumbre técnica, exageración comercial y competencia geopolítica?
5. ¿Cuáles son las principales barreras para la adopción cuántica entre 2025 y 2035?
6. ¿Qué hoja de ruta puede guiar a una nación hacia capacidades cuánticas sin encierro prematuro en hardware inmaduro ni política de innovación puramente retórica?

El argumento es deliberadamente crítico. Las tecnologías cuánticas son reales y estratégicamente importantes, pero su adopción suele discutirse con evidencia débil. Los pronósticos de mercado pueden ser señales útiles, pero no son datos de adopción. El conteo de qubits no equivale a capacidad de sistema. La ventaja en circuitos aleatorios no implica automáticamente valor comercial. La distribución cuántica de claves no reemplaza de forma universal a la criptografía post-cuántica. El aprendizaje automático cuántico no es automáticamente superior al aprendizaje automático clásico. Una estrategia nacional creíble requiere separar con claridad la posibilidad científica, la factibilidad de ingeniería, la preparación organizacional y el valor público.

## 2. Revisión de literatura y marco teórico

### 2.1 De la revolución cuántica a la infraestructura

La agenda moderna de tecnología cuántica comienza con la afirmación de que los sistemas cuánticos individuales pueden ser diseñados como recursos, en vez de tratarse como fenómenos microscópicos inevitables. @dowling2003 describieron este proceso como la segunda revolución cuántica. La hoja de ruta cuántica europea organizó posteriormente el campo en comunicación cuántica, computación cuántica, simulación cuántica, metrología y sensórica cuánticas, control cuántico y software cuántico [@acin2018]. Esta taxonomía sigue siendo útil, pero la estrategia nacional requiere una clasificación adicional por preparación para la adopción, carga infraestructural, urgencia de seguridad y dependencia de tolerancia a fallas.

La computación cuántica recibe la mayor atención porque sus implicaciones computacionales de largo plazo son profundas. @montanaro2016 muestra que los algoritmos cuánticos pueden ofrecer aceleraciones en clases específicas de problemas, como búsqueda, optimización, simulación, sistemas lineales y criptografía. @preskill2018 caracterizó la era actual como computación cuántica ruidosa de escala intermedia, en la cual los dispositivos son lo suficientemente grandes para ser científicamente interesantes, pero demasiado ruidosos para muchos algoritmos tolerantes a fallas. @bharti2022 y @cerezo2021 muestran que el paisaje algorítmico de corto plazo está dominado por métodos variacionales e híbridos cuántico-clásicos, no por la ejecución madura de algoritmos tolerantes a fallas a escala de Shor. Esto importa porque la ruta desde el dispositivo de laboratorio hasta la ventaja operativa no es lineal: pasa por corrección de errores, diseño de benchmarks, herramientas de software y validación específica por aplicación.

La simulación cuántica y la química cuántica ofrecen el caso intelectual más claro para la computación cuántica futura porque los sistemas objetivo son, ellos mismos, mecánico-cuánticos. @georgescu2014 presentan la simulación cuántica como una clase natural de aplicaciones, mientras que @cao2019 y @bauer2020 revisan algoritmos para química y ciencia de materiales. Aun aquí, sin embargo, la ventaja teórica no resuelve el problema de adopción. Los flujos de trabajo útiles requieren precisión química, codificación del problema, mitigación o corrección de errores, validación contra experimentos e integración con pipelines de investigación existentes.

La sensórica cuántica sigue una ruta distinta. @degen2017 definen la sensórica cuántica como el uso de sistemas cuánticos para medir magnitudes físicas con alta sensibilidad. @giovannetti2011 y @pezze2018 muestran por qué el entrelazamiento y los estados no clásicos pueden mejorar la metrología. Aplicaciones como relojes, magnetómetros, gravímetros, sensores inerciales, navegación, geodesia y sensórica biomédica no requieren computación cuántica universal tolerante a fallas. Esto convierte a la sensórica en un dominio de adopción más cercano, aunque sus requisitos de ingeniería siguen siendo exigentes: robustecimiento, calibración, costo, estabilidad ambiental, despliegue en campo e integración con flujos de trabajo de dominio.

La comunicación cuántica también posee un perfil de madurez distinto. @kimble2008 y @wehner2018 describen el internet cuántico como una red futura para distribución de entrelazamiento, comunicación segura, sensórica distribuida y, eventualmente, computación cuántica distribuida. @pirandola2020 y @xu2020 revisan la criptografía cuántica y QKD con dispositivos realistas. El caso de investigación es sólido, pero el despliegue práctico enfrenta límites de distancia, pérdida, autenticación, nodos confiables, vulnerabilidades de dispositivos, costo y estándares. El resultado es una ruta de infraestructura especializada, no una solución universal de ciberseguridad.

La PQC es conceptualmente distinta de la comunicación cuántica. Es criptografía clásica diseñada para resistir ataques cuánticos. @bernstein2017 revisan sus fundamentos técnicos; @mosca2018 encuadra el problema de ciberseguridad mediante la relación entre vida útil de los datos, tiempo de migración y horizonte de una computadora cuántica criptográficamente relevante. @gidney2021 muestran por qué la amenaza no es inminente en sentido operativo pero sí estratégicamente seria: los estimados para atacar RSA-2048 requieren máquinas tolerantes a fallas muy grandes, pero el problema de "capturar ahora, descifrar después" empieza antes de que esas máquinas existan. Esto convierte a la PQC en el dominio de adopción nacional más claro en el corto plazo.

### 2.2 Teoría de adopción: capacidad de absorción y sistemas nacionales de innovación

La adopción cuántica no es solo un problema de hardware. Es un problema de capacidad de absorción. @cohen1990 definen la capacidad de absorción como la habilidad para reconocer, asimilar y explotar conocimiento externo. Las tecnologías cuánticas requieren una capacidad de absorción inusualmente alta porque son difíciles de evaluar, exigen conocimiento especializado y dependen de activos complementarios como estándares, laboratorios, plataformas de software, inventarios criptográficos y reglas de adquisición.

La teoría de sistemas nacionales de innovación refuerza este punto. El desempeño tecnológico depende de redes de universidades, empresas, agencias públicas, organismos de estandarización, instituciones financieras y usuarios industriales, no de invenciones aisladas [@lundvall1992; @nelson1993]. La política de innovación orientada por misiones añade que los gobiernos pueden moldear mercados cuando definen misiones públicas, coordinan capacidades y crean demanda para tecnologías difíciles [@mazzucato2018]. Las tecnologías cuánticas se ajustan a este marco porque el sector privado por sí solo difícilmente financiará toda la ciencia fundamental, transición de ciberseguridad, estandarización, formación laboral e infraestructura de testbeds requeridas para la adopción.

La evidencia de adopción empresarial empieza a alcanzar a la física. @kwon2026 analizan la intención de adopción de computación cuántica mediante entrevistas con expertos y una encuesta a 250 tomadores de decisión de TI. Encuentran que la ventaja cuántica percibida, la creencia en superioridad cuántica, la asignación continua de presupuesto, el apoyo regulatorio y la co-creación aumentan la intención de adopción, mientras que la resistencia organizacional y el riesgo financiero la reducen. El resultado coincide con la literatura más amplia sobre difusión de innovaciones: la adopción requiere no solo promesa tecnológica, sino ventaja relativa, compatibilidad, capacidad de prueba, recursos organizacionales y apoyo institucional [@rogers2003].

### 2.3 El error estratégico: confundir hitos científicos con adopción

El campo cuántico ha producido hitos científicos genuinos. @arute2019 demostraron ventaja computacional cuántica en un procesador superconductor programable para una tarea de muestreo. @harrow2017 explican por qué estas demostraciones importan para la complejidad computacional. Sin embargo, la ventaja científica y la ventaja económica no son equivalentes. Una tarea de muestreo de circuitos aleatorios puede demostrar que un dispositivo cuántico es difícil de simular clásicamente sin resolver un problema empresarial valioso. Esto no es una crítica a la ciencia; es una advertencia contra el uso de una inferencia equivocada para política pública.

La misma distinción aplica al aprendizaje automático cuántico. @biamonte2017 y @schuld2019 identifican mecanismos plausibles para modelos de aprendizaje cuántico, especialmente mediante mapas de características y representaciones en espacios de Hilbert. @mcclean2018, sin embargo, identifican las mesetas estériles como un obstáculo serio de entrenamiento. Para la estrategia empresarial, la pregunta relevante no es si un circuito es cuántico, sino si mejora precisión, tiempo de solución, consumo energético, robustez, interpretabilidad o costo frente al mejor baseline clásico.

## 3. Datos y métodos

### 3.1 Diseño de investigación

El estudio se diseña como una síntesis integradora de investigación. Este diseño es apropiado porque el objeto de análisis no es una sola estimación empírica, sino una interpretación estratégica de una base de evidencia heterogénea. El corpus incluye ciencia de la información cuántica, teoría de innovación, reportes de política pública, datos bibliométricos abiertos, mapeo de patentes, documentos de estándares y encuestas de preparación empresarial.

La metodología siguió cuatro pasos. Primero, la literatura se organizó en siete dominios: computación cuántica, sensórica cuántica, comunicación cuántica, PQC, integración con cómputo de alto desempeño, teoría de innovación/adopción y política nacional. Segundo, cada dominio fue evaluado según preparación tecnológica, barreras de adopción, requisitos de infraestructura y relevancia para la estrategia nacional. Tercero, se ensamblaron proxies cuantitativos de adopción a partir de fuentes de la OCDE, OCDE-OEP, OpenAlex, NIST y encuestas de preparación.[^adoption-proxies] Cuarto, la evidencia se tradujo en una hoja de ruta estratégica y un conjunto de criterios de decisión para naciones y empresas.

[^adoption-proxies]: Se usan proxies de adopción porque no existen datos públicos completos sobre despliegue cuántico directo. Estos proxies miden dimensiones distintas de preparación y no se tratan como indicadores intercambiables.

El diseño no es una revisión sistemática en el sentido estrecho de PRISMA, pues el objetivo no es estimar un tamaño de efecto a través de estudios empíricos comparables. Es una revisión narrativa estructurada y una síntesis de evidencia de un campo tecnológico emergente en el cual la evidencia relevante proviene de física, ciencias de la computación, ciberseguridad, política pública e investigación en gestión. Los criterios de inclusión priorizaron artículos de revisión importantes, trabajos fundacionales altamente citados, estudios empíricos de adopción, literatura de ciberseguridad relevante para estándares y datasets recientes de instituciones públicas.

### 3.2 Selección de fuentes

El corpus académico se extrajo de revistas y proceedings en física, ciencias de la computación, ingeniería, criptografía, gestión y política de innovación. Incluye trabajos publicados en *Reviews of Modern Physics*, *Nature*, *Nature Reviews Physics*, *Nature Communications*, *Physical Review Letters*, *Physical Review A*, *PRX Quantum*, *npj Quantum Information*, *Quantum*, *Chemical Reviews*, *Applied Physics Reviews*, *Annual Review of Condensed Matter Physics*, *IEEE Transactions on Quantum Engineering*, *IEEE Security & Privacy*, *International Journal of Information Management*, *Administrative Science Quarterly* e *Industrial and Corporate Change*.

La capa cuantitativa utiliza datasets públicos y fuentes oficiales. El material de estrategias nacionales de la OCDE aporta estimaciones de compromisos públicos y modelos de gobernanza. Fundstat de la OCDE aporta evidencia de apoyos a proyectos. El mapeo OCDE-OEP aporta evidencia de familias de patentes. OpenAlex aporta proxies de publicaciones y afiliación por país. NIST, NSA y CISA aportan estándares y orientación de ciberseguridad. Estas fuentes no se tratan como intercambiables. El financiamiento mide compromiso estatal; las patentes miden invención y apropiación; las publicaciones miden capacidad científica de absorción; los estándares miden preparación institucional; las encuestas miden preparación organizacional.

### 3.3 Extracción bibliométrica

Los datos de OpenAlex se extrajeron para 2015-2025 usando los conceptos "Quantum technology" (C190463098) y "Post-quantum cryptography" (C108277079), agrupados por año de publicación y país institucional. La consulta de tecnología cuántica devolvió 15,279 trabajos en el conjunto extraído. Las principales afiliaciones por país fueron Estados Unidos (2,584), China (1,641), Alemania (1,225), Reino Unido (1,102), Francia (607), Italia (552), India (551), Japón (519), Canadá (463) y Australia (438). México apareció con 56 trabajos. La consulta de criptografía post-cuántica mostró una distribución distinta: Estados Unidos (168), India (163), China (132), Reino Unido (61), Alemania (60), Japón (52), Francia (42), Corea (36), España (30) y Rusia (29) encabezaron los conteos; México apareció con 5 trabajos.

Estos conteos se usan con cautela. La asignación de conceptos en OpenAlex, los metadatos de afiliación, la coautoría y las prácticas de indexación afectan los resultados. El conteo de tecnología cuántica de 2025 es especialmente alto frente a años previos; por tanto, la tendencia anual se interpreta como una señal de consulta e indexación, no como una medición precisa de producción global anual. Los conteos por país son más útiles como proxy amplio de capacidad científica de absorción.

![Distribución global de capacidad de publicación en tecnología cuántica. Los conteos de afiliación por país de OpenAlex para el concepto "Quantum technology" muestran una geografía concentrada liderada por Estados Unidos, China, Alemania, Reino Unido y Francia, con México incluido como caso de comparación. Los conteos son proxies bibliométricos, no medidas directas de despliegue.](figures/fig1_global_country_distribution.png){width=95%}

![Trayectoria indexada de publicaciones en tecnología cuántica y criptografía post-cuántica. Los conteos anuales de OpenAlex se indexan a 2015=100 para comparar literaturas de distinto tamaño. El salto de tecnología cuántica en 2025 se interpreta como una señal de consulta e indexación que requiere cautela.](figures/fig2_publication_trends.png){width=95%}

## 4. Evidencia cuantitativa: qué puede medirse

No existe una base pública integral que mida directamente la adopción cuántica global. No hay un solo dataset que cubra sensores cuánticos desplegados, enlaces QKD, migraciones PQC, pilotos empresariales, uso de QCaaS, experimentos en la nube y flujos de trabajo de software cuántico. Por ello, la evidencia se triangula mediante múltiples proxies.

| Capa de evidencia | Señal cuantitativa | Interpretación |
| --- | --- | --- |
| Compromisos públicos | La OCDE reporta aproximadamente USD 55.7 mil millones en compromisos públicos cuánticos anunciados mundialmente desde 2013, a octubre de 2025 | Lo cuántico se ha vuelto una tecnología estratégica de Estado |
| Apoyos públicos a I+D | Fundstat de la OCDE identifica USD 11.235 mil millones PPP en 12,209 apoyos de I+D relacionados con tecnologías cuánticas, 2015-2023 | La inversión pública se organiza mediante programas de investigación y misión |
| Familias de patentes | El mapeo OCDE-OEP identifica 31,700 familias de patentes cuánticas con primeros años de publicación entre 2005 y 2024; el patentamiento cuántico se multiplicó por siete entre 2005 y 2024 y creció alrededor de 20 por ciento CAGR desde 2014 | La invención se acelera pero está geográficamente concentrada |
| Publicaciones | La consulta "Quantum technology" de OpenAlex devuelve 15,279 trabajos, 2015-2025; los países principales son Estados Unidos, China, Alemania, Reino Unido y Francia | La capacidad científica de absorción está distribuida de manera desigual |
| Publicaciones PQC | La consulta PQC de OpenAlex muestra a Estados Unidos, India y China como afiliaciones líderes | La preparación PQC depende de capacidades criptográficas y de software, no solo de hardware físico |
| Preparación empresarial | La OCDE resume encuestas en las que la expectativa de disrupción es alta, pero la planeación, los presupuestos y la identificación de casos de uso son bajos | La conciencia no equivale a preparación |
| Estándares | NIST finalizó ML-KEM, ML-DSA y SLH-DSA en 2024 | La migración PQC ya es una agenda de implementación |

El patrón más fuerte no es el crecimiento simple. Es la formación desigual de capacidades. El financiamiento público aumenta, el patentamiento se acelera y las publicaciones se concentran en un grupo reducido de países. Al mismo tiempo, la preparación empresarial sigue siendo débil. En la evidencia de preparación resumida por la OCDE, 97 por ciento de ejecutivos del Reino Unido en una encuesta esperaba disrupción cuántica, pero solo alrededor de un tercio había iniciado planeación; 87 por ciento de encuestados del sector financiero veía la computación cuántica como oportunidad, mientras 73 por ciento carecía de un caso de uso con ventaja comercial y 87 por ciento no tenía presupuesto cuántico dedicado; evidencia de ISACA resumida por la OCDE encontró que solo 20 por ciento de los encuestados tenía planes formales de preparación cuántica pese a expectativas amplias de impacto [@oecd2026].

Esta es la brecha de adopción. Países y empresas están escuchando la narrativa cuántica, pero muchos no han construido los mecanismos requeridos para actuar sobre ella. La brecha no es un problema de relaciones públicas. Es un problema de capacidades.

![Brecha entre conciencia y preparación en la adopción de computación cuántica. La evidencia de encuestas resumida por la OCDE indica que una alta expectativa de impacto coexiste con niveles mucho menores de planeación, definición de casos de uso y formación de presupuestos dedicados.](figures/fig3_readiness_gap.png){width=95%}

## 5. Resultados: rutas de adopción por dominio tecnológico

### 5.1 Computación cuántica: alta opcionalidad, baja certeza de corto plazo

La computación cuántica tiene el mayor potencial estratégico de largo plazo y la mayor incertidumbre de adopción. Su fundamento teórico es sólido. Los algoritmos cuánticos pueden ofrecer aceleraciones asintóticas en clases específicas de problemas [@montanaro2016]. La simulación cuántica y la química son objetivos naturales porque las computadoras clásicas enfrentan dificultades con la estructura exponencial de muchos sistemas cuánticos [@georgescu2014; @cao2019; @bauer2020]. Los algoritmos variacionales híbridos ofrecen rutas experimentales de corto plazo [@peruzzo2014; @kandala2017; @cerezo2021; @bharti2022].

La restricción dura es que las aplicaciones valiosas requieren circuitos más profundos, menores tasas de error lógico y mejor verificación que las disponibles en los dispositivos actuales. La tolerancia a fallas sigue siendo el punto de transición entre dispositivos experimentales e infraestructura confiable. Los códigos de superficie son una ruta líder porque son compatibles con interacciones locales bidimensionales, pero imponen grandes sobrecostos [@fowler2012; @campbell2017]. Las estimaciones de recursos para máquinas criptográficamente relevantes siguen siendo altas, aun cuando mejores algoritmos reducen requerimientos [@gidney2021].

La implicación para adopción es que la computación cuántica funciona en el corto plazo como un dominio de aprendizaje, evaluación comparativa y valor de opción. Las acciones nacionales y empresariales más racionales no son el despliegue masivo, sino la experimentación dirigida, la formación de talento, la evaluación algorítmica, el acceso a plataformas QCaaS y la comparación cuidadosa con alternativas clásicas.

### 5.2 Sensórica cuántica: el dominio de valor público más inmediato

La sensórica cuántica es el dominio de aplicación de corto plazo más fuerte porque puede producir valor sin computadoras cuánticas universales tolerantes a fallas. Usa sistemas cuánticos como dispositivos de medición: relojes atómicos para tiempo, magnetómetros para campos magnéticos, gravímetros para mapeo del subsuelo, sensores inerciales para navegación y defectos cuánticos en diamante para sensórica magnética local [@degen2017; @barry2016]. La propuesta de valor no es "cómputo más rápido", sino mejor información sobre el mundo físico.

La distinción es importante para la política pública. Muchos países tienen problemas urgentes en agua, infraestructura, minería, salud, energía, navegación, monitoreo fronterizo, riesgo sísmico, vigilancia ambiental y control de calidad industrial. La sensórica cuántica puede vincularse a estas misiones antes de que la computación cuántica pueda vincularse a una transformación empresarial general. La barrera no es la incertidumbre teórica, sino el despliegue en campo: los instrumentos requieren robustez, calibración, costo-efectividad, interoperabilidad y relevancia operativa.

### 5.3 Comunicación cuántica: estratégica, especializada e intensiva en infraestructura

La comunicación cuántica tiene fuerte relevancia estratégica de largo plazo, especialmente para distribución de entrelazamiento, enlaces seguros, sensórica distribuida y redes cuánticas futuras [@kimble2008; @wehner2018]. QKD ya ha avanzado más allá de la demostración puramente de laboratorio, y la literatura de seguridad se ha vuelto sofisticada respecto a dispositivos realistas, canales laterales y protocolos independientes del dispositivo de medición [@pirandola2020; @xu2020].

La crítica es igualmente importante. QKD no elimina la necesidad de autenticación, seguridad de endpoints, ingeniería de redes, estándares de adquisición ni análisis costo-beneficio. Requiere infraestructura especializada y puede estar limitada por pérdida, distancia, supuestos de nodos confiables y aseguramiento de dispositivos. Los repetidores cuánticos son el análogo de red de la tolerancia a fallas: sin repetidores, memorias, intercambio de entrelazamiento e interfaces de baja pérdida confiables, las redes cuánticas de gran escala siguen restringidas.

En consecuencia, la comunicación cuántica se persigue mejor mediante testbeds dirigidos y enlaces de alto valor, no mediante afirmaciones amplias de que reemplazará la ciberseguridad existente. Su valor nacional reside en aprendizaje estratégico, experimentación telecom, nichos de alta seguridad y preparación para futuras redes cuánticas.

### 5.4 Criptografía post-cuántica: el primer mandato nacional de adopción

La PQC es el dominio de adopción más urgente porque aborda una transición real de seguridad que puede comenzar antes de que existan computadoras cuánticas criptográficamente relevantes. El algoritmo de Shor amenaza RSA, Diffie-Hellman y criptografía de curva elíptica una vez que existan máquinas tolerantes a fallas de gran escala. El riesgo relevante no es solo un ataque futuro; es la recolección actual de datos cifrados de larga vida [@mosca2018]. Los estándares de NIST de 2024 ofrecen a las organizaciones un objetivo concreto de migración, especialmente ML-KEM, ML-DSA y SLH-DSA [@nist2024].

La parte difícil no es elegir un algoritmo en aislamiento. La migración requiere inventarios criptográficos, cripto-agilidad, coordinación con proveedores, pruebas de protocolos, reemplazo de sistemas heredados, lenguaje de adquisición, gobernanza de cumplimiento y priorización por vida útil de los datos. La PQC es, por tanto, un programa de infraestructura digital. Tratarla como un parche estrecho de ciberseguridad subestima el trabajo institucional implicado.

## 6. Comparación de hardware y economía de qubits lógicos

Ninguna modalidad de hardware ha ganado. Cada plataforma expresa un compromiso de ingeniería distinto.

| Modalidad | Fortaleza | Cuello de botella | Interpretación estratégica |
| --- | --- | --- | --- |
| Qubits superconductores | Compuertas rápidas, ecosistema industrial fuerte, ruta de microfabricación, disponibilidad en nube | Cableado criogénico, pérdida dieléctrica, crosstalk, carga térmica, calibración | Plataforma fuerte de corto plazo, pero la escala depende de la economía de control y corrección de errores |
| Iones atrapados | Alta fidelidad, larga coherencia, uniformidad natural de qubits, conectividad flexible | Velocidad de compuertas, transporte, calentamiento, complejidad láser/control | Calidad excelente, pero la escala de ingeniería y el throughput siguen siendo preguntas centrales |
| Átomos neutros | Arreglos grandes, geometría reconfigurable, escalabilidad prometedora | Pérdida de átomos, leakage, fidelidad de compuertas, lectura, control óptico | Opción fuerte para simulación y escalamiento, con preguntas abiertas sobre arquitectura tolerante a fallas |
| Fotónica | Medio natural de comunicación, potencial a temperatura ambiente, compatibilidad con redes | Pérdida de fotones, compuertas deterministas, integración de fuentes y detectores | Estratégicamente importante para redes y algunas arquitecturas de cómputo |
| Recocido cuántico | Sistemas disponibles y experimentos de optimización | Universalidad limitada, ambigüedad de benchmarks, sobrecosto de mapeo | Útil para experimentación cuando se compara contra heurísticas clásicas |

Las plataformas superconductoras han avanzado rápidamente y son revisadas en detalle por @krantz2019 y @kjaergaard2020. Los sistemas de iones atrapados son revisados por @bruzewicz2019. Los sistemas de átomos neutros son revisados por @saffman2016 y @henriet2020. Los sistemas fotónicos son revisados por @slussarenko2019. La comparación muestra por qué el conteo de qubits es una métrica débil. Un dispositivo con más qubits físicos puede ser menos valioso que uno más pequeño con mejor fidelidad de compuertas, menor ruido correlacionado, mejor conectividad o una ruta más clara hacia la supresión de error lógico.

La métrica estratégica es la economía de qubits lógicos. Una computadora cuántica útil no se definirá por el número de qubits físicos que contenga. Se definirá por el costo, la confiabilidad y la velocidad de sus operaciones lógicas. Las métricas relevantes incluyen tasa de error lógico, distancia de código, tiempo de ciclo, latencia de decodificación, leakage, conectividad, estabilidad de calibración, profundidad de circuito con fidelidad útil, costo energético y recursos físicos por qubit lógico. @proctor2022 sostienen que la capacidad de una computadora cuántica se mide por los programas que un procesador puede ejecutar con éxito, no por un benchmark escalar único. Ese es el estándar requerido para política pública y adquisición.

## 7. Dominios de aplicación: promesa, evidencia y crítica

### 7.1 Química y materiales

La química y la ciencia de materiales siguen siendo el caso de aplicación más fuerte de largo plazo. Las computadoras cuánticas podrían eventualmente simular sistemas moleculares y de materiales de forma más natural que las máquinas clásicas [@georgescu2014; @cao2019; @bauer2020]. Las aplicaciones potenciales incluyen catalizadores, baterías, fármacos, superconductores de alta temperatura, corrosión, fertilizantes, polímeros, semiconductores y captura de carbono.

La crítica es que la relevancia científica no produce adopción industrial automáticamente. Un flujo de trabajo útil mejora una decisión en descubrimiento de fármacos, diseño de materiales o manufactura. Produce precisión relevante, se integra con experimentos de laboratorio y reduce tiempo o costo. La ruta de adopción es por tanto híbrida: algoritmos cuánticos, cómputo clásico de alto desempeño, modelos de IA, experimentos y expertos de dominio trabajando juntos.

### 7.2 Optimización

La optimización se cita con frecuencia como la oportunidad comercial más temprana, pero también es el área más fácil de exagerar. Logística, optimización de portafolios, calendarización, gestión de redes eléctricas y cadenas de suministro son valiosas, pero la optimización clásica es extraordinariamente fuerte. Programación entera mixta, programación por restricciones, heurísticas, algoritmos de aproximación, GPUs y solvers específicos de dominio ya funcionan bien. Una afirmación de optimización cuántica solo es creíble cuando supera el mejor baseline clásico en una instancia relevante a un costo relevante.

El rol más realista de corto plazo es exploratorio: recocido cuántico, flujos tipo QAOA y métodos inspirados en lo cuántico pueden ayudar a identificar clases de problemas y prácticas de software. No son reemplazos generales para la investigación de operaciones.

### 7.3 Finanzas

Las finanzas son atractivas porque pequeñas mejoras en riesgo, optimización, muestreo o precios pueden crear gran valor. @orus2019 y @egger2020 revisan aplicaciones potenciales, incluyendo optimización de portafolios, aceleración de Monte Carlo, análisis de riesgo, calificación crediticia y valuación de derivados. Las instituciones serias no preguntarán si la computación cuántica está de moda. Preguntarán si mejora calidad de modelo, velocidad, auditabilidad regulatoria y asignación de capital frente a métodos clásicos.

### 7.4 Aprendizaje automático e IA

El aprendizaje automático cuántico es intelectualmente rico, pero comercialmente inmaduro. @biamonte2017 identifican razones por las que los sistemas cuánticos podrían soportar modelos útiles de aprendizaje. @schuld2019 conectan mapas de características cuánticas con métodos kernel. @mcclean2018 muestran que el entrenamiento puede fallar por mesetas estériles. La recomendación de política es directa: QML pertenece al portafolio de investigación, no a afirmaciones exageradas de transformación empresarial. El valor de corto plazo puede venir más de la IA mejorando sistemas cuánticos -calibración, mitigación de errores, diseño de pulsos, descubrimiento de materiales y control- que de sistemas cuánticos mejorando la IA convencional.

### 7.5 Ciberseguridad

La ciberseguridad es la aplicación transversal más inmediata porque la migración PQC afecta casi todo sistema digital. El asunto central de política es el tiempo. Datos que requieren confidencialidad por 10, 20 o 30 años pueden ser vulnerables al descifrado cuántico futuro. Grandes organizaciones pueden requerir muchos años para inventariar y migrar activos criptográficos. Si la suma de vida útil del dato y tiempo de migración excede el tiempo hasta una computadora cuántica criptográficamente relevante, la acción ya llega tarde por definición [@mosca2018].

## 8. Cómputo de alto desempeño y computación cuántica

La ruta de adopción de la computación cuántica es inseparable del cómputo de alto desempeño. Es improbable que las computadoras cuánticas reemplacen a las supercomputadoras clásicas como máquinas de propósito general. La transición más plausible es un modelo de aceleradores en el cual las unidades de procesamiento cuántico se integran a entornos HPC heterogéneos junto con CPUs, GPUs, almacenamiento, gestores de flujos de trabajo, calendarizadores y pilas de software científico. En esta arquitectura, la computación cuántica se invoca solo para subrutinas donde una representación cuántica podría mejorar simulación, muestreo, optimización o tareas de álgebra lineal, mientras el HPC clásico realiza preparación de datos, orquestación, mitigación de errores, ciclos de optimización, verificación y post-procesamiento.

La investigación reciente en HPC-QC refleja esta transición. @cranganore2024 formalizan flujos de trabajo científicos híbridos cuántico-clásicos e identifican requisitos de gestión de flujos para mapear pipelines científicos clásicos hacia recursos híbridos. @beck2024 enmarcan la computación cuántica como acelerador computacional dentro de ecosistemas científicos HPC, enfatizando integración independiente del hardware, benchmarks, interfaces de usuario y gestión de workflows. @liu2024 desarrollan una perspectiva HPC centrada en lo cuántico para química cuántica, donde algoritmos cuánticos, emuladores cuánticos y recursos HPC clásicos apoyan conjuntamente la simulación química. Esta literatura desplaza la pregunta de "¿cuándo reemplazarán las computadoras cuánticas a las supercomputadoras?" hacia "¿qué componentes de un flujo científico pueden delegarse a una QPU bajo restricciones realistas de latencia, ruido, colas y verificación?"

La visión HPC modifica cuatro elementos de la estrategia cuántica. Primero, modifica la infraestructura. Un ecosistema útil de computación cuántica requiere no solo QPUs y cuentas en la nube, sino también calendarizadores, middleware, compiladores, software de mitigación de errores, protocolos de movimiento de datos, sistemas de procedencia, controles de reproducibilidad e interfaces con códigos científicos existentes. Segundo, modifica la evaluación comparativa. Una subrutina cuántica debe evaluarse dentro de un flujo completo, incluyendo costo de carga de datos, tiempo de optimización clásica, latencia de cola, sobrecosto de mitigación de errores y validación contra baselines HPC clásicos. Tercero, modifica la formación laboral. La adopción de computación cuántica requiere científicos computacionales e ingenieros HPC capaces de descomponer aplicaciones en componentes clásicos y cuánticos, no solo físicos que entienden qubits. Cuarto, modifica la adquisición nacional. Un país que invierte en computación cuántica sin capacidad de integración HPC corre el riesgo de comprar dispositivos aislados incapaces de sostener flujos científicos o industriales.

La complementariedad es especialmente importante para economías cuánticas emergentes y de ingreso medio. La propiedad doméstica de una computadora cuántica líder puede ser irrealista en el corto plazo, pero el acceso a centros HPC, clusters GPU, sistemas de workflow científico y QPUs en la nube puede construir capacidad de absorción significativa. El objetivo estratégico no es una transición binaria de HPC a computación cuántica. Es la construcción de un continuo HPC-QC en el que la supercomputación clásica permanece como sustrato operativo y la computación cuántica entra como acelerador especializado cuando la evidencia lo justifica.

## 9. Estrategia nacional comparada

Los modelos nacionales revelan teorías estratégicas distintas.

Estados Unidos combina coordinación federal, laboratorios nacionales, universidades, capital de riesgo, grandes plataformas en la nube e investigación vinculada a defensa. Su ventaja es la diversidad ecosistémica y la profundidad del capital privado. Su debilidad es la fragmentación y la traducción desigual entre agencias y sectores.

China ha enfatizado inversión dirigida por el Estado, infraestructura de comunicación segura y autosuficiencia tecnológica. Su ventaja es la coordinación y el foco estratégico. Su debilidad puede ser menor transparencia y riesgo de sobredimensionar infraestructura simbólica antes de que exista valor operativo claro.

Europa enfatiza coordinación transfronteriza, redes públicas de investigación, estándares y autonomía estratégica. Su ventaja es la coordinación institucional y la calidad de investigación. Su debilidad es la velocidad de comercialización y la fragmentación entre mercados nacionales.

Los países de ingreso medio e intensivos en manufactura enfrentan un problema distinto. No pueden simplemente copiar los programas más grandes. Su oportunidad estratégica es la construcción selectiva de capacidades: migración PQC, sensórica cuántica para misiones públicas, acceso a computación cuántica mediado por la nube, laboratorios de metrología, redes de fuerza laboral y participación en estándares. La meta correcta no es poseer de inmediato cada capa del stack. Es evitar convertirse solo en comprador de tecnologías cuánticas diseñadas, evaluadas y gobernadas en otra parte.

## 10. Hacia un modelo nacional de capacidades cuánticas

La evidencia apoya un modelo de capacidades con siete pilares.

| Pilar | Capacidad central | Pregunta institucional principal |
| --- | --- | --- |
| Frontera científica | Investigación en información cuántica, algoritmos, metrología, materiales, corrección de errores, fundamentos | ¿Puede el país participar en la producción de conocimiento de frontera? |
| Transición de seguridad | Migración PQC, cripto-agilidad, protección de datos de larga vida | ¿Pueden los sistemas críticos mantenerse seguros durante la transición cuántica? |
| Sensórica y metrología | Relojes atómicos, magnetometría, gravimetría, sensórica inercial, calibración | ¿Puede la medición cuántica resolver problemas nacionales en territorio, agua, salud, energía e infraestructura? |
| Acceso computacional HPC-QC | QCaaS, integración HPC, flujos híbridos, benchmarks, software cuántico | ¿Pueden las instituciones aprender sin encierro prematuro en hardware y preservando continuidad con infraestructura científica de cómputo? |
| Estándares y adquisición | Benchmarking, interoperabilidad, evaluación de proveedores, criterios anti-hype | ¿Pueden compradores públicos y privados distinguir desempeño de narrativa? |
| Fuerza laboral | Investigadores, ingenieros, técnicos, profesionales de ciberseguridad, responsables de compras | ¿Puede el ecosistema construir el eslabón intermedio entre doctorados en física y despliegue operativo? |
| Posición industrial | Componentes, sistemas de control, fotónica, criogenia, software, integración de sensores | ¿Dónde pueden entrar realistamente las empresas nacionales en la cadena de valor? |

El pilar de fuerza laboral merece énfasis. @kaur2022 muestran que las iniciativas globales de educación cuántica se expanden, pero el problema laboral no consiste solo en más doctorados. Las industrias cuánticas requieren técnicos e ingenieros capaces de alinear láseres, operar criostatos, construir sistemas de control RF, manejar vacío, escribir firmware, calibrar, diseñar interfaces de software, auditar criptografía y traducir problemas de dominio en flujos de trabajo verificables. Una nación que forma solo investigadores, pero no operadores, seguirá dependiendo de sistemas importados.

![Secuenciación de capacidades cuánticas nacionales. El mapa de calor puntúa la prioridad estratégica en tres fases de hoja de ruta y enfatiza que PQC, fuerza laboral, estándares, sensórica, QCaaS, comunicación e I+D de frontera maduran en horizontes de política distintos.](figures/fig4_capability_heatmap.png){width=95%}

## 11. Hoja de ruta estratégica, 2025-2035

### 11.1 Fase I: preparación y seguridad, 2025-2027

La primera fase no consiste en comprar una computadora cuántica nacional. Consiste en convertirse en un adoptante competente. Las acciones institucionales centrales incluyen una oficina de preparación cuántica, inventarios de activos criptográficos, prioridades de migración PQC para datos de larga vida, lenguaje de adquisición para sistemas cuánticamente seguros, estudios de factibilidad de sensórica cuántica, acceso QCaaS para universidades y agencias, entrenamiento en flujos HPC-QC y módulos de fuerza laboral para ingenieros, profesionales de ciberseguridad y tomadores de decisión del sector público.

Los productos medibles no son comunicados de prensa. Son inventarios, personal capacitado, pipelines de casos de uso, requisitos verificables, estándares de adquisición y competencia institucional básica.

### 11.2 Fase II: testbeds y pilotos de misión, 2027-2030

La segunda fase se centra en aprendizaje operativo. Los pilotos de sensórica cuántica pueden vincularse a agua, energía, salud, geodesia, infraestructura, minería y riesgo ambiental. La migración PQC pasa de planeación a implementación por etapas. Los testbeds de software cuántico evalúan algoritmos contra baselines clásicos. Los centros HPC prueban flujos híbridos cuántico-clásicos, incluyendo integración de calendarizadores, transición de simulador a hardware y procedencia de workflows. Instituciones de telecomunicaciones e investigación pueden probar QKD y componentes tempranos de red donde los enlaces de alto valor justifiquen el costo. Los laboratorios de estándares evalúan afirmaciones de proveedores.

El riesgo principal en esta fase es el *quantum washing*. Proveedores y agencias pueden etiquetar sistemas clásicos, inspirados en lo cuántico o inmaduros como avances estratégicos. La protección es disciplina de benchmarks: cada piloto requiere un baseline clásico, una métrica de desempeño, una métrica de costo, un método de verificación y una regla de decisión.

### 11.3 Fase III: escalamiento selectivo e integración de frontera, 2030-2035

La tercera fase escala solo aquello que ha demostrado valor. Los sistemas de sensórica que resuelvan problemas de misión pueden pasar a adquisición. La PQC puede convertirse en estándar en toda la infraestructura digital pública. La computación cuántica puede expandirse donde los workflows muestren ventaja creíble o donde el valor científico y de formación justifique continuar la experimentación. La investigación nacional profundiza en corrección de errores, qubits lógicos, repetidores cuánticos, seguridad independiente de dispositivos, metrología cuántica, materiales cuánticos y fundamentos.

![Hoja de ruta para la formación de capacidades cuánticas nacionales, 2025-2035. La secuencia se organiza alrededor de preparación institucional, aprendizaje operativo y escalamiento selectivo, no de la predicción de un solo avance de hardware.](figures/fig5_roadmap_timeline.png){width=95%}

El objetivo estratégico es la opcionalidad. Para 2035, la nación exitosa no es necesariamente la que anuncia la computadora cuántica más grande. Es la que cuenta con personas formadas, criptografía segura, testbeds funcionales, capacidad de estándares, capacidad metrológica, pilotos de dominio, alianzas internacionales y una base de investigación conectada con la frontera.

## 12. Agenda de investigación de frontera

La estrategia nacional cuántica incluye temas de frontera que no son inmediatamente comerciales. Estas áreas generan instrumentos, expertise y autonomía de largo plazo.

**Economía de qubits lógicos.** La investigación se desplaza de conteos de qubits físicos al costo de operaciones lógicas. Esto incluye corrección de errores, decodificadores, gestión de leakage, sobrecosto de estados mágicos, códigos qLDPC y estimaciones de recursos específicas por arquitectura.

**Punto de equilibrio de redes cuánticas.** Repetidores, memorias, transductores e intercambio de entrelazamiento son el equivalente de red de la tolerancia a fallas. El hito no es solo un enlace de laboratorio; es desempeño superior a la transmisión directa bajo condiciones realistas de costo y confiabilidad.

**Sensórica cuántica para misiones nacionales.** La investigación conecta gravimetría, magnetometría, temporización y sensórica inercial con problemas públicos reales. La pregunta central no es la sensibilidad máxima en aislamiento, sino el valor operativo bajo condiciones de campo.

**Ciencia de benchmarks.** Las naciones necesitan capacidad independiente para probar afirmaciones cuánticas. Esto incluye benchmarking aleatorizado, benchmarks a nivel de aplicación, caracterización de errores, reproducibilidad y métricas de desempeño basadas en costo [@proctor2022; @alexeev2021].

**Fundamentos cuánticos como estrategia de instrumentación.** El trabajo fundamental en contextualidad, medición, superposición macroscópica, decoherencia y ruido no markoviano no es meramente filosófico. Impulsa instrumentación en interferometría, aislamiento, óptica, criogenia, detectores y control.

**IA para sistemas cuánticos.** La IA puede ser más valiosa como herramienta de ingeniería cuántica: calibración, control, mitigación de errores, descubrimiento de materiales, calendarización, optimización de pulsos e interpretación de datos de sensores.

## 13. Discusión: qué debe evitar una estrategia cuántica seria

El primer error es esperar. Esperar máquinas tolerantes a fallas antes de preparar PQC, fuerza laboral, estándares y sensórica dejaría a las instituciones sin preparación cuando aumente la presión de adopción. La preparación toma años.

El segundo error es nacionalismo de hardware sin capacidad. Comprar o anunciar una computadora cuántica doméstica no crea un ecosistema cuántico si no hay operadores entrenados, laboratorio de benchmarking, pipeline de software, disciplina de adquisición ni demanda de misión.

El tercer error es confundir QKD con PQC. QKD puede ser valiosa para enlaces especializados y redes de investigación, pero PQC es la ruta amplia de migración para sistemas digitales existentes. Tratar QKD como sustituto general de PQC malinterpreta tanto la tecnología como el problema de infraestructura.

El cuarto error es tratar QCaaS como acceso neutral. El acceso en la nube democratiza la experimentación, pero también puede concentrar poder de plataforma. El proveedor de nube puede controlar herramientas de desarrollo, acceso a backends, precios, políticas de datos y relaciones empresariales. Las naciones necesitan acceso QCaaS, pero también soberanía sobre conocimiento, benchmarks, gobernanza de datos críticos y capacidad de conectar experimentos cuánticos con infraestructura HPC doméstica.

El quinto error es aceptar afirmaciones de ventaja cuántica sin baselines. Una afirmación creíble especifica clase de problema, baseline clásico, supuestos de hardware, modelo de error, método de verificación, tiempo de solución, costo energético y relevancia económica. Sin estos elementos, la afirmación no constituye base para adquisición.

El sexto error es subfinanciar el eslabón intermedio. La estrategia cuántica suele financiar investigación de élite y promoción de startups mientras ignora técnicos, ingenieros, expertos en estándares, auditores de ciberseguridad y profesionales de compras. Estos roles determinan si la ciencia se convierte en infraestructura.

## 14. Recomendaciones de política pública y empresa

Para los gobiernos nacionales, la primera recomendación es crear una función de preparación cuántica con autoridad transversal en ciencia, economía, ciberseguridad, defensa, educación, estándares y adquisición pública. Los comités fragmentados son insuficientes si no pueden fijar prioridades ni coordinar presupuestos.

Segundo, la migración PQC es infraestructura digital crítica. La unidad correcta de trabajo no es solo la selección de algoritmos. Es inventario de activos, clasificación por vida útil de datos, cripto-agilidad, gestión de proveedores, pruebas, migración por etapas y cumplimiento.

Tercero, la sensórica cuántica debe financiarse mediante pilotos de misión. Agua, energía, salud, territorio, infraestructura, minería, navegación y monitoreo ambiental ofrecen casos de uso de valor público donde una mejor medición puede cambiar decisiones.

Cuarto, la política de computación cuántica debe enfatizar integración HPC, acceso, benchmarks y talento antes de encierro en hardware doméstico. QCaaS, testbeds compartidos, software abierto y gestores de workflows híbridos pueden construir competencia mientras las trayectorias de hardware siguen inciertas.

Quinto, la adquisición pública requiere evidencia anti-hype. Todo piloto cuántico incluye baseline clásico, métrica de desempeño, métrica de costo, requisito de interoperabilidad, evaluación de seguridad y criterio de salida.

Sexto, el sistema de investigación financia conjuntamente ciencia de frontera e industrialización. Corrección de errores, repetidores, metrología, fundamentos, materiales y sistemas de control no están separados de la comercialización; son la base de la cual emergerá la comercialización.

Para las empresas, el primer paso no es un gran programa de transformación cuántica. Es un portafolio pequeño de preparación: identificar problemas de alto valor, mapear riesgo criptográfico, formar personal técnico, probar flujos QCaaS, monitorear estándares y participar en consorcios. La inversión se justifica cuando un método cuántico mejora una decisión, no cuando mejora una narrativa.

## 15. Conclusión

Las tecnologías cuánticas moldearán la próxima década menos por una disrupción universal repentina que por una formación desigual de capacidades. La PQC ya es un problema de migración de ciberseguridad. La sensórica cuántica puede producir valor público e industrial antes de la computación tolerante a fallas. La comunicación cuántica es estratégicamente importante pero intensiva en infraestructura. La computación cuántica sigue siendo la mayor oportunidad de largo plazo, pero su valor depende de la economía de qubits lógicos, ventaja verificada e integración con flujos clásicos.

La conclusión más importante es que la preparación cuántica es una capacidad nacional, no una compra de hardware. Los países que construyan capacidad de migración criptográfica, pilotos de sensórica, laboratorios de estándares, trayectorias de fuerza laboral, competencia QCaaS y redes de investigación de frontera estarán posicionados para adoptar las modalidades de hardware que maduren. Los países que esperen a que el mercado entregue productos cuánticos terminados se convertirán en compradores dependientes.

El futuro de las tecnologías cuánticas requiere ambición disciplinada. La ambición es construir soberanía científica y tecnológica en un campo que afectará seguridad, medición, computación y descubrimiento industrial. La disciplina es evidencial: ciencia rigurosa, benchmarks reproducibles, baselines clásicos, pilotos operativos y compras transparentes. La estrategia cuántica tiene éxito cuando convierte efectos cuánticos frágiles en capacidad pública confiable.

## Agradecimientos

Este manuscrito fue preparado para el track de Tecnologías Cuánticas de la vigésima tercera edición de la Conferencia Anual de la Global Information Technology Management Association, Monterrey, México, 6-8 de mayo de 2026. El autor reconoce su papel como Track Chair de Tecnologías Cuánticas y agradece a Rogelio Marín y al Centro de Investigación en Matemáticas, A.C. por el apoyo intelectual y el contexto institucional. Todas las interpretaciones y errores remanentes son responsabilidad del autor.

## Disponibilidad de datos

Las tablas cuantitativas generadas para este manuscrito están depositadas en el repositorio de investigación complementario. Incluyen conteos por país y año de OpenAlex para los conceptos "Quantum technology" y "Post-quantum cryptography" durante 2015-2025. Los datos de OCDE, NIST, NSA, CISA, OCDE-OEP y preparación de mercado se citan a fuentes públicas en la lista de referencias. Las consultas de OpenAlex usaron los identificadores de concepto `C190463098` y `C108277079`, agrupados por año de publicación y país institucional.

## Disponibilidad de código

El repositorio de investigación complementario está disponible en https://github.com/ekaropolus/quantum-technologies-national-strategy. Contiene los manuscritos fuente, datos procesados, bibliografía BibTeX, código de generación de figuras y script reproducible de construcción usados para generar los resultados del manuscrito. El repositorio permite inspeccionar los extractos de OpenAlex, regenerar figuras y reconstruir las versiones PDF, TeX y DOCX a partir de las fuentes del manuscrito.

## Contribuciones del autor

Edgar Valdés conceptualizó el manuscrito, dirigió la síntesis de investigación, interpretó la evidencia y preparó el manuscrito.

## Financiamiento

No se declaró financiamiento externo para este manuscrito.

## Conflictos de interés

El autor declara no tener conflictos de interés.

## Limitaciones

El análisis se basa en proxies de adopción, no en datos directos de despliegue global. Financiamiento, patentes, publicaciones, estándares y encuestas de preparación miden dimensiones distintas de capacidad cuántica y no son intercambiables. Los conteos de OpenAlex dependen de la asignación de conceptos, metadatos institucionales y prácticas de indexación. Los pronósticos de mercado se tratan solo como evidencia direccional. Una extensión empírica futura requeriría entrevistas con agencias gubernamentales, operadores de infraestructura, proveedores cuánticos, equipos de ciberseguridad y adoptantes empresariales, además de una encuesta estructurada de preparación cuántica por sectores.

## Referencias

::: {#refs}
:::
