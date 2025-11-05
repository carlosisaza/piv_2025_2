# 🏙️ Proyecto Integrado 5 – Analizar y predecir la deserción de clientes (churn)

## 📘 1. Descripción del proyecto

El propósito principal de este proyecto es construir modelos de Machine Learning que permitan:

- Predecir si un cliente abandonará el servicio.
- Identificar patrones de comportamiento asociados al churn.
- Diseñar estrategias de retención basadas en datos.

## 📊 2. Dataset utilizado

**Fuente:** Kaggle  
**Nombre:** *Telco Customer Churn*  
**Autor:** [IBM Sample Data Sets]  
**Enlace:** [https://www.kaggle.com/datasets/blastchar/telco-customer-churn]
**Archivo principal:** `WA_Fn-UseC_-Telco-Customer-Churn.csv`  
**Licencia:** Según Kaggle, licencia abierta (normalmente *CC BY 4.0*).  
**Fecha de descarga:** Octubre de 2025  

Este dataset contiene información de clientes de una empresa de telecomunicaciones. Cada fila representa un cliente y cada columna describe atributos relacionados con servicios contratados, comportamiento de pago, y datos demográficos.

---

## 🧩 3. Variables relevantes
| Columna | Descripción |
|---------|-------------|
| `customerID` | Identificador único del cliente |
| `gender` | Género del cliente (Male, Female) |
| `SeniorCitizen` | Si el cliente es adulto mayor (1 = sí, 0 = no) |
| `Partner` | Si tiene pareja (Yes, No) |
| `Dependents` | Si tiene personas a cargo (Yes, No) |
| `tenure` | Meses como cliente |
| `PhoneService` | Si tiene servicio telefónico (Yes, No) |
| `MultipleLines` | Si tiene múltiples líneas (Yes, No, No phone service) |
| `InternetService` | Tipo de internet (DSL, Fiber optic, No) |
| `OnlineSecurity` | Servicio de seguridad en línea (Yes, No, No internet service) |
| `OnlineBackup` | Servicio de respaldo en línea (Yes, No, No internet service) |
| `DeviceProtection` | Protección de dispositivos (Yes, No, No internet service) |
| `TechSupport` | Soporte técnico (Yes, No, No internet service) |
| `StreamingTV` | Servicio de TV por streaming (Yes, No, No internet service) |
| `StreamingMovies` | Servicio de películas por streaming (Yes, No, No internet service) |
| `Contract` | Tipo de contrato (Month-to-month, One year, Two year) |
| `PaperlessBilling` | Si usa facturación electrónica (Yes, No) |
| `PaymentMethod` | Método de pago (Electronic check, Mailed check, etc.) |
| `MonthlyCharges` | Valor mensual facturado |
| `TotalCharges` | Total facturado durante la relación con el cliente |
| `Churn` | Variable objetivo: si el cliente se fue (Yes, No) |

---

## 🧠 4. Ideas para análisis

Análisis exploratorio de churn por tipo de contrato, edad o método de pago.

Visualización de correlaciones entre servicios contratados y deserción.

Modelos predictivos: regresión logística, árboles de decisión, Random Forest, XGBoost.

Segmentación de clientes por riesgo de churn.

---
