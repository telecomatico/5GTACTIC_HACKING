# Bases de MACsec

## Propósito del documento

Este documento introduce las bases de MACsec de forma gradual para que el alumnado comprenda qué problema resuelve, cómo funciona a alto nivel y en qué escenarios resulta útil dentro de redes Ethernet modernas y entornos de transporte 5G. MACsec está definido por el estándar IEEE 802.1AE y proporciona confidencialidad, integridad y autenticidad de origen para tráfico sobre Ethernet. 

El objetivo no es sustituir una práctica de laboratorio, sino ofrecer el marco conceptual mínimo para que después resulte más fácil configurar, verificar y analizar una implantación real. En particular, conviene entender desde el principio que MACsec protege el enlace Ethernet en capa 2, mientras que otras soluciones como IPsec o WireGuard protegen tráfico IP en capa 3. 

## Qué es MACsec

MACsec, abreviatura de *Media Access Control Security*, es una tecnología de seguridad para redes Ethernet definida por IEEE 802.1AE. Su función es proteger tramas Ethernet frente a escucha, modificación e inserción no autorizada en el tramo protegido. 

De forma resumida, MACsec añade seguridad directamente en el nivel de enlace de datos. Eso significa que la protección se aplica al tráfico Ethernet entre equipos conectados mediante un enlace o un dominio Ethernet concreto, sin depender de las aplicaciones superiores. 

## Qué servicios de seguridad ofrece

MACsec ofrece tres capacidades principales:

- Confidencialidad, mediante cifrado del contenido de la trama Ethernet. 
- Integridad, para detectar modificaciones no autorizadas durante el transporte. 
- Autenticidad de origen, para asegurar que la trama procede de una entidad autorizada dentro del enlace protegido. 

Además, MACsec está pensado para operar con baja sobrecarga y con soporte frecuente en hardware de red, lo que lo hace atractivo en enlaces de alto rendimiento. Esta característica es especialmente interesante en transporte Ethernet asociado a redes móviles y entornos de backhaul o fronthaul. 

## Qué problema resuelve

En una red Ethernet sin protección, un atacante con acceso al medio o a un equipo intermedio puede observar tráfico, intentar modificarlo o inyectar tramas. MACsec reduce esos riesgos cuando el objetivo es proteger el enlace Ethernet entre dos nodos o a través de un dominio controlado. 

Por eso MACsec encaja muy bien cuando la preocupación principal no está en la aplicación, sino en el transporte. Por ejemplo, puede utilizarse para proteger enlaces entre switches, routers, servidores, funciones virtualizadas o nodos de acceso radio conectados por Ethernet. 

## Dónde se sitúa en el modelo por capas

Una idea que ayuda mucho al alumnado es ubicar cada tecnología por capas:

| Tecnología | Capa principal | Qué protege |
|---|---|---|
| MACsec | Capa 2 Ethernet  | El enlace o segmento Ethernet  |
| IPsec | Capa 3 IP  | El tráfico IP entre extremos o túneles  |
| WireGuard | Capa 3 IP  | El tráfico IP entre pares definidos  |

La consecuencia práctica es importante: MACsec no sustituye automáticamente a IPsec. En muchos diseños, MACsec protege el enlace físico o conmutado, mientras IPsec protege un trayecto IP más amplio entre funciones de red. 

## Cómo funciona a alto nivel

MACsec protege tramas Ethernet mediante asociaciones de seguridad y claves que permiten cifrar y autenticar el tráfico. Para el alumnado basta con retener la idea de que hay un proceso de establecimiento de confianza y, después, un proceso de protección de tramas en cada dirección del enlace. 

A nivel conceptual, el flujo puede explicarse así:

1. Dos equipos Ethernet acuerdan participar en un dominio protegido. 
2. Se autentican y obtienen material criptográfico, normalmente con ayuda de mecanismos complementarios de control de acceso y gestión de claves. 
3. A partir de ese momento, las tramas del enlace pueden enviarse protegidas con MACsec. 
4. El receptor valida integridad y autenticidad antes de aceptar el tráfico. 

En muchos despliegues, la negociación y distribución de claves se apoya en MKA y en mecanismos basados en 802.1X, aunque para una introducción básica basta con entender que MACsec necesita un plano de control para autenticar y gestionar claves, además del plano de datos que protege las tramas. 

## Protección por enlace frente a protección extremo a extremo

