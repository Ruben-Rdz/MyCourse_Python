# Cloud, AWS e Infraestructura.

## Indice 
- Módulo 1: Fundamentos del Cloud y Amazon Web Services
- Módulo 2: Introducción a Amazon Web Services
- Módulo 3: Infraestructura Tradicional y Compute Clásico
- Módulo 4: Almacenamiento y Bases de Datos
- Módulo 5: Contenedores y Docker
- Módulo 6: Redes y Arquitectura
- Módulo 7: Principios de Diseño Cloud Native
- Módulo 8: Serverless e Infraestructuras Nativas del Cloud
- Módulo 9: DevOps y Cultura de Automatización
- Módulo 10: Infraestructura como Código
- Módulo 11: CI/CD y Despliegue
- Módulo 12: Observabilidad y Operaciones
- Módulo 13: Seguridad, Gobernanza y Finanzas
- Módulo 14: Kubernetes
- Módulo 15: Kubernetes en Amazon Web Services (EKS)
- Proyecto Final


### Módulo 1: Fundamentos del Cloud y Amazon Web Services

#### Introducción a la nube.
##### Modelos de servicio
- Infrastructure as a service (IaaS): Proporciona recursos de computación virtualizados como servidores, almacenamiento y redes. 
- Platform as a Service (PaaS): Ofrece una plataforma completa para desarrollar, ejecutar y gestionar aplicaciones sin gestionar la infraestructura subyacente.
- Software as a Service (SaaS): Aplicaciones completas entregadas a través de Internet, listas para usar.

##### Modelos de Despliegue
- Nube Pública: Recursos compartidos ofrecidos por proveedores como AWS, Azure o Google Cloud.
- Nube Privada: Infraestructura dedicada exclusivamente a una organización.
- Nube Híbrida: Combinación de nubes públicas y privadas que trabajan conjuntamente.

##### Terminología elementa 

- Serverless: Modelo donde el proveedor gestiona completamente la infraestructura
- Lambda: Funciones que se ejecutan en respuesta a eventos sin gestionar servidores
- Escalabilidad horizontal: Añadir más instancias para distribuir la carga
- Escalabilidad vertical: Aumentar los recursos de una instancia existente
- Región: Ubicación geográfica donde se alojan los recursos cloud
- Zona de disponibilidad: Centros de datos aislados dentro de una región

##### Importancia del Cloud Computing 

- Base para conceptos avanzados: Tecnologías como serverless y contenedores se construyen sobre estos principios
- Toma de decisiones: Permite elegir las soluciones más apropiadas para cada caso de uso
- Optimización de costos: Entender los modelos de precios ayuda a diseñar arquitecturas eficientes
- Comunicación efectiva: Facilita la colaboración con equipos técnicos y stakeholders

#### ¿Qué es el Cloud Computing?

##### ¿Qué es el Cloud Computing? 

-  Este debe cumplir con 5 caracteristicas: 
    - On demand Self-service 
    - Broad Network access
    - Resource Pooling
    - Rapid Elasticity
    - Measured services 

1. Autoservicio Bajo Demanda (On-Demand Self-Service)

El usuario debe poder provisionar recursos computacionales automáticamente, sin necesidad de interactuar con personal de la empresa proveedora. No se requiere abrir tickets ni hacer llamadas telefónicas.

Ejemplo: En Amazon Web Services, puedes hacer clic en un botón y levantar un servidor inmediatamente. Si un proveedor de hosting requiere que abras un ticket para obtener un servidor, no cumple con esta característica y, por tanto, no es considerado cloud computing.

2. Acceso Amplio a la Red (Broad Network Access)

Los servicios deben estar disponibles a través de protocolos de red estándar. Esto significa que debes poder acceder a ellos mediante HTTP, APIs REST, o cualquier otro mecanismo de red estandarizado.

Esta característica permite gestionar la infraestructura desde múltiples dispositivos: portátiles, móviles, navegadores web o scripts automatizados.

3. Agrupación de Recursos (Resource Pooling)

El proveedor debe mantener un conjunto (pool) de recursos físicos compartidos entre múltiples clientes. Cuando solicitas un servidor o una base de datos, no sabes (ni necesitas saber) en qué máquina física específica se ejecutará.

Este modelo se conoce como arquitectura multi-tenant: los mismos recursos físicos son compartidos por distintos clientes. Por ejemplo:

Un cliente puede tener un servidor ejecutándose en una máquina física específica
Otro cliente puede tener su servidor en una máquina diferente
Un tercer cliente podría tener su servidor en la misma máquina que el primero
Nota importante: Aunque no controlas la máquina física específica, sí puedes elegir aspectos de alto nivel como el país o la región donde se crearán tus recursos (concepto que se profundizará al estudiar las regiones de Amazon Web Services).

