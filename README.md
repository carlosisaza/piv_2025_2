# 🏙️ Proyecto Integrado 5 – Analizar y predecir la deserción de clientes (churn)

## Definición de la Problemática y Selección del Dataset (EA1)


## 📊 1. Problema / Caso de Uso

### ¿Qué necesidad resolverás? (El Problema)
La necesidad principal es transformar el proceso de retención de clientes de un modelo reactivo (actuar solo cuando el cliente llama a cancelar) a un modelo proactivo (identificar quién podría irse antes de que llame). El problema es que la empresa Telco desconoce los factores y perfiles de los clientes que abandonan el servicio, lo que genera una alta tasa de abandono (churn) y una pérdida financiera significativa, dado que es más costoso adquirir nuevos clientes que retener los existentes.

### ¿Para quién? (El Cliente)
La solución está dirigida principalmente al Departamento de Retención de Clientes y al Departamento de Marketing de la empresa Telco.

### ¿Por qué requiere analítica? (La Justificación)
Con un volumen de 7,043 clientes, cada uno con 21 atributos, es humanamente imposible para el departamento de retención identificar patrones de abandono de forma manual. La analítica (específicamente la estadística descriptiva y el perfilamiento) es indispensable para procesar este volumen de datos y responder preguntas clave: ¿Qué tipo de contrato es más propenso al abandono? ¿La falta de soporte técnico impacta la decisión? ¿Los clientes con más servicios contratados son más leales? Solo la analítica puede generar los insumos accionables (perfiles de riesgo) que el equipo de retención necesita para focalizar sus esfuerzos.

---

## 📊 2. Selección del Dataset

Fuente Seleccionada: Se ha seleccionado un dataset de Kaggle.

Nombre del Dataset: Telco Customer Churn.

---

## 🧩 3. Variables relevantes (Clave)

Se han identificado 5 variables clave (de las 21 disponibles) que son fundamentales para el análisis de perfilamiento:

1.	Churn (Variable Objetivo):
•	Descripción: Indica si el cliente abandonó ("Yes") o no ("No") en el último mes.
•	Utilidad: Es la variable principal de nuestro análisis. Todas las demás variables se cruzarán contra esta para calcular la tasa de abandono de cada segmento.

2.	Contract (Tipo de Contrato):
•	Descripción: El tipo de contrato del cliente (Ej. "Month-to-month", "One year", "Two year").
•	Utilidad: Es una de las variables predictoras más fuertes. Nuestra hipótesis es que los clientes “Mes a Mes” tienen una tasa de abandono significativamente mayor al no tener ataduras a largo plazo.

3.	tenure (Antigüedad):
•	Descripción: El número de meses que el cliente ha estado con la compañía.
•	Utilidad: Permite perfilar si el abandono ocurre en clientes nuevos (con baja antigüedad, quizás por problemas de onboarding) o en clientes antiguos (quizás por falta de ofertas de renovación).

4.	TechSupport (Soporte Técnico):
•	Descripción: Indica si el cliente tiene contratado el servicio de soporte técnico ("Yes", "No", "No internet service").
•	Utilidad: Es clave para el perfilamiento de servicios. Nos permite evaluar si la percepción de "estar protegido" con soporte técnico reduce activamente la tasa de abandono.

5.	MonthlyCharges (Cargos Mensuales):
Descripción: El monto que el cliente paga cada mes.

Utilidad: Permite analizar la sensibilidad al precio. Podremos determinar si los clientes que pagan montos más altos tienen mayor probabilidad de irse, justificando estrategias de descuento focalizadas.

---

## 🧩 4. Trazabilidad del Dataset (Fuente y Licencia)

Enlace: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

Autor/Publicador: BlastChar

Fuente Original (Citada por el publicador): IBM Sample Data Sets

Licencia: No especificada (Unknown).


## Procedimiento de Limpieza y Enriquecimiento (Fase 2)

Para la segunda fase del proyecto, se implementó un proceso de depuración y enriquecimiento de datos utilizando el script analysis_ea2.py. El procedimiento se estructuró en tres pasos:

i.	Limpieza e Imputación: Se detectaron valores nulos en la variable TotalCharges (espacios vacíos correspondientes a clientes nuevos). Estos fueron imputados con el valor 0. Además, se normalizaron las variables categóricas (como PaymentMethod) convirtiendo los textos a minúsculas para estandarización.

ii.	Enriquecimiento Temporal: Dado que el dataset original carecía de fechas, se generaron datos sintéticos coherentes. Utilizando la variable tenure (antigüedad en meses) y una fecha de corte al 01/01/2025, se calculó retrospectivamente la SubscriptionDate para cada cliente.
iii.	Desglose de Variables: Se derivaron nuevas columnas: Año, Mes y Día, habilitando el análisis de estacionalidad.

## Metodología

5.1. Enfoque del Proyecto

Se utiliza un enfoque analítico-descriptivo, centrado en la ingeniería de datos (ETL) y el análisis exploratorio (EDA).

Herramientas Tecnológicas

•	Python (Pandas/Seaborn): Para manipulación de datos y visualización.

•	SQLite: Para almacenamiento y consultas SQL.

