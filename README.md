# Proyecto: Marketplace de Manizales

---

## Descripción

Este proyecto consiste en el desarrollo de un Marketplace para la ciudad de Manizales, Colombia. El objetivo principal es proporcionar una plataforma donde los pequeños emprendedores locales puedan promocionar y vender sus productos, y donde los usuarios puedan explorar, realizar pedidos y comunicarse con los vendedores.

El Marketplace permitirá a los usuarios:

1. Explorar una variedad de productos ofrecidos por emprendedores locales.
2. Realizar pedidos de productos sin realizar pagos en línea, con la opción de pagar contra entrega.
3. Comunicarse directamente con los vendedores a través de la plataforma para realizar consultas y obtener información adicional sobre los productos.
4. Calificar y dejar reseñas sobre los productos adquiridos, brindando retroalimentación valiosa a los vendedores y ayudando a otros usuarios en sus decisiones de compra.

---

## Tecnologías Utilizadas

- **Lenguaje de Programación:** Python
- **Framework Backend:** FastAPI
- **ORM (Mapeo Objeto-Relacional):** SQLAlchemy

---

## Estructura del Proyecto

El proyecto seguirá una arquitectura limpia, organizada en capas para garantizar la modularidad, la escalabilidad y el mantenimiento del código. La estructura del proyecto incluirá las siguientes capas:

1. **Capa API:** Esta capa será responsable de manejar las solicitudes HTTP entrantes y las respuestas salientes. Se utilizará FastAPI para definir los endpoints de la API y gestionar la lógica de las solicitudes.

2. **Capa de Aplicación:** Aquí se ubicará la lógica de negocio de la aplicación. Esta capa será responsable de procesar las solicitudes recibidas desde la capa de presentación, interactuar con la capa de acceso a datos y devolver los resultados apropiados.

3. **Capa Infraestructura:** Esta capa se encargará de interactuar con la base de datos utilizando SQLAlchemy para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los datos de los productos, usuarios y pedidos. Además de tener servicios tercerizados para evitar la exposición de la lógica del negocio.

4. **Capa de Dominio:** En esta capa se definirán los modelos de dominio que representan los objetos principales de la aplicación, como Productos, Usuarios, Pedidos, etc. Estos modelos serán utilizados por las capas superiores para realizar operaciones y manipular los datos.

---

## Instrucciones de Ejecución

1. Clonar el repositorio desde GitHub: `git clone https://github.com/tu_usuario/marketplace-manizales.git`
2. Instalar las dependencias del proyecto: `pip install -r requirements.txt`
3. Configurar la base de datos y el entorno según las especificaciones del archivo `config.py`.
4. Ejecutar la aplicación: `uvicorn main:app --reload`

---

## Autores - CodeSnakes ![CodeSnakes](./resources/images/codesnakes.png)

- Jhonatan Arroyave Gonzales
- Daniel Antonio Giraldo Quintero
- Miguel Angel
- Juan Diego Ramírez Muñoz
- Juan Diego Varón Valencia

## Nota

Este README proporciona una visión general del proyecto y sus componentes principales. Para obtener detalles más específicos sobre la implementación y el funcionamiento del sistema, consulte la documentación técnica y los comentarios dentro del código fuente.

---

![Python](./resources/images/python.png)
![FastAPI](./resources/images/fast-api.png)
![SQLAlchemy](./resources/images/sql-alchemy.png)
