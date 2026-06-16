# 🚕 Proyecto de Automatización: Urban Routes (Sprint 9)

## 📌 Descripción del Proyecto
Este proyecto automatiza pruebas del flujo crítico de la plataforma **Urban Routes**, validando que un usuario pueda completar correctamente el proceso de solicitud de un taxi, desde la configuración de la ruta hasta la asignación dinámica de un conductor.

El objetivo principal es **detectar fallos en flujos críticos**, especialmente aquellos relacionados con:
- Elementos dinámicos
- Validaciones externas
- Modales emergentes
- Eventos asincrónicos propios de aplicaciones modernas

---

## ✅ Casos de Prueba Automatizados

El framework cubre los siguientes escenarios:

1. Configuración de dirección de origen y destino  
2. Selección de tarifa *Comfort*  
3. Validación de número telefónico  
4. Asociación de tarjeta de crédito  
5. Envío de comentarios adicionales  
6. Selección de extras (mantas, helado, etc.)  
7. Solicitud del servicio de taxi  
8. Validación de asignación dinámica de conductor  
9. Verificación de texto dinámico  

## 🧠 Retos Técnicos Abordados

- Manejo de **elementos dinámicos** que aparecen tras acciones del usuario  
- Sincronización de eventos asincrónicos usando `WebDriverWait` + `ExpectedConditions`  
- Validación de **textos variables sin hardcodear valores estáticos**  
- Separación clara de responsabilidades mediante **Page Object Model (POM)**  
---
## 🛠️ Tecnologías y Metodologías

Para garantizar escalabilidad y mantenibilidad, el proyecto utiliza:

- **Lenguaje:** Python 3.13  
- **Framework de Pruebas:** PyTest  
- **Automatización Web:** Selenium WebDriver  
- **Patrón de Diseño:** Page Object Model (POM)  
- **Principios:** Single Responsibility Principle & Clean Code  


## 📁 Estructura del Framework

La arquitectura del proyecto es POM (Page Object Model) organiza el código en paquetes:

- data/data.py = datos de prueba 
- helpers/utilities.py = retrieve_phone_code
- pages/urban_routes_page.py = localizadores, acciones y validaciones 
- test.py/test_urban_routes.py = ejecucion de pruebas


# Esta estructura facilita:
- Mantenimiento
- Escalabilidad
- Reutilización de código
- Lectura clara de los flujos de prueba

. Instalar dependencias:
   ```bash
   pip install selenium pytest requests

   pytest main.py
# 📌 Buenas Prácticas Aplicadas

- Esperas explícitas en lugar de sleep

- Assertions orientadas al comportamiento del usuario

- Localizadores centralizados

- Código legible y desacoplado

## Resultados de la Ejecución
Se realizaron 8 pruebas integrales cubriendo todo el flujo de usuario, obteniendo un resultado exitoso (100% pass rate).