4. Elasticidad Rápida (Rapid Elasticity)

Los recursos deben poder escalarse de forma rápida y, idealmente, automática.

Ejemplo práctico: Imagina que tienes una tienda online funcionando en un servidor. Durante el Black Friday, el tráfico se multiplica exponencialmente. Un servicio cloud real debe permitirte escalar rápidamente a más servidores para:

Mantener tiempos de respuesta aceptables
Evitar la sobrecarga del servidor original
Ofrecer una mejor experiencia al usuario
Esta elasticidad funciona en ambas direcciones: puedes escalar hacia arriba cuando necesitas más recursos y hacia abajo cuando la demanda disminuye.

5. Servicio Medido (Measured Service)

Como el modelo principal de negocio es el pago por uso, debe existir un sistema de medición preciso del consumo de recursos. Esto incluye:

Horas de uso de CPU
Gigabytes de almacenamiento utilizados
Número de peticiones a una API
Ancho de banda consumido
Cualquier otro recurso facturable
Sin esta capacidad de medición, no es posible implementar un modelo de pago por uso justo y transparente.

#### Ventajas
Existen diversas ventajas por mencionar un groso general: 
 - No tenemos un costo de inversión inicial alto.
 - El costo pasa de CAPEX a OPEX 
 - En negocios emergentes esto supone un menor riesgo.
 - Delega responsabilidades a terceros (proveedor de la nube), como mantenimiento, energia electrnica, desastres naturales. 
 - Economias a escala:
  - Inversión en eficiencia 
  - Optimización de recursos 
  - Reducción de emisiones
 
#### Necesidades del servicio On-promise
CUando las empresas tienen servicios en legacy es complejo realizar un traslado a la nube, eso frena el cambio. 

#### Historia de Cloud

##### Hechos

- 2003 Chris Pinkham y Benjamin Black, escribieron el papper que presentaba una solución innovadora a estos problemas. 
    - Infraestructura completamente estandarizada
    - Autmatización completa de procesos. 
    - Servicios basados en web, controlables a través de la red. 

- 2004 Jeff Bezos aprobo la propuesta y coloco a un equipo en africa a desarrollar la infraestructura.

- 2004 Primeros servicios de AWS
    - 11.04 SQS - Simple Queue Service - Debut oficial de AWS.
    - 03.06 S3  - Simple Storage Service. 
    - 08.06 Ec2 - Elastic Cloud Compute - Primer sistema que se abrió al mundo y donde era posibel que todos el publico desplegará un equipo en la nube para scripts de python, aplicaciones o algún otro software. 

- 2008 Google App Engine - También se introdujo en el negocio del cloud. 

- 2010 Microsoft - Azure - Plataforma de servicios en la nube. 

**Conclusión**: Nos encontramos con una empresa que comenzo vendiendo libros en internet, que el volumen e inversión genero un proyecto secundario, el cual años más tarde paso a ser el principal. Desde 2003 hasta hoy han pasado 24 años, tiempo donde esto ha madurado de una forma incesante. La industria cuenta hoy herrameintas diversas para generar sistemas automaticos, orquestados y especialziados. 

##### Casos de Uso

**Netflix**: Esta corporación migro durante 7 años a AWS, derivado de un problema con sus BD, este se corrompió y para solucionar el error demoraron 3 días, gran impacto economico y de confianza con sus usuarios. 

**Arbnb**: Esta empresa comenzo con hiosting tradicional, sin embargo, derivado de las ventajas y acuerdos que ofrece un mounstro como AWS, se trasladaron un año más tarde a AWS. 

**Ventaja general** Una visión general de AWS es dar a todos los emprendedores las mismas herramientas, la misma exposición global con el menor desembolso inicial. Es decir, una empresa puede comenzar a trabjar con clientes de todo el mundo, una vez que integra sus servicios en AWS.


**Casos de uso generales:** 
- Desarrollo de aplicaciones móviles y web: Backend escalable y servicios de autenticación
- Distribución de contenido: Libros, multimedia, streaming
- Análisis de datos: Procesamiento masivo y data warehousing
- Copias de seguridad y recuperación: Almacenamiento redundante y duradero
- Inteligencia artificial: Machine Learning, modelos de IA generativa 
- Hosting y plataformas: Empresas como Vercel, Neon y Supabase construyen sus servicios sobre AWS


##### Modelos de servicio

**Capas de abstracció** 
1. Capa de infraestructura 
2. Capa de plataforma 
3. Capa de aplicación