La diferencia más importante que debe quedar clara es que MACsec suele proporcionar protección **por enlace** o por tramo Ethernet, no protección extremo a extremo a través de toda una red IP. Si el tráfico atraviesa varios saltos, hay que decidir en qué enlaces se activa MACsec y dónde termina esa protección. 

Esto tiene ventajas y limitaciones. La ventaja es que el rendimiento suele ser muy bueno y el funcionamiento es transparente para capas superiores; la limitación es que un paquete puede salir de un enlace protegido y entrar en otro distinto, lo que obliga a diseñar cuidadosamente el dominio de confianza. 

## Ventajas de MACsec

Las ventajas más importantes para una primera aproximación son estas:

- Opera en capa 2 y resulta transparente para protocolos IP y aplicaciones superiores. 
- Puede tener bajo impacto de latencia y buen rendimiento cuando existe soporte hardware. 
- Es especialmente adecuado para proteger enlaces Ethernet de infraestructura, backhaul y fronthaul. 
- Proporciona confidencialidad e integridad sin necesidad de rediseñar la aplicación que usa el enlace. 

## Limitaciones de MACsec

También conviene presentar claramente sus límites:

- No es la mejor opción cuando se necesita protección IP extremo a extremo a través de redes amplias o heterogéneas. 
- Requiere soporte en equipos y puertos Ethernet compatibles. 
- En topologías con múltiples saltos, hay que planificar qué enlaces quedan cubiertos y cómo se mantiene la cadena de confianza. 
- No sustituye por sí solo a otros controles de seguridad como segmentación, autenticación de acceso, listas de control o monitorización. 

## Relación con 5G y redes de transporte

Aunque MACsec no es una tecnología específica de 5G, su relevancia en 5G viene del uso intensivo de Ethernet en fronthaul, midhaul y backhaul. Distintos trabajos y documentos técnicos lo presentan como una solución eficiente para proteger transporte Ethernet en Open RAN y redes móviles de nueva generación. 

En una explicación docente sencilla puede decirse que, si N2 o N3 atraviesan una infraestructura Ethernet, MACsec puede proteger el **enlace Ethernet subyacente** sobre el que viajan esos flujos. En cambio, si lo que se busca es proteger el trayecto IP entre funciones 5G, suele considerarse antes IPsec o, en algunos laboratorios y redes privadas, WireGuard. 

## Ejemplos de uso

Algunos escenarios donde MACsec tiene mucho sentido son:

- Enlaces switch-switch dentro de un campus o CPD. 
- Enlaces entre router y equipo de agregación Ethernet. 
- Transporte Ethernet en backhaul o fronthaul móvil. 
- Entornos donde se necesita alta velocidad con protección integrada en hardware. 

Un ejemplo intuitivo es este: si dos edificios de una universidad están unidos por fibra Ethernet y se quiere impedir que alguien intercepte o altere el tráfico en ese tramo, MACsec es una opción muy natural. 

## Conceptos mínimos que debe recordar el alumnado

Al terminar la lectura, el alumnado debería poder recordar estas ideas:

- MACsec es seguridad para Ethernet en capa 2. 
- Protege confidencialidad, integridad y autenticidad de origen de las tramas. 
- Normalmente protege enlaces o segmentos Ethernet concretos, no todo el trayecto IP extremo a extremo. 
- Su uso es muy razonable en infraestructura, centros de datos y transporte de redes móviles. 
- No compite siempre con IPsec; muchas veces ambos se complementan. 

## Preparación para una práctica posterior

Antes de un laboratorio sobre MACsec conviene que el alumnado repase cuatro preguntas:

1. ¿Qué equipos del escenario soportan MACsec? 
2. ¿Qué enlace exacto se quiere proteger? 
3. ¿Dónde empieza y dónde termina el dominio de confianza? 
4. ¿Cómo se comprobará que el tráfico realmente va cifrado o autenticado? 

En la práctica, lo habitual será verificar interfaces, activar la protección en ambos extremos, revisar el estado operativo y comparar capturas o contadores antes y después de aplicar MACsec. Ese trabajo práctico tiene más sentido cuando primero se entiende bien que el objetivo es proteger el transporte Ethernet y no una aplicación concreta. 

## Preguntas de autoevaluación

1. ¿En qué capa del modelo de red opera MACsec? 
2. ¿Qué diferencia principal existe entre MACsec e IPsec? 
3. ¿Por qué MACsec se considera apropiado para enlaces Ethernet de alto rendimiento? 
4. ¿Qué significa que MACsec ofrece protección por enlace? 
5. ¿En qué escenarios de 5G puede resultar útil aunque no sea un protocolo específico de 5G? 
