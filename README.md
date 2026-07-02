Los métodos obtener_* devolverán la estructura de Pandas que represente mejor la información solicitada.

Puede ser:

- Series
- DataFrame

No existe una única estructura obligatoria.

Un método de nivel superior (como generar_resumen()) debe reutilizar primero los métodos existentes antes de acceder directamente al DataFrame.

Y quiero dejarte una idea para el futuro (sin implementarla aún)

Creo que cuando lleguemos al Sprint 6, el archivo config.py va a empezar a crecer mucho. En ese momento propondría crear un directorio como:

config/
│
├── aliases.py
├── patrones.py
├── reemplazos.py
└── settings.py

No ahora.