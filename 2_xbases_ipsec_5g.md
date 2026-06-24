# Bases de IPsec

## Propósito del documento

Este documento presenta las bases de IPsec de forma clara y progresiva para que el alumnado entienda qué problema resuelve, cómo funciona a nivel general y por qué es una tecnología especialmente importante en redes IP modernas y en el transporte de interfaces 5G. En el ecosistema 3GPP, el marco NDS/IP toma IPsec como base para proteger redes basadas en IP, y por eso IPsec aparece con frecuencia cuando se habla de seguridad en interfaces como N2 y N3. 

El objetivo no es profundizar en todos los detalles criptográficos o de señalización, sino ofrecer una base conceptual suficiente para abordar después una práctica de laboratorio. La idea principal que debe quedar clara es que IPsec protege tráfico IP en capa 3, a diferencia de MACsec, que protege enlaces Ethernet en capa 2. 

## Qué es IPsec

IPsec, abreviatura de *Internet Protocol Security*, es un conjunto de mecanismos de seguridad para proteger comunicaciones IP. Su diseño permite aportar confidencialidad, integridad, autenticación y protección frente a ciertas formas de repetición de paquetes en redes IP. 

A diferencia de soluciones ligadas a una aplicación concreta, IPsec opera en la capa de red. Eso le permite proteger tráfico IP de forma relativamente transparente para las aplicaciones y para muchos protocolos superiores. 

## Qué servicios de seguridad ofrece

IPsec proporciona varios servicios fundamentales:

- Confidencialidad, mediante cifrado del tráfico IP. 
- Integridad, para detectar modificaciones de los paquetes durante el transporte. 
- Autenticación del origen, para asegurar que el tráfico procede de la entidad esperada. 
- Protección frente a ataques de repetición, mediante mecanismos de control de secuencia. 

En redes de operador y en infraestructuras críticas, esta combinación hace que IPsec sea una opción muy consolidada cuando el objetivo es proteger caminos IP entre equipos o funciones de red. 

## Qué problema resuelve

En una red IP sin protección, un atacante con visibilidad sobre el trayecto puede observar, modificar o intentar inyectar paquetes. IPsec se diseñó precisamente para reducir esos riesgos cuando el tráfico circula por redes que no pueden considerarse plenamente confiables. 

Por esa razón, IPsec resulta adecuado en enlaces entre sedes, en redes de operadores, en interconexión entre funciones virtualizadas y en múltiples escenarios de seguridad de transporte para 4G y 5G. En documentos relacionados con 5G y Open RAN se presenta de forma recurrente como una solución de referencia para proteger tramos IP de señalización y de usuario. 

## Dónde se sitúa en el modelo por capas

Una forma útil de explicar IPsec es compararlo con otras tecnologías de protección:

| Tecnología | Capa principal | Qué protege |
|---|---|---|
| MACsec | Capa 2 Ethernet  | El enlace o segmento Ethernet  |
| IPsec | Capa 3 IP  | El tráfico IP entre extremos o túneles  |
| WireGuard | Capa 3 IP  | El tráfico IP entre pares definidos  |

La implicación práctica es que IPsec encaja mejor que MACsec cuando el problema de seguridad está en el **trayecto IP** entre dos funciones o dos dominios de red, y no solamente en un enlace Ethernet concreto. 

## Componentes básicos de IPsec

Para una introducción de nivel base, basta con presentar tres ideas:

- **ESP** (*Encapsulating Security Payload*), que en redes NDS/IP se utiliza como protocolo de seguridad principal para proteger tráfico IP. 
- **Asociaciones de seguridad** o *Security Associations* (SA), que definen parámetros y claves para proteger el tráfico en una dirección concreta. 
- **Gestión de claves y negociación**, normalmente asociada a IKE en despliegues reales, aunque en una primera aproximación basta con saber que IPsec necesita un mecanismo para acordar parámetros criptográficos de forma segura. 

Un punto importante para el alumnado es que una asociación de seguridad suele ser unidireccional. Eso implica que, en una comunicación bidireccional, normalmente se necesitan asociaciones distintas para cada sentido del tráfico. 

## Cómo funciona a alto nivel

El comportamiento de IPsec puede explicarse de forma simple en cuatro pasos:

1. Dos extremos IP deciden proteger sus comunicaciones. 
2. Negocian o establecen asociaciones de seguridad y claves. 
3. El emisor cifra y/o autentica los paquetes según la política configurada. 
4. El receptor verifica integridad, autenticidad y, si corresponde, descifra el contenido. 

Desde el punto de vista docente, no hace falta entrar al detalle de todos los campos del encabezado o de cada intercambio IKE en una primera sesión. Es más útil que el alumnado entienda la idea de “túnel seguro IP entre dos extremos”. 

## Modos de uso: transporte y túnel

IPsec puede emplearse en distintos modos, pero para una base introductoria conviene distinguir sobre todo el **modo túnel**. En este modo, un paquete IP original queda encapsulado dentro de otro flujo IP protegido, lo que resulta muy útil para redes entre sedes, dominios de operador o interconexión entre funciones. 

En la práctica docente, el modo túnel suele ser el más intuitivo porque permite visualizar a IPsec como una “tubería segura” entre dos extremos. Ese modelo mental ayuda mucho para comprender su aplicación en transporte de señalización y tráfico de usuario en redes móviles. 