Con base en el nivel de abstracción que se este utilizado nos encontraremos con mayores o menores retos, es decir, las actividades que se desarrollaran en cada tipo de escenario será muy diferentes. 

**Según su nivel de abstraccion**

**En la capa de infraestructura:** se gestionan servidores físicos o virtuales, configuración de red, almacenamiento y bases de datos a bajo nivel.

**En la capa de plataforma:** se instala el sistema operativo, se configura el runtime del servidor (como Python o Node.js) y se prepara el entorno de ejecución.

**En la capa de aplicación:** se desarrolla el código de la aplicación directamente, sin preocuparse por la infraestructura subyacente.

**IaaS: Infrastructure as a Service**

El proveedor se encarga de gestionar el harware fisico, los servidores virtuales, el almacenamiento y la red. El usuario debe Elegir e instalar el sistema operativo. Configurar el runtime de la aplicación, Desplegar y gestionar la aplicación. entre otras.

**Productos de AWS en la capa IaaS**

EC2 (Elastic Compute Cloud): para crear y gestionar servidores virtuales

VPC (Virtual Private Cloud): para configurar redes virtuales privadas

EBS (Elastic Block Store): para gestionar almacenamiento en bloques

**PaaS: Platform as a Service**

El proveedor cloud gestiona no solo la infraestructura, sino tambien el SO y runtime. El usuario debe desplegar su código y gestionar su lógica de negocio.

**Productos de AWS en la capa PaaS**

Elastic Beanstalk: permite desplegar aplicaciones web sin preocuparse por la infraestructura subyacente (utiliza EC2 internamente)

Lambda: servicio de funciones serverless donde solo se despliega el código

RDS (Relational Database Service): para gestionar bases de datos relacionales sin preocuparse del sistema operativo o la configuración del servidor

**SaaS: Software as a Service**

En este modelo no es necesario desarrollar la aplicaicón, directamente se puede consumir de la misma que construyó un tercero.

Ejemplos: 
- Salesforce: CRM en la nube
- Notion: herramienta de productividad y documentación
- Slack: plataforma de comunicación empresarial
- Discord: plataforma de comunicación y comunidades

**FaaS: Functions as a Service** 

Es también conocido el termino, donde se establece el uso de funciones unicamnete. No se tiene preocupación del servidor, runtime o las librerias subyacentes. 

Ejemplo: AWS Lambda, el desarrollador escribe y despliega funciones que se ejecutan en respuesta a eventos, sin gestionar ningun aspecto de la infraestructura. 

**Conclusiones**

- Si se necesita control total: se puede trabajar en la capa IaaS, gestionando servidores EC2 directamente
- Si se prefiere enfocarse en el código: se puede trabajar en la capa PaaS, utilizando servicios como Beanstalk o Lambda
- Si solo se necesita usar software: se pueden consumir servicios SaaS disponibles en AWS

La decisión depende de varios factores:

- El nivel de control requerido sobre la infraestructura
- Los recursos y conocimientos del equipo
- Los requisitos específicos del proyecto
- El balance entre flexibilidad y simplicidad

La decisión de trabjar en una u otra capa depende totalmente de las necesidades del proyecto que stemos trabajndo, es decir, no podemos plantear un razonamiento general o el mejor para todo. Deende como se describre antes de varios factores. 


##### Modelos de despligue 

###### Nube Publica

Cualquier proveedor de nuber que presta servicios de forma general al publico, se centra en bajar costos. 
Gran disponibilidad de recursos desde un inicio.

###### Nube Privada

Las empresas cuentan con su propia infraestructura (on-promise), se aplica cuando por regualizaciones es necesario tener control fisico de los componentes.
- Alta inversión inicial. 
- Nube administratida totalmente por el propietario. 
- Existen servicios como AWS Hybrid Cloud, para darle un "uso" "interfaz" a los recursos, con esto se homologan o estandarizan todos los servicios que podemos desplegar. 

###### Nube Hibrida 

Se puede tener la combinación de Nuber pública y nube privda, para utilizar lo recursos propios que ya se tenian, para cumplir con normativas, para mantener el control de ciertas partes de la infraestructura. 

- Ley Organiza de Protección de Datos (LOPD), son algunas de las reglas que se deben cumplir.

###### Multicloud 

Acá debemos tener cuidado, no confundir con nube pública. Acá hablamos de multimarcas, donde por diversos motivos trabajmos con más de un proveedr de nube. 

- Para tener mayor numero de opciones de servicios
- Para buscar costos menores entre proveedores, 
- Para tener alta disponiblidad, en caso de que el proveedor A falle, se inicial el proveedor C. 
- Por regulación, podemos tener despliiegues a nivel mundial estratificando las zonas a fin de cumplir cualquier condicional en ley. 

