# 🚀 Automatización de Red con Cisco CSR1000v

<p align="center">
  <img src="https://img.shields.io/badge/Cisco-IOS%20XE-blue?style=for-the-badge&logo=cisco" />
  <img src="https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Automation-Ansible-red?style=for-the-badge&logo=ansible" />
  <img src="https://img.shields.io/badge/API-NETCONF%20%7C%20RESTCONF-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Testing-pyATS%20%7C%20Genie-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
</p>

---

## 👨‍💻 Autor

**Diego Molina**
🔗 GitHub: https://github.com/diemolinar-prog

---

## 📌 Descripción

Este proyecto implementa un flujo completo de **automatización de red** sobre un router **Cisco CSR1000v**, integrando herramientas modernas utilizadas en entornos reales de ingeniería:

* Automatización con **Ansible**
* Validación con **NETCONF / RESTCONF**
* Testing con **pyATS / Genie**
* Control de versiones con **Git**

---

## 🎯 Objetivos

✔️ Capturar estado inicial de red (Baseline)
✔️ Automatizar configuraciones de red
✔️ Validar cambios mediante APIs
✔️ Generar evidencia técnica reproducible
✔️ Aplicar buenas prácticas DevNet

---

## 🧱 Arquitectura del Proyecto

```bash
ep3-automatizacion-005D-11/
│
├── fase1_baseline/                # Estado inicial del router
├── fase2_aprovisionamiento/      # Configuración automatizada (Ansible)
├── fase3_validacion_netconf/     # Validación con NETCONF
├── fase4_validacion_restconf/    # Validación con RESTCONF
├── fase5_reporte/                # Evidencia final
│   └── evidencias/
│
└── playbook_005D-11.yaml         # Playbook principal
```

---

## ⚙️ Tecnologías Utilizadas

| Tecnología    | Uso                     |
| ------------- | ----------------------- |
| Python 3      | Scripts de validación   |
| Ansible       | Automatización          |
| pyATS / Genie | Testing y baseline      |
| NETCONF       | Validación estructurada |
| RESTCONF      | Validación vía API      |
| SSH           | Acceso remoto           |
| Git           | Control de versiones    |

---

## 🧪 Desarrollo por Fases

### 🔹 Fase 1: Baseline

* Captura del estado inicial del router
* Uso de pyATS para inventario y conexión

---

### 🔹 Fase 2: Aprovisionamiento

Automatización con Ansible:

✔️ Hostname
✔️ Banner
✔️ NTP
✔️ Interfaz WAN
✔️ Loopback
✔️ NETCONF / RESTCONF

✔️ **Configuración idempotente validada**

---

### 🔹 Fase 3: Validación NETCONF

Validación automatizada de:

* Hostname
* Loopback
* WAN
* NTP

📌 Resultado:

```bash
CONFORME
```

---

### 🔹 Fase 4: Validación RESTCONF

Validación mediante API REST:

✔️ Estado de interfaces
✔️ Configuración aplicada

📌 Resultado:

```bash
CONFORME
```

---

### 🔹 Fase 5: Reporte Final

#### 📊 Snapshot Final

Debido a incompatibilidad de **Genie con banner personalizado**, se utilizó validación manual:

```bash
show ip interface brief
show running-config
show ip route
```

📄 Evidencia:

```bash
fase5_reporte/evidencias/snapshot_final_manual.txt
```

---

#### 🔍 Comparación (Diff)

Cambios detectados:

* Hostname → RTR-SEGPROV
* Loopback10 → 10.5.11.1
* WAN activa vía DHCP
* NTP configurado
* NETCONF / RESTCONF habilitados
* Banner de seguridad aplicado

📄 Archivo:

```bash
diff_005D-11.txt
```

---

## ⚠️ Consideración Técnica

El módulo **Genie Learn** presentó problemas de conexión debido a:

* Banner personalizado
* Manejo de prompts en IOS XE

✔️ Se implementó solución alternativa mediante evidencia CLI
✔️ En entornos reales, esta práctica es válida

---

## 🏆 Resultado Final

```bash
===================================
RESULTADO FINAL DE AUTOMATIZACION
===================================
ESTADO: CONFORME
```

---

## 🚀 Habilidades Demostradas

* Automatización de redes Cisco
* Uso de APIs (NETCONF / RESTCONF)
* Troubleshooting real
* Integración de herramientas DevNet
* Documentación técnica profesional

---

## 📬 Contacto

💻 GitHub: https://github.com/diemolinar-prog

---

<p align="center">
  <b>✔️ Proyecto completado exitosamente</b><br>
  <i>Automatización, validación y documentación de red de nivel profesional</i>
</p>
