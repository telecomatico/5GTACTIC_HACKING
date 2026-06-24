# Bases de WireGuard

## Propósito del documento

Este documento introduce las bases de WireGuard para que el alumnado comprenda qué problema resuelve, cómo funciona a alto nivel y por qué se ha convertido en una opción muy atractiva en laboratorios, redes privadas y algunos escenarios modernos de 5G y Open RAN. Estudios recientes lo evalúan como una solución ligera para proteger tráfico en redes 5G privadas y comparan su uso con alternativas tradicionales como IPsec. 

El objetivo es ofrecer una base conceptual suficiente para que, en una práctica posterior, el alumnado pueda configurar túneles, intercambiar claves, verificar conectividad y entender qué tráfico está siendo protegido. La idea más importante es que WireGuard protege tráfico IP en capa 3, con un diseño más simple y ligero que IPsec. 

## Qué es WireGuard

WireGuard es una tecnología de túneles VPN moderna diseñada para proteger comunicaciones IP de forma sencilla y eficiente. En la literatura reciente sobre redes privadas y Open RAN se presenta como una alternativa ligera para asegurar transporte IP con menor complejidad operativa que IPsec. 

Desde un punto de vista práctico, WireGuard crea un túnel seguro entre pares definidos mediante claves públicas y privadas. Ese túnel puede transportar tráfico IP de manera cifrada y autenticada entre los extremos configurados. 

## Qué servicios de seguridad ofrece

WireGuard ofrece, a nivel funcional, los servicios de seguridad que se esperan de una VPN moderna de capa 3:

- Confidencialidad del tráfico IP mediante cifrado. 
- Integridad de los paquetes para detectar modificaciones no autorizadas. 
- Autenticación entre pares basada en claves criptográficas. 
- Simplicidad de configuración al utilizar un conjunto criptográfico fijo y una lógica de operación más reducida que otras alternativas. 

Esa combinación hace que WireGuard resulte especialmente atractivo para entornos donde la facilidad de despliegue, la ligereza y la claridad operativa son prioritarias. 

## Qué problema resuelve

Cuando dos sistemas intercambian tráfico IP a través de una red que no se considera completamente confiable, existe riesgo de intercepción, modificación o suplantación. WireGuard se utiliza para crear un canal cifrado entre esos dos extremos y así proteger el tráfico durante el trayecto. 

Eso lo hace útil en redes privadas, laboratorios, infraestructuras virtualizadas, entornos Linux y algunos casos de 5G no públicos o de Open RAN. Un trabajo reciente sobre una red industrial 5G real evalúa precisamente WireGuard como solución ligera para proteger comunicaciones relevantes en ese contexto. 

## Dónde se sitúa en el modelo por capas

Una comparación por capas ayuda mucho a aclarar su posición:

| Tecnología | Capa principal | Qué protege |
|---|---|---|
| MACsec | Capa 2 Ethernet  | El enlace o segmento Ethernet  |
| IPsec | Capa 3 IP  | El tráfico IP entre extremos o túneles  |
| WireGuard | Capa 3 IP  | El tráfico IP entre pares definidos  |

La idea esencial es que WireGuard no protege directamente el enlace Ethernet, sino el tráfico IP que circula entre dos extremos configurados. Por eso se compara más naturalmente con IPsec que con MACsec. 

## Cómo funciona a alto nivel

WireGuard puede explicarse de forma muy sencilla si se parte de cuatro ideas:

1. Cada extremo tiene una clave privada y una clave pública. 
2. Cada par conoce la clave pública del otro extremo. 
3. Se definen direcciones IP del túnel y qué prefijos o redes deben enviarse por ese túnel. 
4. El tráfico permitido circula cifrado y autenticado entre ambos extremos. 

Este modelo resulta muy didáctico porque evita mucha complejidad habitual de otras VPN. Para una primera explicación basta con que el alumnado entienda que WireGuard funciona como una interfaz de red virtual segura entre pares que se conocen criptográficamente. 

## Conceptos básicos que debe entender el alumnado

En una primera aproximación, los conceptos más importantes son estos:

- **Par o peer**: cada uno de los extremos que participa en el túnel. 
- **Clave pública y privada**: material criptográfico que identifica y autentica a cada extremo. 
- **Interfaz WireGuard**: interfaz virtual por la que circula el tráfico protegido. 
- **Allowed IPs**: redes o direcciones que se enviarán al peer correspondiente por el túnel. 
- **Endpoint**: dirección IP y puerto del extremo remoto. 

Para el laboratorio, el concepto de **Allowed IPs** suele ser especialmente importante, porque determina qué tráfico entra realmente en el túnel y hacia qué peer se encamina. 

## Ventajas de WireGuard

Las ventajas que más valoran los técnicos y administradores suelen ser las siguientes:

- Configuración más simple que IPsec en muchos escenarios. 
- Menor complejidad operativa, al reducir el número de decisiones criptográficas y de señalización que debe tomar el administrador. 
- Buena adecuación a entornos Linux, virtualización, contenedores y laboratorios. 
- Interés creciente en redes privadas y Open RAN como alternativa ligera para proteger transporte IP. 