##### Modelo de Responsabilidad Compartida

User : 

    - Data  protection & encript of data user 
    - Identity & Access Management 

Compartido:

    - Application and performance 
    - Network and Firewall protection
    - OS and software Updates
    - 

AWS:

    - Physical infraestructure security 
    - Hardware like SSD, PC, Switchs, etc- 


Desde el panorma general es importante manejar de forma correcta la posición que queremos asumir, es decir, según el nivel al que nos manejamos (Modes de Servicio) será el nivel de responsabilidad.  

Es decir, si valuamos entre IaaS vs PaaS, notaremos que hay una cantidad de cosas indispensables para la seguridad. Por ser puntuales, en IaaS debemos considerar las actualizaciones del SO, puertos, conexiones, contraseñas, entre otras. 

Por otro lado si utilizamos un servicio más abstracto, como una lambda, la responsabilidad del usuario es determinar que la función esta trabajndo correctamente. AWS se encargará de la seguridad del código, de las conexiones, etc.

Finalmente, es importante comprender que elegir el nivel de servicio que estaremos trabajndo depende no sólo de la capacidad técnica (IaaS requiere mucho más experiencia), también se debe afrontar el nivel de responsabilidad con el que queremos trabajar. 

##### Introducción a Amazon Web Services (AWS)

###### Servicios principales que se abordarán

Dado que AWS cuenta con más de 200 servicios, es inviable y poco práctico intentar cubrirlos todos. El enfoque se centra en los servicios fundamentales que permiten construir arquitecturas robustas y escalables.

Servicios de Compute (Computación)

- EC2: Servidores virtuales tradicionales
- Lambda: Funciones serverless
- EKS: Kubernetes gestionado
- Fargate: Contenedores sin gestión de servidores

Storage y Database (Almacenamiento y bases de datos)
- S3: Almacenamiento de objetos y ficheros
- EBS: Volúmenes de datos para servidores EC2
- RDS: Bases de datos relacionales gestionadas
- DynamoDB: Base de datos NoSQL

Networking (Redes)
- VPC: Redes privadas virtuales con sus subredes
- Security Groups (SG): Firewalls a nivel de instancia
- Load Balancers: Balanceadores de carga para distribuir tráfico

Security (Seguridad)
- IAM: Gestión de usuarios, roles y permisos
- KMS: Gestión de claves de cifrado
- CloudTrail: Auditoría y monitoreo de acciones en la cuenta

Arquitectura Serverless

La arquitectura serverless permite construir aplicaciones sin gestionar servidores directamente:

- Lambda: Ejecución de funciones en respuesta a eventos
- API Gateway: Creación y gestión de APIs REST y WebSocket
- SQS, SNS y EventBridge: Sistemas de colas, notificaciones y buses de eventos para arquitecturas event-driven

Estos servicios son fundamentales para implementar patrones de diseño modernos como Event Driven Design, donde las aplicaciones reaccionan a eventos en lugar de esperar requests síncronas. Esto permite construir sistemas más escalables y con menor acoplamiento entre componentes.

Contenedores
- Docker: Containerización de aplicaciones
- EKS: Elastic Kubernetes Service, la implementación de Kubernetes en AWS

Distribución de contenido
- CloudFront: CDN (Content Delivery Network) para distribución global de contenido

Infraestructura como Código (IaC)

Terraform será la herramienta principal para gestionar infraestructura como código. Aunque AWS ofrece su propio CDK (Cloud Development Kit), Terraform presenta ventajas significativas:

 - Multi-cloud: Funciona con AWS, Azure, GCP y otros proveedores
 - Flexibilidad: Permite gestionar recursos fuera de AWS (MongoDB, GitHub, etc.)
 - Portabilidad: El conocimiento es transferible entre diferentes plataformas





### Módulo 2: Introducción a Amazon Web Services
### Módulo 3: Infraestructura Tradicional y Compute Clásico
### Módulo 4: Almacenamiento y Bases de Datos
### Módulo 5: Contenedores y Docker
### Módulo 6: Redes y Arquitectura
### Módulo 7: Principios de Diseño Cloud Native
### Módulo 8: Serverless e Infraestructuras Nativas del Cloud
### Módulo 9: DevOps y Cultura de Automatización
### Módulo 10: Infraestructura como Código
### Módulo 11: CI/CD y Despliegue
### Módulo 12: Observabilidad y Operaciones
### Módulo 13: Seguridad, Gobernanza y Finanzas
### Módulo 14: Kubernetes
### Módulo 15: Kubernetes en Amazon Web Services (EKS)
### Proyecto Final



