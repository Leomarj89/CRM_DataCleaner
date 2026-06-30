Los métodos obtener_* devolverán la estructura de Pandas que represente mejor la información solicitada.

Puede ser:

- Series
- DataFrame

No existe una única estructura obligatoria.

Un método de nivel superior (como generar_resumen()) debe reutilizar primero los métodos existentes antes de acceder directamente al DataFrame.