En un caso real de red industrial 5G, WireGuard se utilizó para cifrar tráfico relacionado con N3 y para autenticar comunicaciones asociadas a N2 entre gNB y AMF, mostrando resultados de rendimiento comparables a IPsec y una configuración más sencilla. 

## Limitaciones de WireGuard

Conviene también presentar sus limitaciones con claridad:

- No es el mecanismo clásico de referencia dentro del marco tradicional NDS/IP de 3GPP, donde IPsec tiene más tradición normativa. 
- Puede encontrar más barreras organizativas en grandes operadores si existen procesos, herramientas y políticas ya centrados en IPsec. 
- Su simplicidad no elimina la necesidad de diseñar bien direcciones, rutas, segmentación y control de acceso. 
- No sustituye por sí solo a otras medidas de seguridad de la red. 

## Relación con 5G, N2 y N3

WireGuard no forma parte de la familia clásica de mecanismos 3GPP usados históricamente para protección de redes IP, pero su ligereza ha despertado interés en escenarios de 5G privado y Open RAN. La investigación reciente lo evalúa explícitamente como alternativa para proteger N3 y parte de las comunicaciones internas del 5G Core o del acceso radio. 

En 5G, N2 conecta el gNB con el AMF para señalización de control, mientras N3 conecta el gNB con el UPF para tráfico de usuario. Al tratarse de trayectos sobre IP, WireGuard puede utilizarse como túnel ligero para proteger esos flujos cuando el entorno operativo lo permite. 

Una forma sencilla de explicarlo en clase es esta:

- En **N2**, WireGuard puede ayudar a asegurar señalización entre gNB y AMF en redes privadas o entornos de prueba. 
- En **N3**, WireGuard puede cifrar tráfico de usuario entre gNB y UPF. 
- Su principal atractivo en estos casos es la simplicidad de despliegue frente a IPsec. 

## Comparación sencilla con MACsec e IPsec

| Tecnología | Idea simple | Punto fuerte principal | Límite principal |
|---|---|---|---|
| MACsec | “Protege el enlace Ethernet”  | Buen rendimiento en capa 2  | No protege por sí mismo un trayecto IP amplio  |
| IPsec | “Protege el trayecto IP con una solución madura”  | Muy alineado con marcos de operador y 3GPP  | Mayor complejidad operativa  |
| WireGuard | “Protege el trayecto IP con una VPN ligera”  | Simplicidad y despliegue ágil  | Menor tradición normativa en 3GPP clásico  |

Esta comparación ayuda a que el alumnado entienda que WireGuard no debe presentarse como sustituto universal de todo, sino como una opción especialmente útil cuando se priorizan sencillez, rapidez de despliegue y operación clara. 

## Ejemplos de uso

Algunos escenarios donde WireGuard tiene especial interés son:

- Laboratorios docentes y de investigación sobre redes IP seguras. 
- Redes privadas 5G o entornos de campus. 
- Infraestructuras Linux y sistemas virtualizados. 
- Protección ligera de interconexiones entre funciones de red o entre nodos distribuidos. 

Un ejemplo intuitivo para el alumnado es imaginar un gNB software y un 5G Core desplegados en dos servidores Linux conectados a través de una red IP intermedia. Si se desea cifrar el tráfico entre ambos de forma sencilla y rápida para una prueba o práctica, WireGuard puede ser una solución muy adecuada. 

## Conceptos mínimos que debe recordar el alumnado

Al terminar la lectura, el alumnado debería recordar estas ideas:

- WireGuard protege tráfico IP en capa 3. 
- Usa una lógica de pares con claves públicas y privadas. 
- Define qué tráfico entra en el túnel mediante rutas o *Allowed IPs*. 
- Suele ser más simple de desplegar que IPsec en muchos escenarios. 
- En 5G, resulta especialmente atractivo en laboratorios, redes privadas y algunos contextos Open RAN. 

## Preparación para una práctica posterior

Antes de una práctica sobre WireGuard, conviene que el alumnado tenga claras estas preguntas:

1. ¿Qué dos extremos actuarán como peers? 
2. ¿Qué claves públicas y privadas tendrá cada extremo? 
3. ¿Qué direcciones IP se asignarán al túnel? 
4. ¿Qué redes o prefijos se incluirán en *Allowed IPs*? 
5. ¿Cómo se comprobará que el tráfico realmente circula por el túnel y no por la ruta ordinaria? 

En una práctica real, lo habitual será generar claves, crear la interfaz WireGuard, definir el peer remoto, asignar direcciones del túnel y validar conectividad, rutas y capturas. Esa práctica se entiende mucho mejor cuando primero se ha interiorizado que WireGuard crea una interfaz virtual segura de capa 3 entre extremos autenticados por claves. 

## Preguntas de autoevaluación

1. ¿En qué capa opera WireGuard? 
2. ¿Qué diferencia principal existe entre WireGuard y MACsec? 
3. ¿Por qué WireGuard suele percibirse como más simple que IPsec? 
4. ¿Qué función cumplen las *Allowed IPs*? 
5. ¿En qué tipo de despliegues 5G resulta especialmente atractivo? 