## Ventajas de IPsec

Las ventajas más importantes son estas:

- Protege tráfico IP sin depender de una única aplicación concreta. 
- Está ampliamente alineado con marcos de seguridad de operador y con NDS/IP en 3GPP. 
- Resulta adecuado para proteger tanto señalización como tráfico de usuario sobre redes IP. 
- Es una tecnología madura, conocida y ampliamente soportada en equipos de red y sistemas operativos. 

## Limitaciones de IPsec

También es importante explicar sus límites y costes operativos:

- Suele ser más complejo de configurar y mantener que alternativas ligeras como WireGuard. 
- Puede requerir una gestión más elaborada de políticas, claves, certificados y asociaciones de seguridad. 
- Su operación puede complicarse en escenarios con NAT, múltiples dominios administrativos o grandes despliegues heterogéneos. 
- No sustituye a otras medidas de seguridad como segmentación, endurecimiento de sistemas, control de acceso y monitorización. 

## Relación con 5G y con N2/N3

La relación entre IPsec y 5G es especialmente relevante porque N2 y N3 son interfaces que, en términos prácticos, se apoyan sobre transporte IP entre funciones de red. N2 conecta el gNB con el AMF para señalización de control, mientras que N3 conecta el gNB con el UPF para tráfico de usuario. [cite:20]

Como IPsec protege tráfico IP, su uso encaja de forma muy natural cuando se quiere asegurar esos trayectos entre RAN y Core, especialmente si la red de transporte no se considera totalmente confiable. Documentos relacionados con 3GPP NDS/IP y con despliegues 5G/Open RAN lo sitúan como una opción estándar o de referencia para este fin. 

En términos docentes, puede resumirse así:

- En **N2**, IPsec ayuda a proteger señalización crítica entre gNB y AMF. 
- En **N3**, IPsec ayuda a proteger tráfico de usuario entre gNB y UPF. 
- En ambos casos, su lógica de uso está más asociada al trayecto IP que al enlace Ethernet físico subyacente. 

## Comparación sencilla con MACsec y WireGuard

| Tecnología | Idea simple | Punto fuerte principal | Límite principal |
|---|---|---|---|
| MACsec | “Protege el enlace Ethernet”  | Buen rendimiento en capa 2  | No es protección IP extremo a extremo  |
| IPsec | “Protege el trayecto IP”  | Muy alineado con marcos de operador y 3GPP  | Mayor complejidad operativa  |
| WireGuard | “VPN IP ligera entre pares”  | Simplicidad de despliegue  | Menor tradición como mecanismo clásico 3GPP  |

Esta comparación ayuda a evitar un error habitual: pensar que todas estas tecnologías compiten exactamente por el mismo espacio. En realidad, muchas veces se complementan, porque protegen capas y dominios distintos. 

## Ejemplos de uso

Algunos escenarios típicos en los que IPsec tiene mucho sentido son:

- Conexión segura entre sedes de una organización sobre una red IP no confiable. 
- Protección del transporte entre funciones de red virtualizadas o distribuidas. 
- Seguridad de interfaces de señalización y usuario en despliegues 5G. 
- Interconexión entre dominios administrativos donde se necesita confidencialidad e integridad del tráfico IP. 

Un ejemplo muy útil para estudiantes es imaginar dos nodos 5G ubicados en centros distintos y unidos por una red IP del operador. Si se quiere asegurar que ni la señalización ni el tráfico de usuario puedan ser leídos o alterados durante el tránsito, IPsec resulta una solución natural. 

## Conceptos mínimos que debe recordar el alumnado

Al finalizar la lectura, el alumnado debería poder retener estas ideas:

- IPsec protege tráfico IP en capa 3. 
- Proporciona confidencialidad, integridad, autenticación y protección frente a repetición. 
- Utiliza asociaciones de seguridad y mecanismos de gestión de claves. 
- Encaja especialmente bien cuando lo que se quiere proteger es un trayecto IP entre extremos. 
- En 5G, su aplicación a N2 y N3 es muy natural por tratarse de transporte entre funciones de red sobre IP. [cite:20]

## Preparación para una práctica posterior

Antes de una práctica de laboratorio sobre IPsec, conviene que el alumnado tenga presentes estas preguntas:

1. ¿Qué extremos IP se van a proteger? 
2. ¿Qué tráfico debe entrar dentro del túnel y qué tráfico debe quedar fuera? 
3. ¿Qué mecanismo de autenticación y gestión de claves se usará? 
4. ¿Cómo se verificará que el tráfico realmente va cifrado y autenticado? 

En una práctica real, lo habitual será definir políticas, crear túneles o asociaciones, activar parámetros criptográficos y validar conectividad, contadores y capturas. Esa parte operativa se entiende mucho mejor cuando primero se comprende que IPsec está pensado para crear un canal seguro de capa 3 entre extremos de red. 

## Preguntas de autoevaluación

1. ¿En qué capa opera IPsec y qué implica eso? 
2. ¿Qué diferencia principal existe entre MACsec e IPsec? 
3. ¿Por qué IPsec resulta adecuado para proteger N2 y N3 en 5G? [cite:20]
4. ¿Qué papel juegan las asociaciones de seguridad en IPsec? 
5. ¿Qué ventaja aporta IPsec frente a limitarse a proteger solo el enlace Ethernet? 
