# vibe-seed

Seed repo para vibe coding con IA.

## Qué es

Este repo contiene archivos `.md` que **guían a la IA** para que construya el proyecto entero sin alucinar ni perder el control. La IA lee estos archivos, ejecuta, y los **reescribe** al final de cada sesión para mantener el contexto actualizado.

## Cómo funciona

```bash
git clone <repo> mi-proyecto
cd mi-proyecto
```

Le dices a la IA:

> *"Hey, lee AGENTS.md, ARCHITECTURE.md y PLAN.md. El proyecto se llama X, es un clon de WhatsApp para CRM con React Native + Meta API. Crea todo desde cero."*

La IA:
1. Lee los `.md` → entiende reglas, estructura, tecnologías
2. Pide detalles si faltan
3. Genera configs, estructura, código, tests
4. **Actualiza los `.md`** al final de cada sesión
5. Nunca se desvía porque los `.md` la mantienen en cintura

## Archivos

| Archivo | Propósito |
|---|---|
| `AGENTS.md` | Reglas, stack, session log — la fuente de verdad |
| `ARCHITECTURE.md` | Decisiones de arquitectura, estructura de carpetas |
| `PLAN.md` | Requirements, milestones, tareas activas |

La IA escribe y reescribe estos archivos. El humano solo da la idea inicial y revisa.
